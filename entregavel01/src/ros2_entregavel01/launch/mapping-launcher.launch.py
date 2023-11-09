import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
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
   teleop_turtlebot3 = ExecuteProcess(
            condition=IfCondition(LaunchConfiguration('use_gnome_terminal')),
            cmd=['gnome-terminal', '--', 'ros2', 'run', 'turtlebot3_teleop', 'teleop_keyboard'],
            output='screen'
        )

   return LaunchDescription([
      gazebo_world,
      cartographer_ros2,
      DeclareLaunchArgument(
            'use_gnome_terminal',
            default_value='true',
            description='Use gnome_terminal to open a new terminal for the node'
        ),
      teleop_turtlebot3,
   ])

if __name__ == "__main__":
   generate_launch_description()