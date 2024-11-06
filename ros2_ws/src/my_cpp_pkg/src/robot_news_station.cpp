#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class RobotNewsStationNode : public rclcpp::Node
{
public:
    RobotNewsStationNode() : Node("robot_news_station"), count_(0)
    {
        // Create a publisher that publishes messages on the "robot_news" topic
        publisher_ = this->create_publisher<example_interfaces::msg::String>("robot_news", 10);

        // Create a timer that triggers every second
        timer_ = this->create_wall_timer(
            std::chrono::seconds(1), std::bind(&RobotNewsStationNode::publish_news, this));

        RCLCPP_INFO(this->get_logger(), "Robot News Station has been started");
    }

private:
    void publish_news()
    {
        auto message = example_interfaces::msg::String();
        message.data = "Hello Robo " + std::to_string(count_++);
        publisher_->publish(message);

        RCLCPP_INFO(this->get_logger(), "Published: '%s'", message.data.c_str());
    }

    rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
    int count_;
};

int main(int argc, char *argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<RobotNewsStationNode>());
    rclcpp::shutdown();
    return 0;
}
