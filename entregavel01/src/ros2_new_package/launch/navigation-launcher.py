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
#    navigator_ros2 = IncludeLaunchDescription(
#       PythonLaunchDescriptionSource([os.path.join(
#          get_package_share_directory('turtlebot3_navigation2'), 'launch'),
#          '/navigation2.launch.py']),
#          launch_arguments={'use_sim_time': 'True', 
#                            'map': '~/Documents/GitHub/Module8-exercises/entregavel01/src/ros2_new_package/launch/my-map.yaml'}.items(),
#          )
   navigator_ros2 = ExecuteProcess(
            cmd=['gnome-terminal', '--', 'ros2', 'launch', 'turtlebot3_navigation2', 'navigation2.launch.py', 'use_sim_time:=True', 'map:=my-map.yaml'],
            output='screen'
        )

   return LaunchDescription([
      gazebo_world,
      navigator_ros2,
   ])