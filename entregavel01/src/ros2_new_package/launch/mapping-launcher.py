import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():
   gazebo_world = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('turtlebot3_gazebo'), 'launch'),
         '/turtlebot3_world.launch.py'])
      )
   cartographer_ros2 = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('turtlebot3_cartographer'), 'launch'),
         '/cartographer.launch.py']),
         launch_arguments={'use_sim_time': 'True'}.items(),
      )

   return LaunchDescription([
      gazebo_world,
      cartographer_ros2,
    #   Node(
    #      package='turtlebot3_teleop',
    #      executable='teleop_keyboard',
    #      name='teleop_turtlebot3',
    #   ),
   ])