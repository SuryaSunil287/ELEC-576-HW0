import twitchio
import asyncio

# Twitch bot configuration
bot_username = 'your_bot_username'
oauth_token = 'your_oauth_token'
channel_name = 'target_channel_name'
message_interval = 30  # Time interval in seconds between each message


# Twitch bot class
class TwitchBot(twitchio.Client):
    def __init__(self):
        super().__init__(token=oauth_token, prefix='!', initial_channels=[channel_name])

    async def event_ready(self):
        print(f'Bot is ready. Listening to #{channel_name}')

    async def event_message(self, message):
        if message.author.name.lower() == bot_username.lower():
            return  # Ignore messages from the bot itself

        # Process the received message here if needed

    async def send_periodic_message(self, message):
        while True:
            await self.send_msg(channel_name, message)
            await asyncio.sleep(message_interval)


# Create and run the bot
bot = TwitchBot()
loop = asyncio.get_event_loop()
loop.create_task(bot.send_periodic_message('Your message goes here'))
loop.run_until_complete(bot.run())
