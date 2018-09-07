#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# <bitbar.title>Deep Work</bitbar.title>
# <bitbar.version>v0.1/bitbar.version>
# <bitbar.author>Jonas Zagatta</bitbar.author>
# <bitbar.author.github>zagatta-sonah</bitbar.author.github>
# <bitbar.desc>Deep Work Helper</bitbar.desc>
# <bitbar.dependencies>python3</bitbar.dependencies>
import datetime
from pathlib import Path

PATH = "/Users/jonaszagatta/Gitprojects/deep_work/deep_work.txt"
SEPARATOR_TIME = "|"
SEPARATOR_HOURS = "/"

class Counter:
    def __init__(self, hours_worked, hours_wasted):
        self.hours_worked = int(hours_worked)
        self.hours_wasted = int(hours_wasted)

def log_exists():
    log_path = Path(PATH)
    if log_path.is_file():
        return True
    else:
        return False

def get_counter():
    if (not log_exists()):
        initialize()
    log = open(PATH,"r")
    firstline = log.readline()
    position_time = firstline.find(SEPARATOR_TIME)
    position_hours_worked = firstline.find(SEPARATOR_HOURS)
    position_end = firstline.find("\n")
    hours_worked = firstline[position_time+1:position_hours_worked]
    hours_wasted = firstline[position_hours_worked+1:position_end]
    counter = Counter(hours_worked, hours_wasted)
    return  counter

def print_stats():
    counter = get_counter()
    print_str = "hours_worked: " + str(counter.hours_worked) + ", hours_wasted: " + str(counter.hours_wasted)
    print(print_str)

def print_stats_short():
    counter = get_counter()
    print_str = str(counter.hours_worked) + "/ " + str(counter.hours_wasted)
    print(print_str)

def write_log_entry(hours_worked, hours_wasted):
    log_old = ""
    if (log_exists()):
        log = open(PATH,"r")
        log_old = log.read()
        log.close()

    log = open(PATH,"w")
    log_text = str(datetime.datetime.now()) + SEPARATOR_TIME + str(hours_worked) + SEPARATOR_HOURS + str(hours_wasted)+"\n"
    log.write(log_text)
    log.write(log_old)
    log.close()

def initialize():
    write_log_entry(0,0)

print_stats_short()
