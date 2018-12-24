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


# Display all warframes 10 at once
def genWarframeMenu(expandList):
    warframeEmbed = discord.Embed(
        title='All Warframes',
        colour=discord.Colour.dark_teal()
    )
    warframeEmbed.set_thumbnail(url='https://bit.ly/2RlTq6p')  # Display server logo ;)
    lAllWarframes = []
    lWarframeInfo = wfDatabase.getAllWarframes()  # Get warframe info from database
    for warframe in lWarframeInfo:
        lAllWarframes.append(warframe[0])  # Store warframe names into the lAllWarframes list
    if expandList == 0:  # If list is on page 1 of 4
        intIterations = 0
        while (intIterations <= 9):  # Display 10 warframes at once
            if lAllWarframes[intIterations] != 'Excalibur Umbra':
                warframeEmbed.add_field(name=lAllWarframes[intIterations],
                                        value='https://warframe.fandom.com/wiki/' + lAllWarframes[intIterations],
                                        inline=False)  # Update with the 1st half of the Warframe list
            else:
                warframeEmbed.add_field(name=lAllWarframes[intIterations],
                                        value='https://warframe.fandom.com/wiki/Excalibur#Umbra',
                                        inline=False)  # Update with the 1st half of the Warframe list
            intIterations += 1
        warframeEmbed.set_footer(text="(Page 1 of 4)")
    elif expandList == 1:  # Page 2 of 4
        intIterations = 10
        while (intIterations <= 19):
            warframeEmbed.add_field(name=lAllWarframes[intIterations],
                                    value='https://warframe.fandom.com/wiki/' + lAllWarframes[intIterations],
                                    inline=False)  # Update with the 1st half of the Warframe list
            intIterations += 1
        warframeEmbed.set_footer(text="(Page 2 of 4)")
    elif expandList == 2:  # Page 3 of 4
        intIterations = 20
        while (intIterations <= 29):
            warframeEmbed.add_field(name=lAllWarframes[intIterations],
                                    value='https://warframe.fandom.com/wiki/' + lAllWarframes[intIterations],
                                    inline=False)  # Update with the 1st half of the Warframe list
            intIterations += 1
        warframeEmbed.set_footer(text="(Page 3 of 4)")
    else:  # Page 4 of 4
        intIterations = 30
        while (intIterations < len(lAllWarframes)):
            warframeEmbed.add_field(name=lAllWarframes[intIterations],
                                    value='https://warframe.fandom.com/wiki/' + lAllWarframes[intIterations],
                                    inline=False)  # Update with 2nd half of the Warframe list
            intIterations += 1
        warframeEmbed.set_footer(text="(Page 4 of 4)")

    return warframeEmbed  # Pass back the embed to be used in the main file


# Display information about a user selected warframe
def genPreview(lWarframeInfo, prime):
    if prime:
        if lWarframeInfo[13] == "Excalibur Umbra":
            previewEmbed = discord.Embed(
                title=lWarframeInfo[0],
                url='https://warframe.fandom.com/wiki/Excalibur#Umbra%20Prime',
                colour=discord.Colour.dark_grey()
            )
            previewEmbed.set_footer(text='Note: This warframe is currently unobtainable and cannot be farmed')
        else:
            previewEmbed = discord.Embed(
                title=lWarframeInfo[0],
                url='https://warframe.fandom.com/wiki/' + lWarframeInfo[13] + "#Prime",
                colour=discord.Colour.gold()
            )
            previewEmbed.set_footer(text='(Version: pre pre pre alpha early access dlc edition preorder)')
    else:
        if lWarframeInfo[0] == "Excalibur Umbra":
            previewEmbed = discord.Embed(
                title=lWarframeInfo[0],
                url='https://warframe.fandom.com/wiki/Excalibur#Umbra',
                colour=discord.Colour.light_grey()
            )
            previewEmbed.set_footer(text='(Version: pre pre pre alpha early access dlc edition preorder)')
        else:
            previewEmbed = discord.Embed(
                title=lWarframeInfo[0],
                url='https://warframe.fandom.com/wiki/' + lWarframeInfo[0],
                colour=discord.Colour.blue()
            )
            previewEmbed.set_footer(text='(Version: pre pre pre alpha early access dlc edition preorder)')
    previewEmbed.add_field(name='Description',
                           value=lWarframeInfo[1],
                           inline=False)
    previewEmbed.add_field(name='Mastery Requirement',
                           value=lWarframeInfo[4],
                           inline=False)
    previewEmbed.add_field(name='Health',
                           value=lWarframeInfo[5],
                           inline=False)
    previewEmbed.add_field(name='Shield',
                           value=lWarframeInfo[6],
                           inline=False)
    previewEmbed.add_field(name='Armour',
                           value=lWarframeInfo[7],
                           inline=False)
    previewEmbed.add_field(name='Energy',
                           value=lWarframeInfo[8],
                           inline=False)
    previewEmbed.add_field(name='Sprint Speed',
                           value=lWarframeInfo[9],
                           inline=False)
    previewEmbed.add_field(name='Polarities',
                           value=lWarframeInfo[10],
                           inline=False)
    previewEmbed.add_field(name='Exilus Polarity',
                           value=lWarframeInfo[11],
                           inline=False)
    previewEmbed.add_field(name='Aura Polarity',
                           value=lWarframeInfo[12],
                           inline=False)
    previewEmbed.set_thumbnail(url=lWarframeInfo[3])  # Display Warframe chosen
    return previewEmbed  # Pass back to main file
