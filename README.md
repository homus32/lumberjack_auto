## Description
This bot is for the game [LumberJack](https://tbot.xyz/lumber/)

The game is available on Telegram via a bot `@gamebot lumberjack`

## Installation


#### Poetry
```
git clone <REPO_URI>
cd <REPO_NAME>
poetry install
```

### pip

```
git clone <REPO_URI>
cd <REPO_NAME>
pip install requirements.txt
```

## Usage
In order to configure the bot, you need to specify the coordinates with the mouse cursor, where 
it can be found a branch that can hit on the head.
Place the coordinate above the character's head.

`Ctrl + 1` - set the coordinate on the screen for the left side.

`Ctrl + 2` - set the coordinate on the screen for the right side.

`Ctrl + 3` - enable / disable the bot.

### Settings
Be sure to go into the code and change the value of `monitor` for correct work

```python
left = Point(x = 621, y = 333) # Fixed coordinates for the left side
right = Point(x = 742, y = 333) # Fixed coordinates for the left side


monitor = {
    'top': 0, # must always be zero
    'left': 0, # must always be zero
    'width': 1366, # screen size (width)
    'height': 768 # screen size (length)
}

INTERVAL = 0.059 # 59 ms. Picked up the maximum speed
RANGE = 130 # 130 pixels. Maximum value.

```