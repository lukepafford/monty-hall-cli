# monty-hall-cli
Simulate Monty Hall game thousands of times to see probablity over time

## Usage

### Default options
```
❯ python3 monty-hall.py
MONTY HALL GAME
===============
Games Played: 10000
Choice: keep_door
Number Of Doors: 3
Won: 3354
Lost: 6646
Choosing keep_door resulted in winning 33.54% of the time
```

### Change game settings
```
❯ python3 monty-hall.py --choice change_door --number-of-games 10000 --door-count 3
MONTY HALL GAME
===============
Games Played: 10000
Choice: change_door
Number Of Doors: 3
Won: 6689
Lost: 3311
Choosing change_door resulted in winning 66.89% of the time
```

### View help
```
❯ python3 monty-hall.py --help
usage: monty-hall.py [-h] [--choice {keep_door,change_door}] [--number-of-games NUMBER_OF_GAMES] [--door-count DOOR_COUNT]

Monty Python game N number of times

optional arguments:
  -h, --help            show this help message and exit
  --choice {keep_door,change_door}
                        Keep or change your original door (default: keep_door)
  --number-of-games NUMBER_OF_GAMES
                        How many games shall we play (default: 10000)
  --door-count DOOR_COUNT
                        number of doors to choose from (default: 3)
```
