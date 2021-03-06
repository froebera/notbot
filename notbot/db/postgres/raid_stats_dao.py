from typing import List
import arrow

from notbot.context import Context, Module
from notbot.models import RaidPlayerAttack, RaidAttacks

from .postgres_dao_base import PostgresDaoBase

MODULE_NAME = "raid_stats_dao"


class RaidStatsDao(PostgresDaoBase, Module):
    def get_name(self):
        return MODULE_NAME

    async def check_if_attacks_exist(self, guild_id, raid_id):
        async with self.connection() as connection:
            res = await connection.fetchval(
                """
                SELECT 1
                FROM raid r
                JOIN raid_player_attack rpa
                    on rpa.raid_id = r.id
                WHERE
                r.guild_id = $1
                AND r.id = $2
                GROUP BY 1
                """,
                str(guild_id),
                raid_id,
            )
            return res == True

    async def save_raid_player_attacks(self, attacks: List[RaidPlayerAttack]):
        async with self.connection() as connection:
            await connection.executemany(
                """
                INSERT INTO raid_player_attack
                    (raid_id, player_id, player_name, total_hits, total_dmg)
                VALUES (
                    $1, $2, $3, $4, $5
                ) 
                """,
                [rpa.iter() for rpa in attacks],
            )

    async def get_raid_player_attacks_for_raid_id(self, raid_id):
        result: List[RaidPlayerAttack] = []
        async with self.connection() as connection:
            res = await connection.fetch(
                """
                SELECT *
                FROM raid_player_attack
                WHERE raid_id = $1
                """,
                raid_id,
            )
            for row in res:
                result.append(self._map_row_to_rpa_model(row))

        return result

    async def delete_attacks_for_raid(self, raid_id):
        async with self.connection() as connection:
            res = await connection.execute(
                """
                DELETE FROM raid_player_attack
                WHERE
                    raid_id = $1
            """,
                raid_id,
            )
            print(res)

    async def load_raid_data_for_stats(self, guild_id, raid_id):
        async with self.connection() as connection:
            res = await connection.fetch(
                """
                SELECT *
                FROM raid r
                JOIN raid_player_attack rpa on rpa.raid_id = r.id
                WHERE r.id in ($1,
                     (
                         SELECT id
                         FROM raid
                         JOIN raid_player_attack rpa on rpa.raid_id = id
                         WHERE
                            cleared_at < (
                                SELECT cleared_at
                                FROM raid
                                WHERE id = $1
                            )
                            AND cleared_at IS NOT NULL
                            AND started_at IS NOT NULL
                            AND guild_id = $2
                         ORDER BY cleared_at DESC
                         LIMIT 1
                     )
                )
                ORDER BY cleared_at DESC, rpa.total_dmg DESC
                """,
                raid_id,
                str(guild_id),
            )
            # print(res)
            models: List[RaidAttacks] = []
            records = []
            r_id = None
            for record in res:
                if not r_id:
                    r_id = int(record["id"])
                    records.append(record)
                else:
                    if r_id == int(record["id"]):
                        records.append(record)
                    else:
                        r_id = int(record["id"])
                        models.append(self._map_row_array_to_raid_attack_model(records))
                        records.clear()
                        records.append(record)
            models.append(self._map_row_array_to_raid_attack_model(records))

            return models

    def _map_row_to_rpa_model(self, row) -> RaidPlayerAttack:
        return RaidPlayerAttack(
            row["raid_id"],
            row["player_id"],
            row["player_name"],
            row["total_hits"],
            row["total_dmg"],
        )

    def _map_row_array_to_raid_attack_model(self, rows) -> RaidAttacks:
        raid_player_attacks: List[RaidPlayerAttack] = []
        for row in rows:
            raid_player_attacks.append(
                RaidPlayerAttack(
                    int(row["raid_id"]),
                    row["player_id"],
                    row["player_name"],
                    int(row["total_hits"]),
                    int(row["total_dmg"]),
                )
            )

        return RaidAttacks(
            int(rows[0]["id"]),
            arrow.get(rows[0]["started_at"]) if rows[0]["started_at"] else None,
            arrow.get(rows[0]["cleared_at"]) if rows[0]["cleared_at"] else None,
            rows[0]["guild_id"],
            raid_player_attacks,
        )


def get_raid_stats_dao(context: Context) -> RaidStatsDao:
    return context.get_or_register_module(MODULE_NAME, lambda: RaidStatsDao(context))
