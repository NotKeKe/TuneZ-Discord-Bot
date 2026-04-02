---
layout: default
title: Register Discord Bot
lang: en
permalink: /en/register-discord-bot/
breadcrumb:
  - title: Home
    url: /en/
  - title: Register Discord Bot
---

## Register Discord Bot
If you don't have a Discord account yet, go register one first ~~this should be self-explanatory~~

### Registration
1. Go to [Discord Developer Application](https://discord.com/developers/applications)
![Application Site](/assets/docs/Register_Discord_Bot/assets/application_site.png)
2. Click "New Application" in the top right corner
    - Enter the name you want your Bot to be called in the Name field
    - Click By clicking...... ~~( Translation: If you click create, you agree to Discord's [Developer Terms of Service](https://support-dev.discord.com/hc/articles/8562894815383-Discord-Developer-Terms-of-Service) and [Developer Policy](https://support-dev.discord.com/hc/articles/8563934450327-Discord-Developer-Policy) )~~
    - Click Create
![New Application](/assets/docs/Register_Discord_Bot/assets/new_application.png)

### Enable Permissions
3. After creating, you should be taken to this page. Click "Bot" in the left Settings column, then give bot intents for it to work properly
![Created Application](/assets/docs/Register_Discord_Bot/assets/created_application.png)
4. After clicking, scroll down and check all three of these options
    - Remember to click "Save Changes" at the bottom - I won't screenshot this, I'm a bit lazy ww
![Click Intents](/assets/docs/Register_Discord_Bot/assets/click_intents.png)
5. (1) Click **Installation** in the left column, we need to let Discord know it's a Bot ~~(because a plain application can also be used to show Discord status (rich presence))~~
    - (2) Click the **Scopes** dropdown and select bot
    - After clicking, **Permission** will appear below - these are the permissions the Bot will get by default when joining a server
    - Click the following options in that menu:
        - Add Reactions (Add reactions)
        - Attach Files (Send files/images)
        - Connect (Connect to channels)
        - Embed Links (Send embeds - you know those nicely formatted messages you see but can't create yourself)
        - Read Message History (Read channel message history)
        - Send Messages (Send messages)
        - Speak (Speak)
        - Use Slash Commands (Use slash commands, not sure if this is needed)
        - View Channels (View channels)
![Set Installation - Bot](/assets/docs/Register_Discord_Bot/assets/installation_bot.png)

### Get Token and Invite Link
6. Next, get the Token - this is super important, without it your Bot will never start
    - (1) Go to "Bot" in the left Settings column    
    - (2) Click "Reset Token"
    - Click the red button (Yes, do it!) - it's asking if you're sure you want to reset the Token
        - Since we haven't used this Bot at all, resetting is fine
    - After clicking, it might ask you to verify, maybe enter your password. Or if you have Multi-Factor Authentication enabled, that might be required too.
![Reset Token](/assets/docs/Register_Discord_Bot/assets/reset_token.png)
7. After that, you should see your Token, copy it (click Copy, or you can manually copy)
    - **Keep this Token, don't share it with others, you'll need it when starting the Discord Bot!**
![Get Token](/assets/docs/Register_Discord_Bot/assets/copy_token.png)
8. Get the Bot invite link
![Get Invite URL](/assets/docs/Register_Discord_Bot/assets/get_invite_url.png)
