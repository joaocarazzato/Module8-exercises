from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch.actions import ExecuteProcess

def generate_launch_description():

    map_saver = ExecuteProcess(
            cmd=['ros2', 'run', 'nav2_map_server', 'map_saver_cli', '-f', 'my-map'],
            output='screen'
        )

    return LaunchDescription([
        map_saver,
        ])

if __name__ == "__main__":
   generate_launch_description()