# discord-auto-deleter
deletes ur discord messages automatically after a set time u choose.

# Auto Message Deleter (Self Bot)

This self-bot automatically deletes messages sent by the user after a predefined delay (e.g., 5 minutes). It's designed for Discord users who want to keep their message history private or clear up their conversations after a short period.

Built using Python and the `discord.py` library, this bot allows users to set a custom timer for each message, ensuring automatic deletion after the timer expires.

## Features:
- **Self-Bot Integration**: Deletes messages sent by the user without affecting other users.
- **Customizable Delay**: Set the delay for message deletion (default: 5 minutes).
- **Automatic Operation**: Once configured, the bot runs in the background and handles message deletion automatically.
- **Easy Setup**: Simple configuration with a few lines of code to get started.

## Requirements:
- Python 3.12+
- `discord.py-self` library
- A Discord bot token (self-bot)
- Basic Python knowledge for setup

## Installation:

### Step 1: Install Dependencies
Make sure you have Python 3.12+ installed on your system. Then, install the required libraries by running the following command:

```bash
pip install discord.py-self

### Step 2: Clone the Repository
Clone this repository to your local machine using the following command:

bash
Copy code
git clone https://github.com/cINUSz-sweetapple/discord-auto-deleter.git cd auto-message-deleter

### Step 3: Configure the Bot
Download 'deleter.py' and configure the script.

Add your Discord bot token inside deleter.py like this:

TOKEN = 'YOUR_BOT_TOKEN'

Also change the time you want yout messages to be deleted after.
### It should look like this:

# await asyncio.sleep(300)

here 300 means messages will be deleted after 300 seconds.
