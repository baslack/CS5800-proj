import machine
import re
import os
import sys

if __name__ == "__main__":
    print("Please input a valid path name? Path name must be in this format: /home/Documents/....../file.tm")
    path = input("Enter:")
    #path = "/home/brandon/Documents/5800/CS5800-proj/configs/ex_821.tm"

    if os.path.isfile(path) and os.access(path, os.R_OK):
        tm = machine.TM(path)
        value = input("Please input the tape you want to use?")
        #value = "ababba"
        #print(tm.tapealpha)

        # Benjamin A. Slack: 12.1.17
        # Why are you checking the input twice?
        # You are attempting to check it here with
        # the if statement. Then you check it again
        # on load. Either or would do.
        #
        # If you're checking it here, you need to make a
        # set from the input, not a list. Example:
        # set(value)
        # read your docs:
        # https://docs.python.org/3/tutorial/datastructures.html#sets
        # you don't even need to give it a name. Just
        # call the methods on the object at creation time
        # Example
        # if (set(value).isSubset(tm.alpha)):
        # ...

        valuelist = list(value)
        #print (valuelist)
        fox = tm.alpha
        if (fox.issubset(valuelist)):
            mytape = machine.TMTape(value)
            try:
                tm.load(mytape)
                for config in tm.exec():
                    print(config)
                    if 'Rejected:' in config:
                        print("The input: " + value + " entered did NOT the final state. The final state:")
                        print(tm.accept)

                    elif 'Accepted:' in config:
                        print("Congratulations: " + value + " was ACCEPTED.")

            # Benjamin A. Slack : 12.1.17
            # if you're going to handle an exception,
            # you should use the info the exception gives you
            # Example:
            # except machine.InvalidCharacterInTape as e:
            #     print(type(e), *e.args)
            # this would print out what went wrong and why
            except:
                print("Invalid input for machine!")

        else:
            print("The entered tape is not a subset of the Language:")
            print(tm.tapealpha)

    else:
        print("BAD PATHFILE")
pass