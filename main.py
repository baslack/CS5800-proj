import machine
import re
import os
import sys

if __name__ == "__main__":
    # Benjamin Slack: 11.29.17
    # this obviously needs to be turned into something that
    # gets a valid path from the user. We can't have it hard
    # coded like this.
    filepath = os.path.join(os.path.expanduser("~"), "Documents", "5800", "CS5800-proj", "configs", "ex_821.tm")
    tm = machine.TM(filepath)
    value = input("Please input the tape you want to use?")
    # Benjamin Slack: 11.29.17
    # Andrew, this is likely something you can do easier
    # the TM has data members containing is tape alphabet
    # you can take your input string and do the following:
    # if set(value).isSubset(tm.tapealpha):
    # then do your work
    # else throw an error message
    # in python, data members are public unless hidden
    # explicitly
    print("You have entered:"+value)
    #if re.match('ab', value):
    if ('a' in value) or ('b' in value):
        # No character other then . a, b was found
        print("The input entered: " + value + " is valid.")
        # Benjamin Slack: 11.29.17
        # The Tape object has a __str__ method, so you can simply
        # print it, like you would any string. It will automatically
        # give you the internal string with blanks on either end.
        print("The tape being used will be:Б" + value + "Б")
        mytape = machine.TMTape(value)
        tm.load(mytape)
        for config in tm.exec():
            print(config)
            if 'Rejected:' in config:
                print("The input: " + value + " entered did NOT get to the final state of q3.")
                print("Therefore the input was REJECTED by this machine.")
            elif 'Accepted:' in config:
                print("Congratulations: " + value + " was ACCEPTED because it reached the final state q3.")
            #else:
                #print("The input: " + value + " entered did HALTED.")
    else:
        # Character other then . a-z 0-9 was found
        print("The input entered is invalid. The input must only be the characters a or b")
        sys.exit()
    pass
