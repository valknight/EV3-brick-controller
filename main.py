#!/usr/bin/env micropython
from time import sleep, time
import json
from config import *
if running_on_robot:
    from urllib.urequest import urlopen
    from urequests import request
    from ev3dev2.console import Console
    from ev3dev2.motor import list_motors, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, MoveJoystick
    console = Console()
    console.set_font(font)
else:
    from requests import request


def get_robot_data():
    try:
        with open('../robot.json', 'r') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        pass
    try:
        with open('robot.json', 'r') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        raise FileNotFoundError(
            "Could not find file in either current directory or higher level directory")


data = get_robot_data()
robotName = data['name']
robotId = data['id']
robotKey = data['key']
host = data['host']

postData = json.dumps({
    "robotId": robotId,
    "robotName": robotName,
    "robotKey": robotKey})

buttons = []
oldest_time = "/"

def get_commands():
    # TODO: fix this for local debugging purposes
    # TODO: revert to old urequests way of getting data - it was more reliable, and the latency difference isn't noticiable
    s = request("POST", "{}/robot".format(host), json=postData)
    return s.json()



def refresh_display(buttons):
    # Manage screen
    if not debug:
        console.reset_console()
    global oldest_time
    print("Running")
    print("ID {}".format(robotId))
    print("Name: {}".format(robotName))
    print("Latency: {}ms".format(oldest_time))
    # Handle latency calculation
    if len(buttons) > 0:
        oldest_time = buttons[0]['time']
        for button in buttons:
            if button['time'] < oldest_time:
                oldest_time = button['time']
        oldest_time = time() * 1000 - oldest_time

def handle_movement(buttons):
    x, z = buttons['coords'][0], buttons['coords'][2]
    z *= speed
    x *= (speed * turn_speed_multiplier)
    if z:
        x *= forward_turn_multiplier
    if do_movement:
        drive.on(x, z)


while True:
    try:
        j = get_commands()
        buttons = j['buttons']
        refresh_display(buttons)
        handle_movement(j)
    except Exception as e:
        if debug:
            print(e)
        pass
    sleep(0.01)
