from utils import generate_map_random
from robot import Robot
from position import Position
from sweeper_bfs import SweeperBFS
from sweeper_dfs import SweeperDFS
from utils import print_progress_matrix

def main():
    
    maps, observed_map = generate_map_random(100,100,1000)
    
    start_position = Position(0, 0)
    robot = Robot(maps, start_position, 0)
    sweeper = SweeperBFS(robot, observed_map)
    #sweeper = SweeperDFS(robot, maps)
    sweeper.work()
    
    print('Robot result. Step number:', robot.step_number, 'Turn number:', robot.turn_number)


if __name__ == "__main__":
    main()
