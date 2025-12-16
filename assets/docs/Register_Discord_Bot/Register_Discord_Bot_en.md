<div align="center">

[![Docs](https://img.shields.io/badge/Docs-繁體-blue.svg)](Register_Discord_Bot.md)
[![Docs](https://img.shields.io/badge/Docs-简体中文-blue.svg)](Register_Discord_Bot_simp_chinese.md) 

</div>


## Registering a Discord Bot
If you don't have a Discord account yet, go register one first ~~I shouldn't need to teach you this, right?~~

### Registration
1. Go to the [Discord Developer Application](https://discord.com/developers/applications) website.
![Application Site](./assets/application_site.png)
2. Click **New Application** in the top right corner.
    - Enter the name you want for your Bot in the **Name** field.
    - Click "By clicking......" ~~(Translation: If you click create, it means you agree to Discord's [Developer Terms of Service](https://support-dev.discord.com/hc/articles/8562894815383-Discord-Developer-Terms-of-Service) and [Developer Policy](https://support-dev.discord.com/hc/articles/8563934450327-Discord-Developer-Policy) )~~
    - Click **Create**.
![New Applicaiotn](./assets/new_application.png)

### Enabling Permissions
3. After creating it, you should land on a page like this. Click **Bot** under the Settings menu on the left. Next, you need to give the bot **intents** for it to work properly.
![Created Application](./assets/created_application.png)
4. After clicking, scroll down and check all three options.
    - Remember to click **Save Changes** at the bottom. I'm not screenshotting this part, kinda lazy lol.
![Click Intents](./assets/click_intents.png)
5. (1) Click **Installation** on the left menu. We need to let Discord know it's a Bot ~~(because a simple application can also be used just to show Discord Rich Presence status)~~.
    - (2) Click the dropdown under **Scopes** and select **bot**.
    - After clicking, **Permissions** will appear below. These are the default permissions given to the Bot when it joins a server.
    - Check the following options in that menu:
        - Add Reactions
        - Attach Files
        - Connect
        - Embed Links (sending embeds, you know those cool layouts you see but can't type out yourself)
        - Read Message History
        - Send Messages
        - Speak
        - Use Slash Commands (not sure if we actually need this one, though)
        - View Channels
![Set Installation - Bot](./assets/installation_bot.png)

### Getting the Token & Invite Link
6. Next, get the Token. This is super important; without it, your Bot will never start.
    - (1) Go to **Bot** under the Settings menu on the left.
    - (2) Click **Reset Token**.
    - Click the red button (Yes, do it!). It's asking if you're sure you want to reset the Token.
        - Since we haven't even used this Bot yet, resetting it doesn't matter.
    - After clicking, it might ask for verification, like your password. Or if you have Multi-Factor Authentication enabled, you might need that too.
![Reset Token](./assets/reset_token.png)
7. Once finished, you should be able to see your Token. Copy it (Click Copy, or highlight and copy manually, whatever).
    - **Keep this Token safe and don't give it to anyone. You'll need it later when starting the Discord Bot!**
![Get Token](./assets/copy_token.png)
8. Get the Bot Invite Link
![Get Invite URL](./assets/get_invite_url.png)