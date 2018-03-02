# IxionBot

A simple Telegram Bot

## Simple use

1. Talk to [BotFather](https://telegram.me/BotFather) to get token and proper rights
1. Install requirements: `pip3 install -r requirements.txt`
1. Copy `config-example.yml` to `config.yml`, and edit it
1. `python3 main.py`

## Autorun?

1. Talk to [BotFather](https://telegram.me/BotFather) to get token and proper rights
1. Install `supervisor` and `virtualenv`
1. Establish virtualenv: `virtualenv -p /usr/bin/python3 venv`
1. Active Virtualenv: `source venv/bin/activate`
1. Install requirements: `pip3 install -r requirements.txt`
1. Copy `config-example.yml` to `config-YOURBOT.yml`, and edit it
1. `sudo tools/install.sh YOURBOT`

## Update?

`sudo tools/upgrade.sh`, then ALL your bots will reboot.