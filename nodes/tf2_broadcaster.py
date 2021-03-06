#!/usr/bin/env python  

import rospy
import tf_conversions
import tf2_ros
import geometry_msgs.msg
import turtlesim.msg

def handle_pose(msg, robot_name):
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "world"
    t.child_frame_id = robot_name

    rospy.logerr(f'Translation x: {msg.x}')
    t.transform.translation.x = msg.x
    t.transform.translation.y = msg.y
    t.transform.translation.z = 0.0

    q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)

    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]

    br.sendTransform(t)

if __name__ == '__main__':
    rospy.init_node('tf2_broadcaster')
    robot_name = rospy.get_param('~robot_name')
    rospy.Subscriber('%s/pose' % robot_name, turtlesim.msg.Pose, handle_pose, robot_name)
    rospy.spin()
