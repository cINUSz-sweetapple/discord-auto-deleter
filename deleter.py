import discord
import asyncio

TOKEN = 'YOUR ACCOUNT TOKEN HERE' # add ur real token

client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    # Only delete messages sent by *you*
    if message.author.id == client.user.id:
        await asyncio.sleep(300)  # auto delete after 300 seconds
      try:
            await message.delete()
            print(f"Deleted: {message.content}")
        except discord.NotFound:
            print("Already deleted.")
        except discord.Forbidden:
            print("No permission to delete.")
        except Exception as e:
            print(f"Error: {e}")

client.run(TOKEN)
