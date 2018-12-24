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


def getHotfixes():
    def genHotFixEmbed(lPatchNotes: object) -> object:
        hotfixEmbed = discord.Embed(title='Warframe Patch Notes',
                                    color=discord.Colour.dark_orange()
                                    )
        for patch in lPatchNotes:
            hotfixEmbed.add_field(name=patch[0],
                                  value=patch[1],
                                  inline=False)
        hotfixEmbed.set_footer(
            text='All patch notes can be found here: https://forums.warframe.com/forum/3-pc-update-notes/'
        )
        hotfixEmbed.set_thumbnail(url='http://bit.ly/WarframeLogo')
        return hotfixEmbed  # Pass back embed

    # Initialise lists
    lPatchNoteLinks = []
    lPatchNoteNames = []
    lCombinedPatch = []

    site_request = requests.get("https://forums.warframe.com/forum/3-pc-update-notes/")  # Scrape warframe forums
    soup = BeautifulSoup(site_request.content, "html.parser")  # Set parser
    patchLinks = soup.find_all(attrs={'href': re.compile("https://forums.warframe.com/topic/")},
                               class_=False)
    for link in patchLinks:
        if "?page=1 " in (link.get('href') + " "):  # Remove any links past page 1
            lPatchNoteLinks.append(link.get('href'))

    patchNames = soup.find_all(attrs={'title': re.compile(": Update|: Hotfix")})  # Retrieve patch names
    for name in patchNames:
        lPatchNoteNames.append(name.get('title'))

    for indexPointer in range(7):  # Only 7 patch notes please for the love of god don't fill my screen
        patchTuple: tuple[Any] = tuple((lPatchNoteNames[indexPointer], lPatchNoteLinks[indexPointer]))  # Store combined
        lCombinedPatch.append(patchTuple)

    return genHotFixEmbed(lCombinedPatch)  # Passback embed to main file
