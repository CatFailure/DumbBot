# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
from typing import Any

import discord
from discord import Embed
from discord.ext.commands import Bot
import random
import asyncio
import WarframeDatabase as wfDatabase
import time
import random

# Website scraping
from bs4 import BeautifulSoup
import requests
import re


# Display information about a user selected warframe
def gen_gun_embed(weapon_info_list):
    weapon_embed = discord.Embed(
        title=weapon_info_list[0],
        colour=discord.Colour.dark_teal()
    )
    weapon_embed.add_field(name='Damage',
                           value=weapon_info_list[2],
                           inline=False)
    weapon_embed.add_field(name='Trigger Type',
                           value=weapon_info_list[1],
                           inline=False)
    weapon_embed.add_field(name='Critical Chance',
                           value=weapon_info_list[3],
                           inline=False)
    weapon_embed.add_field(name='Critical Multiplier',
                           value=weapon_info_list[4],
                           inline=False)
    weapon_embed.add_field(name='Status Chance',
                           value=weapon_info_list[5],
                           inline=False)
    weapon_embed.add_field(name='Projectile Type',
                           value=weapon_info_list[6],
                           inline=False)
    weapon_embed.add_field(name='Fire Rate',
                           value=weapon_info_list[7],
                           inline=False)
    weapon_embed.add_field(name='Magazine Size',
                           value=weapon_info_list[8],
                           inline=False)
    weapon_embed.add_field(name='Reload Speed',
                           value=weapon_info_list[9],
                           inline=False)
    weapon_embed.add_field(name='Mastery Requirement',
                           value=weapon_info_list[10],
                           inline=False)
    weapon_embed.add_field(name='Riven Disposition',
                           value=weapon_info_list[11],
                           inline=False)
    weapon_embed.set_thumbnail(url=weapon_info_list[12])
    return weapon_embed  # Pass back to main file
