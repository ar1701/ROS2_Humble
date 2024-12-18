#!/usr/bin/env python3
import rclpy
import math
import random
from rclpy.node import Node

from functools import partial
from turtlesim.srv import Spawn
 
class TurtleSpawner(Node): 
    def __init__(self):
        super().__init__("turtle_spawner") 
        self.turtle_name_prefix = "turtle"
        self.counter = 1
        self.spawn_turtle_timer = self.create_timer(2.0, self.spawn_new_turtle)  # Corrected line
        
    def spawn_new_turtle(self):
        self.counter += 1
        name = self.turtle_name_prefix + str(self.counter)
        x = random.uniform(0, 11.0)
        y = random.uniform(0, 11.0)
        theta = random.uniform(0, 2*math.pi)
        self.call_spawn_server(name, x, y, theta)
        
    def call_spawn_server(self, turtle_name, x, y, theta):
        client = self.create_client(Spawn, "spawn")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for server spawn...")
        request = Spawn.Request()
        request.x = x
        request.y = y
        request.theta = theta
        request.name = turtle_name
        future = client.call_async(request)
        future.add_done_callback(
            partial(self.callback_call_spawn, turtle_name=turtle_name, x=x, y=y, theta=theta)
        )
        
    def callback_call_spawn(self, future, turtle_name, x, y, theta):    
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().error(f"Service call failed {e}")
        else:
            self.get_logger().info(f"Spawned turtle {turtle_name}")
 
def main(args=None):
    rclpy.init(args=args)
    node = TurtleSpawner() 
    rclpy.spin(node)
    rclpy.shutdown()
 
if __name__ == "__main__":
    main()