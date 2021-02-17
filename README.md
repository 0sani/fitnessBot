# Fitness Bot

## What it does

Randomly sends a message telling you to do fitness whenever you send something in discord

<<<<<<< HEAD
## Features

### Set server odds:

Administrators can set the odds of the bot triggering. The default value for this is 50

Command: `!change_odds <newOdds>`

Ex: `!change_odds 10` will change the odds of the bot triggering to 1 in 10.

### Set message:

Administrators can set the message the bot will send when it tells a user to exercise. By default, the message will be in the form `<user>: do <exercise>`. An example of this would be `@Osani: do 25 squats`

Command: `!change_message <newMsg>`

Ex: `!change_message "Please do"`

### Add or remove channels where the bot can be active

Sometimes, there might be channels where it would be inappropriate for the bot to be active. In this case, you can exclude channels and unexclude them from a list.

Command: `!exclude_channel <channel>` to remove, `!unexclude_channel <channel>` to add it again

Ex: `!exclude_channel 808606611047710730`

=======
## Set Up

Create a file called `config.py` and add a variable called `bot_id`. Set this variable equal to the discord user id of the bot account, as an int
>>>>>>> c289a76ab99ca099017e34edd9357cf2b682e62a

## How to run

`python3 fitness.py <insert discord token here>`

