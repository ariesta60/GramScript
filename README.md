<div align="center">
  <img src="./img/logo-icon.svg" alt="alt text" width="200px">
  <h1>Instagram Selenium Bot</h1>
</div>


# 🔥 Version 0.1.3 🔥

This is the first version of this Instagram bot. Much more is to come in future and this is just a working beta. It's easy to use and very simple for now. I am planning on adding much more features in the future and automate a lot more processes. My goal is to create a Instagram script which is able to run 24/7 without beeing detected by Instagram.

Find more of my Selenium Bots here: http://selenium-bots.000webhostapp.com/

# Instagram Selenium Bot

🚀 Automate your Instagram Account 🚀

📌 Ver. 0.1.3 📌

⚠ No Proxy Support yet ⚠️

## Features

* Watch all Stories from feed
    * Brower is muted for story watching
    * Custom limit on stories being watched
* Like recent posts from a certain hashtag
    * Detects if post already got liked by user
    * Custom limit on media's being liked
* Comment on recent posts from a certain hashtag
    * Detects if post already got commented by user
    * Custom limit on media's being commented

### Support 👨‍💻

Any problems with running the script and any questions please cantact me via Twitter [@hendrik_bgr](https://twitter.com/Hendrik_bgr)

Or via email under [hendriksdevmail@gmail.com](mailto:hendriskdevmail@gmail.com)

Or Email the whole team [Email Us](mailto:Instagram-Selenium-Bot@protonmail.com)
### Prerequisites

You need python 3 installed on your System.

As well as Selenium and the Firefox Webdriver

(Place the geckodriver file in the main directory)

Get a copy of the Project. Open your Terminal and enter:

```
git clone https://github.com/hendrikbgr/Instagram-Selenium-Bot
```

To install all needed requirements run the following command in the project directory:
(coming soon...)

```
pip install -r requirements.txt
```

After that you can proceed to edit the Script.

### Edit Script

Open the /utils folder and open the readme.txt file

There will instructions on how the change the config files.

Also open bot.py and change the max rate limits.

(On line 23 to 25)

## Running 🏃🏽‍♂️

To run this script open your Terminal in the project directory.

To start the script enter:

```
python bot.py
```

## Authors

* **Hendrik Bgr** - *Initial work* - [HendrikBgr](https://github.com/hendrikbgr)
    * **Twitter** - *Initial work* - [HendrikBgr](https://twitter.com/hendrik_bgr)


## Acknowledgments

* Hat tip to anyone whose code was used

## To Do List 📝

* Add follow script
* Add unfollow script
* Store information in database so the same media wont get targeted twice
* Add inputs for rate limits on startup & optional create config file.

## Known Bugs 🐛

* Still watches stories even tho they already got watched.


