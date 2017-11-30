import machine
import re
import os
import sys

if __name__ == "__main__":
    path = input("Please input directory you want to use?")
    if os.path.isfile(path) and os.access(path, os.R_OK):
        print("Example as /home/brandon/Documents/5800/CS5800-proj/configs/ex_821.tm")
        tm = machine.TM(path)
        value = input("Please input the tape you want to use?")
        print("You have entered:" + value)
        prog = re.compile('(a|b)*$')
        if prog.match(value):
            mytape = machine.TMTape(value)
            tm.load(mytape)
            for config in tm.exec():
                print(config)
                if 'Rejected:' in config:
                    print("The input: " + value + " entered did NOT get to the final state of q3.")
                    print("Therefore the input was REJECTED by this machine.")
                elif 'Accepted:' in config:
                    print("Congratulations: " + value + " was ACCEPTED because it reached the final state q3.")
        else:
            print("The input entered is invalid. The input must only be the characters a or b")
            sys.exit()
    else:
        print("This Directory not exists.")