#!/usr/bin/env python3

import pickle
import datetime

try:
    with open("counterfile.txt", "rb") as file:
        counterDict = pickle.load(file)
except FileNotFoundError:
    counterDict = {"testCounter": datetime.date(2022, 6, 1)}

while True:
    print()
    print("My Counters:".center(40, "-"))
    for counter, init_time in counterDict.items():
        print(f"{counter:25s}: {datetime.date.today() - init_time}")
    print("".center(40, "-"))
    choice = input("\nPress:\n'a' to add Counter\n's' to reset Counter\n'd' to delete Counter\n'q' to quit\n\n\n")
    if choice == "a":
        counterDict[input("\nChoose a name for the counter: \n")] = datetime.date.today()
    if choice == "s":
        reset = input("\nInput name of counter to reset: \n")
        if reset in counterDict:
            counterDict[reset] = datetime.date.today()
        else:
            print(" No such counter! ".center(40, "+"))
    if choice == "d":
        delete = input("\nInput name of counter to delete: \n")
        if delete in counterDict:
            counterDict.pop(delete)
        else:
            print(" No such counter! ".center(40, "+"))
    if choice == "q":
        print("\n\n\nThank you for using PyCounter!\n\n\n")
        break

with open("counterfile.txt", "wb") as file:
    pickle.dump(counterDict, file)
