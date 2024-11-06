#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from functools import partial
from my_robot_interfaces.srv import SetLed

class BatteryNode(Node): 
    def __init__(self):
        super().__init__("battery_state")
        self.battery_state = "full"
        self.last_time_battery_state_changed = self.get_current_time_seconds()
        self.battery_timer = self.create_timer(0.1, self.check_battery_state)
        self.get_logger().info("Battery Node has been started")
    
    def get_current_time_seconds(self):
        secs, nsecs = self.get_clock().now().seconds_nanoseconds()
        return secs + nsecs / 1000000000.0
    
    def check_battery_state(self):
        time_now = self.get_current_time_seconds()
        if self.battery_state == "full":
            if time_now - self.last_time_battery_state_changed > 4.0:
                self.battery_state = "empty"
                self.get_logger().info("Battery is empty! Charging Battery")
                self.last_time_battery_state_changed = time_now    
                self.call_set_led_server(3, 1)
                
        elif self.battery_state == "empty":
            if time_now - self.last_time_battery_state_changed > 6.0:
                self.battery_state = "full"
                self.get_logger().info("Battery is full again!")
                self.last_time_battery_state_changed = time_now
                self.call_set_led_server(3, 0)
        
    def call_set_led_server(self, led_number, state):
        client = self.create_client(SetLed, "set_led")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server Set LED...")

        request = SetLed.Request()
        request.led_number = led_number
        request.state = state

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_call_set_led, led_number=led_number, state=state))

    def callback_call_set_led(self, future, led_number, state):
        try:
            response = future.result()
            self.get_logger().info(f"Set LED {led_number} to {'ON' if state == 1 else 'OFF'}: {response.success}")
        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = BatteryNode()  
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()