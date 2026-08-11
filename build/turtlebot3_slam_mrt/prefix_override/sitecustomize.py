import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ram/MRT/turtle/install/turtlebot3_slam_mrt'
