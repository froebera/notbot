import asyncio
import logging
from typing import List

import arrow

from notbot.context import Context, Module
from notbot.db import get_raid_postgres_dao, get_raid_stats_dao
from notbot.models import RaidPlayerAttack, RaidStats

MODULE_NAME = "raid_stat_service"
logger = logging.getLogger(__name__)


class RaidStatService(Module):
    def __init__(self, context: Context):
        self.raid_postgres_dao = get_raid_postgres_dao(context)
        self.raid_stats_dao = get_raid_stats_dao(context)

    def get_name(self):
        return MODULE_NAME

    async def get_raid_for_id(self, raid_id):
        return await self.raid_postgres_dao.get_raid_for_id(raid_id)

    async def get_uncompleted_raids(self, guild_id):
        return await self.raid_postgres_dao.get_uncompleted_raids(guild_id)

    async def get_last_completed_raids(self, guild_id):
        return await self.raid_postgres_dao.get_last_completed_raids(guild_id)

    async def save_raid_player_attacks(self, attacks: List[RaidPlayerAttack]):
        return await self.raid_stats_dao.save_raid_player_attacks(attacks)

    async def check_if_attacks_exist(self, guild_id, raid_id):
        return await self.raid_stats_dao.check_if_attacks_exist(guild_id, raid_id)

    async def has_raid_permission_and_raid_exists(self, guild_id, raid_id):
        return await self.raid_postgres_dao.has_raid_permission_and_raid_exists(
            guild_id, raid_id
        )

    async def get_raid_list(self, guild_id):
        """
            returns the last 10 completed last 10 uncompleted raids
        """

        return await asyncio.gather(
            self.get_uncompleted_raids(guild_id),
            self.get_last_completed_raids(guild_id),
        )

    async def get_raid_player_attacks_for_raid_id(self, raid_id):
        return await self.raid_stats_dao.get_raid_player_attacks_for_raid_id(raid_id)

    async def create_start_raid_stat_entry(self, guild_id, raid_start: arrow.Arrow):
        return await self.raid_postgres_dao.create_start_raid_stat_entry(
            guild_id, raid_start
        )

    async def create_raid_stat_entry(
        self, guild_id, started_at: arrow.Arrow, cleared_at: arrow.Arrow
    ):
        return await self.raid_postgres_dao.create_raid_stat_entry(
            guild_id, started_at, cleared_at
        )

    async def calculate_raid_stats(self, raid_id: int):
        attacks = await self.get_raid_player_attacks_for_raid_id(raid_id)
        raid = await self.get_raid_for_id(raid_id)

        min_dmg, max_dmg, min_avg, max_avg, min_hits, max_hits, total_dmg, total_avg = (
            -1,
            0,
            -1,
            0,
            -1,
            0,
            0,
            0,
        )
        for attack in attacks:
            _attack_avg = (
                0 if not attack.total_hits else attack.total_dmg / attack.total_hits
            )

            total_dmg += attack.total_dmg
            total_avg += _attack_avg

            if attack.total_dmg > max_dmg:
                max_dmg = attack.total_dmg

            if min_dmg == -1 or attack.total_dmg < min_dmg:
                min_dmg = attack.total_dmg

            if attack.total_hits > max_hits:
                max_hits = attack.total_hits

            if min_hits == -1 or attack.total_hits < min_hits:
                min_hits = attack.total_hits

            if _attack_avg > max_avg:
                max_avg = _attack_avg

            if min_avg == -1 or _attack_avg < min_avg:
                min_avg = _attack_avg

        raid_stats = RaidStats(
            min_dmg,
            max_dmg,
            round(total_dmg / len(attacks), 2),
            round(min_avg, 2),
            round(max_avg, 2),
            round(total_avg / len(attacks), 2),
            min_hits,
            max_hits,
            total_dmg,
            len(attacks),
            raid.started_at,
            raid.cleared_at,
        )

        return raid_stats

    async def delete_raid_entry(self, raid_id):
        await self.delete_attacks_for_raid(raid_id)
        await self.raid_postgres_dao.delete_raid_entry(raid_id)

    async def delete_attacks_for_raid(self, raid_id):
        await self.raid_stats_dao.delete_attacks_for_raid(raid_id)

    async def load_raid_data_for_stats(self, guild_id, raid_id):
        """
            Loads the data needed to create the stats for the given raid_id
            ( Will include the previous raid if possible )
        """
        raid_data = await self.raid_stats_dao.load_raid_data_for_stats(
            guild_id, raid_id
        )

        return raid_data


def get_raid_stat_service(context: Context) -> RaidStatService:
    return context.get_or_register_module(MODULE_NAME, lambda: RaidStatService(context))
