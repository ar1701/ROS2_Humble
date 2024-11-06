#include "rclcpp/rclcpp.hpp"
#include <chrono>

using namespace std::chrono_literals;

class HelloWorldNode : public rclcpp::Node
{
public:
    HelloWorldNode() : Node("cpp_test"), count_(1)
    {
        // Create a timer that triggers every second (1000ms)
        timer_ = this->create_wall_timer(1000ms, std::bind(&HelloWorldNode::on_timer, this));
    }

private:
    void on_timer()
    {
        // Print "Hello World" with the incrementing count
        RCLCPP_INFO(this->get_logger(), "Hello World %d", count_);
        count_++;
    }

    rclcpp::TimerBase::SharedPtr timer_;
    int count_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);

    // Create the node
    auto node = std::make_shared<HelloWorldNode>();

    // Spin the node (to keep it running and responding to timers)
    rclcpp::spin(node);

    rclcpp::shutdown();
    return 0;
}
