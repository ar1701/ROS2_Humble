#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class SmartphoneNode : public rclcpp::Node
{
public:
    SmartphoneNode() : Node("robot_news_subscriber")
    {
        // Create a subscription to the "robot_news" topic
        subscription_ = this->create_subscription<example_interfaces::msg::String>(
            "robot_news", 10, std::bind(&SmartphoneNode::callback_news, this, std::placeholders::_1));

        RCLCPP_INFO(this->get_logger(), "Robot News Subscriber has been started");
    }

private:
    void callback_news(const example_interfaces::msg::String::SharedPtr msg) const
    {
        // Log the received message
        RCLCPP_INFO(this->get_logger(), "Received: '%s'", msg->data.c_str());
    }

    rclcpp::Subscription<example_interfaces::msg::String>::SharedPtr subscription_;
};

int main(int argc, char *argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<SmartphoneNode>());
    rclcpp::shutdown();
    return 0;
}
