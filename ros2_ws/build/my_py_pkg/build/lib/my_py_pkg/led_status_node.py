#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import LedStatus
from my_robot_interfaces.srv import SetLed
 
class LEDStatusNode(Node): 
    def __init__(self):
        super().__init__("led_status_node")
        self.declare_parameter("led_states", [0, 0, 0])
        self.led_states = self.get_parameter("led_states").value
        self.led_status_publisher = self.create_publisher(LedStatus, "led_status", 10)
        self.set_led_service = self.create_service(SetLed, "set_led", self.callback_set_led)
        self.led_states_timer = self.create_timer(1, self.publish_led_states)
        self.get_logger().info("LED Status Node has been started")
        
    def publish_led_states(self):
        msg = LedStatus()
        msg.led_states = self.led_states
        self.led_status_publisher.publish(msg)
        
    def callback_set_led(self, request, response):
        led_number = request.led_number
        state = request.state
        
        if led_number <= 0 or led_number >len(self.led_states):
            response.success = False
            response.status_message = "LED number out of range"
            return response
        
        if state != 0 and state != 1:
            response.success = False
            response.status_message = "Invalid state"
            return response
        
        self.led_states[led_number-1] = state
        response.success = True
        response.status_message = "LED state has been set"
        return response
        
def main(args=None):
    rclpy.init(args=args)
    node = LEDStatusNode() 
    rclpy.spin(node)
    rclpy.shutdown()
 
if __name__ == "__main__":
    main()