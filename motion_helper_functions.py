from serial_comm import *
import time

# Axis used for Gantry control
GANTRY_X_AXIS = "X"
GANTRY_Y_AXIS = "Y"
BLADE_AXIS = "Z"
# PRESSURE_PLATE_AXIS = "A"
DEFAULT_GANTRY_SPEED = 200
DEFAULT_GANTRY_ACCELERATION = 300
DEFAULT_BLADE_SPEED = 12
DEFAULT_BLADE_ACCELERATION = 30
HOME = "G28"
MOVE = "G0"
SPEED = "M203"
ACCELERATION = "M201"
RELATIVE_MOTION = "G91"
ABSOLUTE_MOTION = "G90"
VACUUM_ON = 255
VACUUM_OFF = 0
PUMP = "M106 P0 S"
MOVE_GRIPPER = "A"
RESET_DYNAMIXEL = 'R'
CURRENT_GRIPPER_POS = 'P'

def home_gantry_X():
    move_blade_to(50)
    motorController.write((HOME + GANTRY_X_AXIS + "\n").encode())
    time.sleep(0.1)
    print("gantry X axis homing")


def home_gantry_Y():
    motorController.write((HOME + GANTRY_Y_AXIS + "\n").encode())
    time.sleep(0.1)
    print("gantry Y axis homing")

def home_vertical_gantry():
    motorController.write((HOME + BLADE_AXIS + "\n").encode())
    time.sleep(0.1)
    print("gantry vertical homing")


"""
    Relative motion functions for motion in individual axis direction
"""


# Gantry axis direction

def move_blade_forward_by(delta):
    _move_Y_gantry_by(delta)


def move_blade_backward_by(delta):
    _move_Y_gantry_by(-1 * delta)


def move_gantry_left_by(delta):
    _move_X_gantry_by(delta)


def move_gantry_right_by(delta):
    _move_X_gantry_by(-1 * delta)


def _move_X_gantry_by(delta):
    motorController.write((RELATIVE_MOTION + "\n").encode())
    motorController.write((MOVE + GANTRY_X_AXIS + str(delta) + "\n").encode())
    motorController.write((ABSOLUTE_MOTION + "\n").encode())

def _move_Y_gantry_by(delta):
    motorController.write((RELATIVE_MOTION + "\n").encode())
    motorController.write((MOVE + GANTRY_Y_AXIS + str(delta) + "\n").encode())
    motorController.write((ABSOLUTE_MOTION + "\n").encode())


def move_X_gantry_to(abs_pos):
    motorController.write((MOVE + GANTRY_X_AXIS + str(abs_pos) + "\n").encode())

def move_Y_gantry_to(abs_pos):
    motorController.write((MOVE + GANTRY_Y_AXIS + str(abs_pos) + "\n").encode())

# Blade axis commands
def move_blade_up_by(delta):
    _move_blade_by(-1*delta)


def move_blade_down_by(delta):
    _move_blade_by(delta)


def _move_blade_by(delta):
    motorController.write((RELATIVE_MOTION + "\n").encode())
    motorController.write((MOVE + BLADE_AXIS + str(delta) + "\n").encode())
    motorController.write((ABSOLUTE_MOTION + "\n").encode())


def move_blade_to(abs_pos):
    motorController.write((MOVE + BLADE_AXIS + str(abs_pos) + "\n").encode())


def grab_blade():
    motorController.write((PUMP + str(VACUUM_ON) + "\n").encode())


def release_blade():
    motorController.write((PUMP + str(VACUUM_OFF) + "\n").encode())


def move_blade_at_2d_plane(y, z):
    motorController.write((ABSOLUTE_MOTION + "\n").encode())
    motorController.write((MOVE + GANTRY_Y_AXIS + str(y) + BLADE_AXIS + str(z) + "F300" + "\n").encode())
    motorController.write((MOVE + "F3000" + "\n").encode())


#pressure plate lock unlock
# def lock_pressure_plate():
#     motorController.write((ABSOLUTE_MOTION + "\n").encode())
#     motorController.write((MOVE + PRESSURE_PLATE_AXIS + "2" + "\n").encode())

# def unlock_pressure_plate():
#     motorController.write((ABSOLUTE_MOTION + "\n").encode())
#     motorController.write((MOVE + PRESSURE_PLATE_AXIS + "0" + "\n").encode())


# speed & acc for all axes
def set_gantry_max_speed(mm_per_sec):
    motorController.write((SPEED + GANTRY_X_AXIS + str(mm_per_sec) + "\n").encode())
    motorController.write((SPEED + GANTRY_Y_AXIS + str(mm_per_sec) + "\n").encode())



def set_gantry_acc(acc):
    motorController.write((ACCELERATION + GANTRY_X_AXIS + str(acc) + "\n").encode())
    motorController.write((ACCELERATION + GANTRY_Y_AXIS + str(acc) + "\n").encode())



def set_blade_max_speed(mm_per_sec):
    motorController.write((SPEED + BLADE_AXIS + str(mm_per_sec) + "\n").encode())


def set_blade_acc(acc):
    motorController.write((ACCELERATION + BLADE_AXIS + str(acc) + "\n").encode())


def set_default_speed_and_acceleration():
    set_gantry_max_speed(DEFAULT_GANTRY_SPEED)
    set_gantry_acc(DEFAULT_GANTRY_ACCELERATION)
    set_blade_max_speed(DEFAULT_BLADE_SPEED)
    set_blade_acc(DEFAULT_BLADE_ACCELERATION)


def current_gantry_pos():
    motorController.flush()
    motorController.flushInput()
    motorController.write("M114\n".encode())
    resp = motorController.readline().decode("UTF-8")
    print(resp)

# Dynamixel/Vacuum commands


def change_gripping_angle_to(abs_pos):
    dynamixelController.write((MOVE_GRIPPER + str(abs_pos) + "\n").encode())


def current_gripper_pos():
    dynamixelController.flush()
    dynamixelController.flushInput()
    dynamixelController.write((CURRENT_GRIPPER_POS+"\n").encode())
    resp = dynamixelController.readline().decode("UTF-8")
    resp2 = dynamixelController.readline().decode("UTF-8")
    print(resp2)


def reset_dynamixel():
    dynamixelController.write((RESET_DYNAMIXEL+"\n").encode())
    resp = dynamixelController.readline().decode("UTF-8")
    print(resp)


def max_speed():
    motorController.write((MOVE + "F12000" + "\n"))
