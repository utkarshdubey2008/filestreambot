![GitHub](https://img.shields.io/github/license/utkarshdubey2008/Filestreambot)
[![Bot Support](https://img.shields.io/badge/File%20Stream%20Bot-support%20group-blue)](https://t.me/codexmania)

# GIVE A STAR AND FORK ELSE NO MORE OPENSOURCE 
 <p align="center">
    A Telegram bot to turn all media and documents files to web link .
    <br />
   </strong></a>
    <br />
    <a href="https://github.com/utkarshdubey2008/FileStreamBot/issues">Report a Bug</a>
    |
    <a href="https://github.com/utkarshdubey2008/FileStreamBot/issues">Request Feature</a>
  </p>


<hr>



## 🍁 About This Bot :

![streaming-Professional-live_1](https://user-images.githubusercontent.com/88939380/137127129-a86fc939-2931-4c66-b6f6-b57711a9eab7.png)

</p>
<p align='center'>
    This bot will give you stream links for Telegram files without the need of waiting till the download completes
</p>


## ♢ How to make your own :


#### ♢ Click on This Drop-down and get more details

<br>
<details>
  <summary><b>Deploy on Heroku / Railway:</b></summary>


1. Fork This Repo
2. Click on the button to Deploy and follow steps

<h4> So Follow Above Steps 👆 and then deploy other wise bot won't work</h4>

Press the below button to Fast deploy on Heroku/Raiwlay
Either you could locally host or deploy on [Heroku](https://heroku.com)
### 💜 Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy/)

<br>
Railway
  
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2FCode-X-Mania%2FFilestreambot-pro&envs=API_HASH%2CAPI_ID%2CFQDN%2CDATABASE_URL%2CBOT_TOKEN%2CHAS_SSL%2CNO_PORT%2COWNER_ID%2CPORT%2COWNER_USERNAME%2CSESSION_NAME%2CUPDATES_CHANNEL%2CBIN_CHANNEL%2CMY_PASS&API_HASHDesc=Get+it+from+my.telegram.org&API_IDDesc=Get+it+from+my.telegram.org&FQDNDesc=Your+railway+app+URL&DATABASE_URLDesc=Get+it+from+mongodb.com&BOT_TOKENDesc=Get+it+from+%40botfather&HAS_SSLDesc=Don%27t+touch+this&NO_PORTDesc=keep+default+value.&OWNER_IDDesc=Your+telegram+id&PORTDesc=default&OWNER_USERNAMEDesc=tg+username&SESSION_NAMEDesc=Keep+default+or+enter+your+name&UPDATES_CHANNELDesc=channel+username+without+%40+else+None&BIN_CHANNELDesc=id+of+channel&MY_PASSDesc=Bot+pass&FQDNDefault=EDIT+AFTER+DEPLOYING+THE+BOT+LEAVE+IT+AS+IT+IS+RIGHT+NOW&HAS_SSLDefault=True&NO_PORTDefault=False&OWNER_IDDefault=+get+it+from+%40username_to_id_bot&PORTDefault=8080&SESSION_NAMEDefault=I_love_opensource&UPDATES_CHANNELDefault=None&BIN_CHANNELDefault=also+add+bot+to+it&MY_PASSDefault=adarsh&referralCode=ADARSH)





then goto the <a href="#mandatory-vars">variables tab</a> for more info on setting up environmental variables. </details>

<details>
  <summary><b>Features:</b></summary>
  
<p>

🚀Features<p>
💥Superfast⚡️ download and stream links.<br>
💥No ads in generated links.<br>
💥Superfast interface.<br>
💥Along with the links you also get file information like name,size ,etc.<br>
💥Updates channel Support.<br>
💥Mongodb database support for broadcasting.<br>
💥Password Protection.<br>
💥User Freindly Interface.<br>
💥Ping check.<br>
💥User DC Check.<br>
💥Real time CPU , RAM , Internet usage. <br>
💥Custom Domain support. <br>
💥All unwanted code removed. <br>
💥Removes forwarded tag in channel. <br>
💥A lot more tired of writing check out by deploying it. 
</details>
<details>
  <summary><b>Host it on VPS Locally :</b></summary>


  <summary><b>Vars and Details :</b></summary>

`API_ID` : Goto [my.telegram.org](https://my.telegram.org) to obtain this.

`API_HASH` : Goto [my.telegram.org](https://my.telegram.org) to obtain this.
  
`MY_PASS` : Bot PASSWORD

`BOT_TOKEN` : Get the bot token from [@BotFather](https://telegram.dog/BotFather)

`BIN_CHANNEL` : Create a new channel (private/public), add [@missrose_bot](https://telegram.dog/MissRose_bot) as admin to the channel and type /id. Now copy paste the ID into this field.
  
`OWNER_USERNAME` : U should be knowing it afterall it's your username dont remember ? it just go to settings!

`OWNER_ID` : Your Telegram User ID

`DATABASE_URL` : MongoDB URI for saving User IDs when they first Start the Bot. We will use that for Broadcasting to them. I will try to add more features related with Database. If you need help to get the URI you can ask in [Me Telegram](https://t.me/adarshhh0).

 Option Vars

`UPDATES_CHANNEL` : Put a Public Channel Username, so every user have to Join that channel to use the bot. Must add bot to channel as Admin to work properly.

`BANNED_CHANNELS` : Put IDs of Banned Channels where bot will not work. You can add multiple IDs & separate with <kbd>Space</kbd>.

`SLEEP_THRESHOLD` : Set a sleep threshold for flood wait exceptions happening globally in this telegram bot instance, below which any request that raises a flood wait will be automatically invoked again after sleeping for the required amount of time. Flood wait exceptions requiring higher waiting times will be raised. Defaults to 60 seconds.

`WORKERS` : Number of maximum concurrent workers for handling incoming updates. Defaults to `3`

`PORT` : The port that you want your webapp to be listened to. Defaults to `8080`

`WEB_SERVER_BIND_ADDRESS` : Your server bind adress. Defauls to `0.0.0.0`

`NO_PORT` : If you don't want your port to be displayed. You should point your `PORT` to `80` (http) or `443` (https) for the links to work. Ignore this if you're on Heroku.

`FQDN` :  A Fully Qualified Domain Name if present. Defaults to `WEB_SERVER_BIND_ADDRESS` </details>

<details>
  <summary><b>How to Use :</b></summary>

:warning: **Before using the  bot, don't forget to add the bot to the `BIN_CHANNEL` as an Admin**
 
`/start` : To check if the bot is alive or not.

To get an instant stream link, just forward any media to the bot and boom, its fast af.
  
![image](https://user-images.githubusercontent.com/88939380/145798095-3cdad108-96b0-4391-a540-cad144d6b864.png)


### Channel Support
Bot also Supported with Channels. Just add bot Channel as Admin. If any new file comes in Channel it will edit it with **Get Download Link** Button. </details>
