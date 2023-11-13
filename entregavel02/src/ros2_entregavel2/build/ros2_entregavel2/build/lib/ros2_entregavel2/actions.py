import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped
from tf_transformations import quaternion_from_euler
from math import pi

point_dict = {
        "ponto 1": [2.0, 2.0, 1.0]
        }

def pose(pose_x, pose_y, pose_z):
    rclpy.init()
    nav = BasicNavigator()
    q_x, q_y, q_z, q_w = quaternion_from_euler(0.0, 0.0, pi/4)
    goal_pose = PoseStamped()
    goal_pose.header.frame_id = 'map'
    goal_pose.header.stamp = nav.get_clock().now().to_msg()
    goal_pose.pose.position.x = pose_x
    goal_pose.pose.position.y = pose_y
    goal_pose.pose.position.z = pose_z
    goal_pose.pose.orientation.x = q_x
    goal_pose.pose.orientation.y = q_y
    goal_pose.pose.orientation.z = q_z
    goal_pose.pose.orientation.w = q_w

    nav.waitUntilNav2Active()
    nav.goToPose(goal_pose)
    while not nav.isTaskComplete():
        print(nav.getFeedback())

    rclpy.shutdown()

def go_to(point):
    if point in point_dict:
        print(f"Indo para '{point}': {point_dict[point]}")
        pose(point_dict[point][0], point_dict[point][1], point_dict[point][2])
    else:
        print("Esse ponto não está cadastrado: {point}")