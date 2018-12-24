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


def genRelicCatEmbed():
    urlLithRelic = "http://bit.ly/LRelic"
    urlMesoRelic = "http://bit.ly/MRelic"
    urlNeoRelic = "http://bit.ly/NeoRelicIMG"
    urlAxiRelic = "http://bit.ly/ARelic"
    relicCategoriesEmbed: Embed = discord.Embed(
        title='Void Relic Categories',
        color=discord.Colour.gold()
    )
    relicCategoriesEmbed.add_field(name='Lith', value='** **')
    relicCategoriesEmbed.add_field(name='Meso', value='** **')
    relicCategoriesEmbed.add_field(name='Neo', value='** **')
    relicCategoriesEmbed.add_field(name='Axi', value='** **')
    relicCategoriesEmbed.set_footer(text='(Version: pre pre pre alpha early access dlc edition preorder)')
    relicCategoriesEmbed.set_thumbnail(url='https://bit.ly/2RlTq6p')
    randomNumber = random.randint(0, 3)
    if randomNumber == 0:
        relicCategoriesEmbed.set_thumbnail(url=urlLithRelic)
    elif randomNumber == 1:
        relicCategoriesEmbed.set_thumbnail(url=urlMesoRelic)
    elif randomNumber == 2:
        relicCategoriesEmbed.set_thumbnail(url=urlNeoRelic)
    else:
        relicCategoriesEmbed.set_thumbnail(url=urlAxiRelic)
    return relicCategoriesEmbed


def genPrimeDetEmbed(primeDetailList):
    primeDetailsEmbed = discord.Embed(
        title=primeDetailList[0][0],
        color=discord.Colour.gold()
    )
    for primeDetail in primeDetailList:
        lRelicInfo = wfDatabase.getRelicByPart(primeDetail[0], primeDetail[1])
        sRelicInfo = ""
        intLengthOfRelicInfo = len(lRelicInfo) - 1
        for relicInfoPointer in range(len(lRelicInfo)):
            sRelicInfo += lRelicInfo[relicInfoPointer][1] + " " + lRelicInfo[relicInfoPointer][2] + " (" \
                          + lRelicInfo[relicInfoPointer][3] + ")"
            if relicInfoPointer != intLengthOfRelicInfo:
                sRelicInfo += " | "
        primeDetailsEmbed.add_field(name=primeDetail[1], value=sRelicInfo)
        primeDetailsEmbed.set_thumbnail(url=lRelicInfo[relicInfoPointer][5])
    isVaulted = wfDatabase.checkIfVaulted(primeDetailList[0][0])[0][0]
    if isVaulted != 'Yes':
        primeDetailsEmbed.set_footer(text="This item's relics can be farmed and is not vaulted! \
        (Note: Some relics maybe vaulted however)")
    else:
        primeDetailsEmbed.set_footer(text="WARNING: This item is in the Prime Vault and therefore, it's relics \
        CANNOT be farmed outside of trading!")
    return primeDetailsEmbed


def retrieveDropsInOrder(tier, name):
    def setEmbedColor(tier, name):
        urlLithRelic = "http://bit.ly/LRelic"
        urlMesoRelic = "http://bit.ly/MRelic"
        urlNeoRelic = "http://bit.ly/NeoRelicIMG"
        urlAxiRelic = "http://bit.ly/ARelic"
        if tier == "Lith":
            relicDropsEmbed = discord.Embed(
                title=tier + " " + name,
                color=discord.Colour.dark_orange()
            )
            relicDropsEmbed.set_thumbnail(url=urlLithRelic)
        elif tier == "Meso":
            relicDropsEmbed = discord.Embed(
                title=tier + " " + name,
                color=discord.Colour.dark_grey()
            )
            relicDropsEmbed.set_thumbnail(url=urlMesoRelic)
        elif tier == "Neo":
            relicDropsEmbed = discord.Embed(
                title=tier + " " + name,
                color=discord.Colour.light_grey()
            )
            relicDropsEmbed.set_thumbnail(url=urlNeoRelic)
        elif tier == "Axi":
            relicDropsEmbed = discord.Embed(
                title=tier + " " + name,
                color=discord.Colour.gold()
            )
            relicDropsEmbed.set_thumbnail(url=urlAxiRelic)
        return relicDropsEmbed

    relicDropEmbed: object = setEmbedColor(tier, name)
    lDropRarities = ["Common", "Uncommon", "Rare"]
    for rarity in lDropRarities:
        # Retrieve the drops and store in list for each rarity
        lRarityDrops = wfDatabase.getPartByRelicAndRarity(tier, name, rarity)
        rarityItems = ""
        intLengthOfRarityDrops = len(lRarityDrops) - 1
        for dropPointer in range(len(lRarityDrops)):
            rarityItems += lRarityDrops[dropPointer][0] + " " + lRarityDrops[dropPointer][1]
            if dropPointer != intLengthOfRarityDrops:
                rarityItems += " | "
        relicDropEmbed.add_field(name=rarity, value=rarityItems)
    return relicDropEmbed


def genRelicDetEmbed(relicTier, relicName, relicDetailList):
    relicDetailsEmbed = discord.Embed(
        title=(relicTier + " " + relicName),
        color=discord.Colour.gold()
    )
