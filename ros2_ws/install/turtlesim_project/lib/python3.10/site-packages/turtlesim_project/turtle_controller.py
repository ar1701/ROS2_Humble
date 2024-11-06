#!/usr/bin/env python3
import math
import rclpy
from rclpy.node import Node

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

 
 
class TurtleController(Node): 
    def __init__(self):
        super().__init__("turtle_controller") 
        self.pose = None
        self.target_x = 9.0
        self.target_y = 6.0
        self.cmd_vel_publisher = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.pose_subsciber = self.create_subscription(Pose, "turtle1/pose", self.pose_callback, 10)
        self.control_loop_timer = self.create_timer(0.01, self.control_loop)
        
    def pose_callback(self, msg):
            self.pose = msg
           
        
    def control_loop(self):
            if self.pose == None:
                return 
            
            dist_x = self.target_x - self.pose.x
            dist_y = self.target_y - self.pose.y
            distance = ((dist_x ** 2) + (dist_y ** 2)) ** 0.5
            
            msg = Twist()
            
            if distance > 0.5:
                msg.linear.x = 2*distance
                
                goal_theta = math.atan2(dist_y, dist_x)
                diff = goal_theta - self.pose.theta
                if diff > math.pi:
                    diff -= 2 * math.pi
                elif diff < -math.pi:
                    diff += 2 * math.pi
                    
                msg.angular.z = 6 * diff
                
                
            else:
                msg.linear.x = 0.0
                msg.linear.y = 0.0
                self.get_logger().info("Target reached")
            
            self.cmd_vel_publisher.publish(msg)
 
 
def main(args=None):
    rclpy.init(args=args)
    node = TurtleController() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
