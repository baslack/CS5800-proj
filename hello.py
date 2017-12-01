import machine
import re
import os
import sys

if __name__ == "__main__":
    #path = input("Please input directory you want to use?")
    path = "/home/brandon/Documents/5800/CS5800-proj/configs/ex_821.tm"
    if os.path.isfile(path) and os.access(path, os.R_OK):
        tm = machine.TM(path)
        value = "abababaaa"
        mytape = machine.TMTape(value)
        tm.load(mytape)
    else:
        print("BAD JOKE")

    pass
    filepath = os.path.join("..", "configs", "ex_821.tm")
    myMT = TM(filepath)
    myTape = TMTape("aa")
    myMT.load(myTape)
    # print(myMT.get_c())
    for config in myMT.exec():
        print(config)
        # print(myMT.dumps())

#print("Example as home,brandon,Documents,5800,CS5800-proj,configs,ex_821.tm")
 #       tm = machine.TM(path)
  #      value = input("Please input the tape you want to use?")
   #     print("You have entered:" + value)
    #home,brandon,Documents,5800,CS5800-proj,configs,ex_821.tm