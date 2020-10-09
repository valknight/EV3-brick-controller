# Change this if you are not debugging on a robot, but instead using a local client to test features
# Note: this is not recommended for most development, as micropython is used instead of standard python
# Avoid if possible.
running_on_robot = True
# disable this if you are running on robot but want to disable the actual movement part
do_movement = True
# Debug mode disables clearing and will print raw json received, and any errors will be shown
debug = False
# disable if your robot does not have an arm
arm_enabled = True
# configure which output is the arm
arm_position_dxown = 10
arm_position_up = 0
turn_speed_multiplier = 0.5
forward_turn_multiplier = 1
# Get font list from https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/console.html#console-fonts
font = "Lat15-VGA8.psf.gz"
# Change if you want your brick to go slower or faster
# Around 30-50 is best for a EV3 connected to a server over bluetooth
speed = 40
# The following import is used 
if running_on_robot:
    from ev3dev2.motor import list_motors, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, MoveJoystick

if running_on_robot:
    # Change output_B and C respectively if you wire your wheels differently
    left_wheel, right_wheel = OUTPUT_B, OUTPUT_C
    arm_port = OUTPUT_A
    # The following means we    
    drive = MoveJoystick(left_wheel, right_wheel)