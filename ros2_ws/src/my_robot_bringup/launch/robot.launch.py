from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()
    
    news_publisher_node1 = Node(
        package="my_py_pkg",
        executable="robot_news_station",
        name="robot_news_node_1",
        parameters=[
            {"robot_name": "heroku 1"},
        ]
    ) 
    
    news_publisher_node2 = Node(
        package="my_py_pkg",
        executable="robot_news_station",
        name="robot_news_node_2",
        parameters=[
            {"robot_name": "heroku 2"},
        ]
    ) 
      
    news_publisher_node3 = Node(
        package="my_py_pkg",
        executable="robot_news_station",
        name="robot_news_node_3",
        parameters=[
            {"robot_name": "heroku 3"},
        ]
    ) 
      
    news_publisher_node4 = Node(
        package="my_py_pkg",
        executable="robot_news_station",
        name="robot_news_node_4",
        parameters=[
            {"robot_name": "heroku 4"},
        ]
    ) 
      
    news_publisher_node5 = Node(
        package="my_py_pkg",
        executable="robot_news_station",
        name="robot_news_node_5",
        parameters=[
            {"robot_name": "heroku 5"},
        ]
    ) 
    
    
    ld.add_action(news_publisher_node1)
    ld.add_action(news_publisher_node2)
    ld.add_action(news_publisher_node3)
    ld.add_action(news_publisher_node4)
    ld.add_action(news_publisher_node5)
    return ld