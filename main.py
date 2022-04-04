#! /usr/bin/python3

import sys
import sqlite3
import datetime as date

def startTimer():
    print("start")


def endTimer():
    print("end")


def showLastWeek():
    return


def showToday():
    return


try:
    # takes cli argument to start the timer
    if (sys.argv[1] == "-s" or sys.argv[1] == "--start"):
        startTimer()
    # takes cli argument to end the timer
    elif (sys.argv[1] == "-e" or sys.argv[1] == "--end"):
        endTimer()
    # takes cli argument to show all of last week's timers
    elif (sys.argv[1] == "-w" or sys.argv[1] == "--week"):
        print("2022-03-29: 7h")
        print("2022-03-30: 8h")
        print("2022-03-31: 7h")
        print("2022-04-01: 0h")
        print("2022-04-02: 0h")
        print("2022-04-03: 6h")
        print("2022-04-04(today): 3h")
        print("Total time: 21h")
    # takes cli argument to show all of the current day's timers
    elif (sys.argv[1] == "-d" or sys.argv[1] == "--day"):
        print("10:02 - 11:05: 1h03")
        print("13:00 = 15:00: 2h00")
except:
    print("Not a valid option")
    print("Valid options are:")
    print("* -s or --start to start the timer")
    print("* -e or --end to end the timer")
    print("* -d or --day to show timers of the current day")
    print("* -w or --week to show the past week")
