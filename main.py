#!/usr/bin/env python3
import sys
import random


#TODO: make it cleanr/refavtor

def monty_hall_wins(N):
    doors = ['goat', 'goat', 'car']
    wins = 0
    loss = 0

    for turn in range(N):
        random.shuffle(doors)
        init_door = random.randint(0, 2)

        
        goat1 = doors.index('goat')
        goat2 = doors.index('goat', goat1+1)

        # open a door with a goat by the host
        if goat1 == init_door:
            open_door = goat2    
        elif goat2 == init_door:
            open_door = goat1
        else:
            # chooose the car, so open 1 of them goat doors
            open_door = random.choice([goat1, goat2])

        # swap doors all the time
        final_door = 3 - (open_door + init_door)

        if doors[final_door] == 'car':
            wins += 1
        else:
            loss += 1

    return (wins, loss)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        N = int(sys.argv[1])
    else:
        print("Usage: main.py [iterations]", file=sys.stderr)
        exit(1)

    results = monty_hall_wins(N)
    print(f"Tries {N}\nP(Win/Swap): {results[0]/N} P(Loss/Swap): {results[1]/N}")
