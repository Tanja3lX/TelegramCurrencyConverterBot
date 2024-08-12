# TelegramCurrencyConverterBot

This bot allows users to convert currencies directly within Telegram. It provides a simple interface for quickly checking exchange rates and supports several key commands.

Key Features and Commands:

```/start``` Displays a welcome message and provides a list of available commands

```/values``` Lists all available currencies that the bot can convert

```/support``` Provides the support email address for users to contact in case of issues.

You can use the bot to convert currency by sending a message in the following format:
```<amount> <currency_1> <currency_2>```

The bot will respond with the equivalent value of currency_2 for the specified amount of currency_1.

This bot is not currently hosted online. To use it, you'll need to clone this repository and run the bot locally on your machine.

To get the bot up and running, you'll need to install the following Python packages: 

```
pip install requests
pip install pyTelegramBotAPI
```
