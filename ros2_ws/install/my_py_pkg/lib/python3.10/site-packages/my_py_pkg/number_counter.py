#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64
 
 
class NumberCounter(Node): 
    def __init__(self):
        super().__init__("node_name") 
        self.declare_parameter("number_to_publish")
        
        self.number = self.get_parameter("number_to_publish").value
        self.number_publisher = self.create_publisher(Int64, "number", 10)
        self.create_timer(1, self.publish_number)
        self.get_logger().info("Number Counter has been started")
        
    def publish_number(self):
        msg = Int64()
        msg.data = self.number
        self.number_publisher.publish(msg)
        self.number += 1
        
 
 
def main(args=None):
    rclpy.init(args=args)
    node = NumberCounter() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
