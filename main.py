import machine
import re
import os
import sys

if __name__ == "__main__":
    # Benjamin Slack: 11.30.17
    # this gets you a string, but it may or may
    # may not be a valid path. Python is platform
    # independent but paths are not. You need to process
    # the input path to ensure that it gets written
    # out appropriately using str.split and os.path.join
    path = input("Please input directory you want to use?")
    if os.path.isfile(path) and os.access(path, os.R_OK):
        # Benjamin Slack: 11.30.17
        # why are you printing this? Your if checked for
        # an existing file and access. Both had to pass to
        # get here, so they don't need to see an example path
        print("Example as /home/brandon/Documents/5800/CS5800-proj/configs/ex_821.tm")
        tm = machine.TM(path)
        value = input("Please input the tape you want to use?")
        print("You have entered:" + value)
        # Benjamin Slack: 11.30.17
        # again, a and b are not the only legitmate
        # characters for a machine config. You can't
        # hard code this into your tape checking. Some
        # tapes might contain a,b and c? Some might contain
        # 0 and 1. You need to use the machine configuration
        # to check which strings are valid input. As I mentioned,
        # I modified TM so that loading a tape with invalid
        # characters will result in an InvalidCharacterInTape
        # exception. You should either: 1. read the machine
        # alphabet right of the machine (e.g. tm.alpha) or
        # use a try/except handler to catch exception
        prog = re.compile('(a|b)*$')
        if prog.match(value):
            mytape = machine.TMTape(value)
            tm.load(mytape)
            for config in tm.exec():
                print(config)
                if 'Rejected:' in config:
                    # Benjamin Slack: 11.30.17
                    # again, you can not hard code the states into the
                    # output either. States could be named anything, not
                    # just q0, q1, q2, q3. They could be A, B, C, or
                    # 000, 0000, 00000. You have to query the machine
                    # to get these states.
                    # In addition, the rejected status is part of the
                    # trace exec returns. You don't need to print it again.
                    print("The input: " + value + " entered did NOT get to the final state of q3.")
                    print("Therefore the input was REJECTED by this machine.")
                elif 'Accepted:' in config:
                    print("Congratulations: " + value + " was ACCEPTED because it reached the final state q3.")
        else:
            print("The input entered is invalid. The input must only be the characters a or b")
            sys.exit()
    else:
        print("This Directory not exists.")