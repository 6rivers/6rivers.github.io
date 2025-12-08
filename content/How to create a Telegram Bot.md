Title: How to create a Telegram bot
Date: 2022-08-22
Category: General
Summary: Create a Telegram bot to integrate within any application 
opengraph_image: telegram_bot.jpg


Telegram is a great platform to send your application alerts to your users. To create a telegram bot for yourself, you can follow the below steps.

Open the Telegram app on your mobile or desktop and search for "BotFather", or you may use this [link](https://telegram.me/botfather) for that. And enter `/start`

![image0]({static}images/20220817132237.png)

Then you would be presented with a number of options to try. But to create a new bot enter or click on `/newbot`

![image1]({static}images/20220817132315.png)

Now it asks for the bot name and 'username' for it, where *username should end with 'bot'*. 

And since it should be unique, your preferred username might have already been taken by others. But eventually, you are going to get a new username and an access token for it

![image2]({static}images/20220817133338.png)

Now, you have a new bot, which Telegram users can find and use it. 

When a user sends `/start` to your bot, you will have new updates for this bot at `https://api.telegram.org/bot{your_bot_token}/getUpdates` (replace {your_bot_token} with the token you got in the above step). You can use any browser to see the results.

To make the results look good, you can use[JSON Formatter](https://chrome.google.com/webstore/detail/json-formatter/mhimpmpmffogbmmkmajibklelopddmjf) extension if you are using a chrome browser. You will get information like the user's name, username, chat_id, and the text the user has sent to you.

![image3]({static}images/20220817140345.png)

You can integrate this within your application by using the chat_id to send alerts or custom messages to the user.