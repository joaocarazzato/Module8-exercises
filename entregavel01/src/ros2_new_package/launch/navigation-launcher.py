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
   navigator_ros2 = ExecuteProcess(
            cmd=['ros2', 'launch', 'turtlebot3_navigation2', 'navigation2.launch.py', 'use_sim_time:=True', 'map:=my-map.yaml'],
            name='navigator_ros2',
            output='screen'
        )
   initial_pose = ExecuteProcess(
      cmd=['gnome-terminal', '--', 'python3', '../set_initial_pose_nav2.py'],
      name='initial_pos_mapper',
      output='screen'
   )

   return LaunchDescription([
      gazebo_world,
      navigator_ros2,
      initial_pose,
   ])