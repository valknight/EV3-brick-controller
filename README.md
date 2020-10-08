# EV3 Brick Controller

## Purpose

This project is designed as a template for the code running on a LEGO EV3 brick that is designed to interact with [ev3-remote-control-server](https://github.com/valknight/ev3-remote-control-server). To run this, your ev3 should run ev3dev (information on how to set this up can be found on their website)

This script is designed to work with an EV3 that has two wheels (one on the left, one on the right) allowing for movement, as well as an arm that raised and lowers. It has been tested running over Bluetooth (using network sharing), however should be functional and more reliable when communicating directly using a USB wifi adapter.

## Requirements

- EV3 running the ev3dev operating system, or other device compatible with ev3dev
    - Testing has only been carried out on an ev3 brick, so support cannot be guaranteed for other setups
- Functioning installation of [ev3-remote-control-server](https://github.com/valknight/ev3-remote-control-server)
- Network connectivity on the ev3, either via Bluetooth network sharing, or via a USB wifi adapter

## Setup

Note: if you are new to ev3dev, the default SSH password is `maker`

1. Clone the repository to your local machine (or the EV3 if SSH'ed in)
2. Change out config.py as to your requirements
3. Deploy the codebase onto the ev3
4. Copy the file named "robot.json" to the ev3's home directory (/home/robot)
5. Change file as follows:
    - Change the ID to match the rest of your fleet of ev3s
    - Change the name to be what you wish end users using the server to see
    - Change the key to match the `robot-key` ev3-remote-control-server is using
    - Change the host to match the address at which ev3-remote-control-server can be reached

## Configuration

The configuration files in `config.py` should be labelled as to their reason - please refer to these comments for details on what each option does. 