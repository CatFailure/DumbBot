# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
from discord.ext.commands import Bot
import asyncio
import WarframeDatabase as wfDatabase
import querying_warframes as query_wf
import querying_relics as query_relic
import querying_html as query_html
import querying_weapons as query_weap

# Bot token
TOKEN = "NDc2MTMwMzc2ODQzMTMyOTQ5.Dus8Gg.NWW1YN279fFIbfk__TT6UOxHzEM"

# Define a prefix
BOT_Prefix = "="

client = Bot(command_prefix=BOT_Prefix)

client.remove_command("help")


# DEFAULT ERROR MESSAGE
def errorMessage():
    errorEmbed = discord.Embed(title="ERROR!",
                               color=discord.Colour.red()
                               )
    errorEmbed.add_field(name="Invalid query!",
                         value="Item queried does not exist! Check spelling and command usage and try again!",
                         inline=False)
    errorEmbed.set_thumbnail(url='https://i.redd.it/752n4wf5i6f11.png')
    return errorEmbed  # Pass back to main file

# # Create the command decorator
# @client.command(aliases=['t', 'test'],
#                 description="Test command",
#                 brief="Test command",
#                 pass_context=True)
# # Function to randomly select a phrase on command "dh speak"
# async def bot_test(context):
#     if context.message.author.id != "173726112180994048":
#         await client.say(context.message.author.mention + ", you cannot use this command!")
#     else:
#         wfDatabase.addBlanks()


# Create the command decorator
# INVITE COMMAND
@client.command(name='Invite to server',
                aliases=['invite', 'inv'],
                description="Invite this bot to your server!",
                brief="Invite this bot to your server!",
                pass_context=True)
async def invite_bot(context):
    inviteEmbed = discord.Embed(
        title="Invite BotFrame!",
        colour=discord.Colour.magenta()
    )
    inviteEmbed.add_field(name="http://bit.ly/inviteDumbBot",
                          value='Invite DumbBot to your server with this link!',
                          inline=False)
    inviteEmbed.set_thumbnail(url='https://bit.ly/2RlTq6p')  # Display server logo ;)
    await client.send_message(context.message.channel, embed=inviteEmbed)


# Create the command decorator
@client.command(name='Item Information',
                aliases=['info', 'i', 'information'],
                description="Find information about a Warframe",
                brief="Find information about a Warframe",
                pass_context=True)
async def warframe_list(context, *option):
    if option[0].lower() == 'a' or option[0].lower() == 'all':
        page_number = 0
        warframeEmbed: object = query_wf.genWarframeMenu(page_number)  # Generate the embed list (25 cap) # (0 is page number)
        warframeList = await client.send_message(context.message.channel, embed=warframeEmbed)  # Send and store embed
        # Add reactions to interact with
        await client.add_reaction(warframeList, '1⃣')
        await asyncio.sleep(0.6)
        await client.add_reaction(warframeList, '2⃣')
        await asyncio.sleep(0.6)
        await client.add_reaction(warframeList, '3⃣')
        await asyncio.sleep(0.6)
        await client.add_reaction(warframeList, '4⃣')
        await asyncio.sleep(0.6)
        await client.add_reaction(warframeList, '❌')

        @client.event
        async def on_reaction_add(reaction, user):
            if user.name != client.user.name:
                if reaction.emoji == '1⃣':
                    page_number = 0
                    updatedWfEmbed: object = query_wf.genWarframeMenu(page_number)
                    await client.remove_reaction(warframeList, '1⃣', user)
                elif reaction.emoji == '2⃣':
                    page_number = 1
                    updatedWfEmbed: object = query_wf.genWarframeMenu(page_number)
                    await client.remove_reaction(warframeList, '2⃣', user)
                elif reaction.emoji == '3⃣':
                    page_number = 2
                    updatedWfEmbed: object = query_wf.genWarframeMenu(page_number)
                    await client.remove_reaction(warframeList, '3⃣', user)
                elif reaction.emoji == '4⃣':
                    page_number = 3
                    updatedWfEmbed: object = query_wf.genWarframeMenu(page_number)
                    await client.remove_reaction(warframeList, '4⃣', user)
                if reaction.emoji != '❌':
                    await client.edit_message(warframeList, embed=updatedWfEmbed)
                else:
                    await client.delete_message(warframeList)

    else:  # Search database for specific warframe
        combinedOption = ''
        for word in option:
            combinedOption = combinedOption + " " + word.lower().capitalize()
        lItemInfo = wfDatabase.getWarframeInfo(combinedOption.strip())  # Retrieve specific warframe from database
        if len(lItemInfo) != 0:
            previewEmbed: object = query_wf.genPreview(lItemInfo[0], False)
            previewEmbed.set_footer(text='(Version: pre pre pre alpha early access dlc edition preorder)')
            warframePreview = await client.send_message(context.message.channel,
                                                        embed=previewEmbed)  # Display warframe info
            if lItemInfo[0][2] != 'N/A':  # Check for primed version
                await client.add_reaction(warframePreview, '⬆')
                await asyncio.sleep(0.6)
                await client.add_reaction(warframePreview, '❌')
            else:
                await client.add_reaction(warframePreview, '❌')
        else:  # QUERY ERROR!
            lItemInfo = wfDatabase.getWeaponInfo(combinedOption.strip())[0]
            gunEmbed: object = query_weap.gen_gun_embed(lItemInfo)
            gunPreview = await client.send_message(context.message.channel,
                                                        embed=gunEmbed)  # Display warframe info
            if len(lItemInfo) == 0:
                errorEmbed: object = errorMessage()
                await client.send_message(context.message.channel, embed=errorEmbed)

        @client.event
        async def on_reaction_add(reaction, user):
            if user.name != client.user.name:
                await client.remove_reaction(warframePreview, '❌', client.user)
                if reaction.emoji == '⬆':
                    await client.remove_reaction(warframePreview, '⬆', user)
                    await client.remove_reaction(warframePreview, '⬆', client.user)
                    lPrimeItemInfo = wfDatabase.getPrimeInfo(
                        lItemInfo[0][2])  # Retrieve Prime info from database
                    primePreviewEmbed: object = query_wf.genPreview(lPrimeItemInfo[0], True)
                    await client.edit_message(warframePreview, embed=primePreviewEmbed)  # Display prime stats
                    await client.add_reaction(warframePreview, '⬇')
                    await asyncio.sleep(0.6)
                    await client.add_reaction(warframePreview, '❌')
                elif reaction.emoji == '⬇':
                    await client.remove_reaction(warframePreview, '⬇', user)
                    await client.remove_reaction(warframePreview, '⬇', client.user)
                    regularPreviewEmbed: object = query_wf.genPreview(lItemInfo[0], False)
                    await client.edit_message(warframePreview, embed=regularPreviewEmbed)  # Display prime stats
                    await client.add_reaction(warframePreview, '⬆')
                    await asyncio.sleep(0.6)
                    await client.add_reaction(warframePreview, '❌')
                elif reaction.emoji == '❌':
                    await client.delete_message(warframePreview)  # Close embed


# Create the command decorator
@client.command(name='Prime/Relic drops',
                aliases=['r', 'rel', 'relic'],
                description="Find information about Primes/Relics",
                brief="Find information about Primes/Relics",
                pass_context=True)
async def relic_list(context, *option):
    if len(option) == 0:
        relicOptionsEmbed: object = query_relic.genRelicCatEmbed()
        await client.send_message(context.message.channel, embed=relicOptionsEmbed)
    else:
        if option[0].lower() == 'a' or option[0].lower() == 'all':
            relicInfoEmbed = discord.Embed(
                title='Void Relic Information',
                url='https://warframe.fandom.com/wiki/Void_Relic',
                color=discord.Colour.gold()
            )
            relicInfoEmbed.add_field(name='All Void Relic information can be found here',
                                     value='https://warframe.fandom.com/wiki/Void_Relic',
                                     inline=False)
            relicInfoEmbed.set_thumbnail(url='https://bit.ly/2RlTq6p')  # Server logo
            await client.send_message(context.message.channel, embed=relicInfoEmbed)
        else:
            searchQuery = ''
            for i in option:
                searchQuery = searchQuery + " " + i.lower().capitalize()
            if searchQuery.strip() != "Forma":  # Search database for prime item
                primeDetails: object = wfDatabase.searchItem(searchQuery.strip())
                if len(primeDetails) != 0:
                    primeDetailsEmbed = query_relic.genPrimeDetEmbed(primeDetails)
                    await client.send_message(context.message.channel, embed=primeDetailsEmbed)
                else:
                    relicTier = option[0].lower().capitalize()
                    relicName = option[1].capitalize()
                    relicDropsEmbed = query_relic.retrieveDropsInOrder(relicTier, relicName)
                    await client.send_message(context.message.channel, embed=relicDropsEmbed)
                    if len(relicDropsEmbed) == 0:
                        errorEmbed = errorMessage()
                        await client.send_message(context.message.channel, embed=errorEmbed)
            else:  # Forma searched
                formaEmbed = discord.Embed(
                    title="Forma",
                    url="https://warframe.fandom.com/wiki/Forma",
                    color=discord.Colour.gold()
                )
                formaEmbed.add_field(name="All forma drop locations (100+) can be found here:",
                                     value="https://warframe.fandom.com/wiki/Forma")
                formaEmbed.set_thumbnail(url="http://bit.ly/FormaPicture")
                await client.send_message(context.message.channel, embed=formaEmbed)


# Create the command decorator
@client.command(name='Patch Notes',
                aliases=['pn','patchnotes', 'patch', 'notes'],
                description="Displays recent patch notes",
                brief="Displays recent patch notes",
                pass_context=True)
async def patchnotes(context):
    patchEmbed = query_html.getHotfixes()
    await client.send_message(context.message.channel, embed=patchEmbed)


# Ran every time the bot is activated
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    # Create the database and tables
    wfDatabase.create_Database()
    wfDatabase.createTables()
    # lHitOrMiss = ["Hit or miss, I guess", "they never miss, huh?", "You got a boyfriend,",
    #               "I bet he doesn't kiss ya", "He gon' find another girl", "and he won't miss ya",
    #               "He gon' skrrt and", "hit the dab like Wiz Khalifa", "You play with them balls",
    #               "like it’s FIFA", "You won every level,", "you’re the leader, ooh", "You used to work",
    #               "at Whataburger", "Now you pop your", "pussy for the", "Warner Brothers",
    #               "Shots fired,", "you’re fired", "You’re washed up,", "you’re retired",
    #               "Your kitty looks like", "a flat tire", "I bet that your", "kitty real tired", "Perfect!"
    #               ]
    # while not client.is_closed:
    #     for trashLyric in lHitOrMiss:
    #         await client.change_presence(game=discord.Game(name=trashLyric, type=1))  # Set game playing
    #         await asyncio.sleep(5)
    await client.change_presence(game=discord.Game(name="as Tracer", type=1))  # Set game playing


# Define a function to print the current servers
async def list_servers():
    # Make the bot wait until it is ready
    await client.wait_until_ready()
    # Whilst the client is NOT closed
    while not client.is_closed:
        # Print the current servers by iterating through them
        print("Current servers: ")
        for server in client.servers:
            print(server.name)
        # Don't say it again for 1000 minutes for the love of god
        await asyncio.sleep(60000)


@client.event  # MAKE COMMANDS CASE INSENSITIVE
async def on_message(message):
    message.content = message.content.lower()
    await client.process_commands(message)

client.loop.create_task(list_servers())
client.run(TOKEN)
