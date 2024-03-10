#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

#my_first_node is the filename where you gonna write the codes
class MyNode(Node):
    
    def __init__(self):
        #first_node is node name inside ros functionality
        #[INFO] [1709998193.385038224] [first_node]: Hello from ROS2
        super().__init__("first_node")
        # self.get_logger().info("ROS")
        self.counter_ = 0
        self.create_timer(1.0, self.timer_callback)
        
    def timer_callback(self):
        self.get_logger().info("Hello " + str(self.counter_))
        self.counter_ += 1

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    #keep the node open
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    
    
# colcon build --symlink-install : not need to build everytime when code changed