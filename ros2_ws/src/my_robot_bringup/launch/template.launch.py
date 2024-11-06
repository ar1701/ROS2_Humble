from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()
    
    number_publisher_node = Node(
        package="package_name",
        executable="executable_name",
        name="rename_node_name",
        remappings=[
            ("old_topic_name", "new_topic_name"),
            ("old_service_name", "new_service_name"),
        ],
        parameters=[
            {"parameter_name": "parameter_value"},
        ]
    ) 
    
    
    ld.add_action(number_publisher_node)
    return ld