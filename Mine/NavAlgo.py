import time

from typing import Optional, Dict

# from examples.RightWallPID import RightWallPID
from PID import RightWallPID
from simple_airsim.api import coordinate_system
from simple_airsim.api.drone import Drone
from simple_airsim.api.gui_manager import GUIManager
from simple_airsim.api.manager import Manager
from matplotlib import pyplot as plt
import examples.sim_data

sim_time = 0
emergency_threshold = 0.7
front_threshold = 3.0
right_far_threshold = 0.3
tunnel_threshold = 0.2
HEIGHT_Z_AXIS = -2.045
PRECISION = 0.0001

FLIGHT_TIME_MIN = 8
FLIGHT_SPEED = 0.35

drone_points = []
graph = []


def stick_to_right_wall(drone: Drone):
    right_wall_pid = RightWallPID(target=right_far_threshold)

    while True:
        lidars = drone.get_lidars()
        position = drone.get_position()
        orientation = drone.get_orientation()
        velocity = drone.get_velocity()

        right = lidars['right']

        roll_rate = right_wall_pid.compute(right)
        drone.command(roll=roll_rate, pitch=0, yaw_rate=0, z=HEIGHT_Z_AXIS, wait=False)

        if abs(right - right_far_threshold) < PRECISION:
            print(f"Distance from right: {right}\nFinished stick_to_right()")
            break  # Drone can return to main-loop


def tunnel():
    pass

def emergency():
    print("Emergency mode!")
    pass


def return_home():
    print("Returning home")
    pass

def fly_forward(drone: Drone):

    print("Flying forward")



def nav_algo(drone: Drone):
    global drone_points, sim_time, graph
    # Drone's State Machine:
    # 1. Emergency
    # 2. Fix right wall
    # 3. Scan surroundings
    # 4. Move to target point
    # 5. Return home
    battery_low = False

    # Takeoff
    drone.command(0, 0, 0, HEIGHT_Z_AXIS, True)
    # Add starting point to the graph:
    graph.append((drone.get_position()['x'],
                  drone.get_position()['y'],
                  drone.get_position()['z']))
    print(f'Home point: {graph[0]}')
    i = 0
    time_last = 0
    start_time = time.time()
    time_sec_last = 0
    while True:
        lidars = drone.get_lidars()
        position = drone.get_position()
        orientation = drone.get_orientation()
        velocity = drone.get_velocity()

        sim_time = time_last - start_time
        time_sec = int(sim_time)
        if time_sec > time_sec_last:
            if i % 1000 == 0:
                print("Time now: ", float('%.1f' % sim_time))
        if time_sec >= 60 * FLIGHT_TIME_MIN/2:
            battery_low = True
        time_sec_last = time_sec

        if i == 1000000:
            i = 0

        front = lidars['front']
        right = lidars['right']
        left = lidars['left']
        down = lidars['down']
        x = position['x']
        y = position['y']
        z = position['z']

        if front < emergency_threshold:
            emergency()

        elif left < tunnel_threshold and right < tunnel_threshold:
            tunnel()

        elif right > right_far_threshold:
            stick_to_right_wall(drone)  # Loop

        elif battery_low:
            return_home()
            # Handle emergency actions:
        else:
            fly_forward(drone)

        i += 1
        time_last = time.time()


if __name__ == '__main__':
    with Manager(coordinate_system.AIRSIM, method=nav_algo) as man:
        with GUIManager(man, 10, 10, 10, 3) as gui:
            gui.start()
