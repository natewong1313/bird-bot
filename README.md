# Bird Bot
Bird Bot is an auto-checkout bot that currently supports Walmart. It is intended to be used to purchase Nintendo Switch consoles. More sites will be added in the future.

* Easy to use interface built on PyQt5
* Waits for items to restock if they are out of stock
* Optional price checker
* Lighting fast auto-checkout

<p align="center">
  <img src="https://i.imgur.com/E105F74.png" alt="Bird Bot UI" width="738">
</p>

## Getting Started
Here's what you need to do to get Bird Bot installed on your computer.

### Prerequisites
* **Python 3** - you can download it [here](https://www.python.org/downloads/release/python-360/) (scroll down). When you run the installer, make sure you select "Add Python 3.6 to PATH"
### Installation
```sh
git clone https://github.com/natewong1313/bird-bot.git
cd bird-bot
pip install -r requirements.txt
```
If you don't have git installed, you can instead download the repository [here](https://github.com/natewong1313/bird-bot/archive/master.zip). Then cd into it and run `pip install -r requirements.txt`

## Usage
To start the bot, run 
```sh
python app.py
```
To start making tasks, you will first need to setup a profile. A profile contains your shipping, billing, and payment details that are used to checkout. Click the wallet icon on the sidebar and you will the profiles page. Once you've filled out your information, name the profile and then click the save button. You can use the load profile dropdown to check existing profiles or delete profiles.

<p align="center">
  <img src="https://i.imgur.com/BTTki9y.png" alt="Bird Bot Profiles" width="738">
</p>

After you're done making a profile, you will want to create a task. Tasks will automatically checkout the item if it is instock, or wait for it to restock. You can run as many tasks as you would like. To make a task, go back to the homepage and click the add task button in the top right

<p align="center">
  <img src="https://i.imgur.com/Kya9pbe.png" alt="Bird Bot Popup" width="438">
</p>
