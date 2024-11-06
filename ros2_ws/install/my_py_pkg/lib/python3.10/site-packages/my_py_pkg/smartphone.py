#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


class SmartphoneNode(Node):
    def __init__(self):
        super().__init__("smartphone")
        
        # Create a subscriber that listens to the 'robot_news' topic
        self.subscriber_ = self.create_subscription(
            String, "robot_news", self.callback_news, 10)
        
        self.get_logger().info("Smartphone has been started")

    def callback_news(self, msg):
        # This is called every time a message is received
        self.get_logger().info(f"Received: {msg.data}")
        

def main(args=None):
    rclpy.init(args=args)
    node = SmartphoneNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
