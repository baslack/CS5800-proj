import machine
import re
import os
import sys

if __name__ == "__main__":
    #parse_commands(sys.argv)
    filepath = os.path.join(os.path.expanduser("~"), "Documents", "5800", "CS5800-proj", "configs", "ex_821.tm")
    tm = machine.TM(filepath)

    value = input("Please input the tape you want to use? ")
    print("You have entered:" + value)
    pattern = r'[a,b]'
    if re.search(pattern, value):
        # Character other then . a-z 0-9 was found
        print("The input entered is invalid. The input must only be the characters a or b")
        sys.exit()
    else:
        # No character other then . a, b was found
        print("The input entered: " + value + " is valid.")
        print("The tape being used will be:Б" + value + "Б")
        mytape = machine.TMTape(value)
        tm.load(mytape)
        #myTape = TMTape("abbbababba")
        for config in tm.exec():
           print(config)
    pass
