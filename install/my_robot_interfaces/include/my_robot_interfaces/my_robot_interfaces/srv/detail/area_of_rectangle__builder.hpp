// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_robot_interfaces:srv/AreaOfRectangle.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__SRV__DETAIL__AREA_OF_RECTANGLE__BUILDER_HPP_
#define MY_ROBOT_INTERFACES__SRV__DETAIL__AREA_OF_RECTANGLE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_robot_interfaces/srv/detail/area_of_rectangle__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_AreaOfRectangle_Request_breadth
{
public:
  explicit Init_AreaOfRectangle_Request_breadth(::my_robot_interfaces::srv::AreaOfRectangle_Request & msg)
  : msg_(msg)
  {}
  ::my_robot_interfaces::srv::AreaOfRectangle_Request breadth(::my_robot_interfaces::srv::AreaOfRectangle_Request::_breadth_type arg)
  {
    msg_.breadth = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_interfaces::srv::AreaOfRectangle_Request msg_;
};

class Init_AreaOfRectangle_Request_length
{
public:
  Init_AreaOfRectangle_Request_length()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AreaOfRectangle_Request_breadth length(::my_robot_interfaces::srv::AreaOfRectangle_Request::_length_type arg)
  {
    msg_.length = std::move(arg);
    return Init_AreaOfRectangle_Request_breadth(msg_);
  }

private:
  ::my_robot_interfaces::srv::AreaOfRectangle_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_interfaces::srv::AreaOfRectangle_Request>()
{
  return my_robot_interfaces::srv::builder::Init_AreaOfRectangle_Request_length();
}

}  // namespace my_robot_interfaces


namespace my_robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_AreaOfRectangle_Response_area
{
public:
  Init_AreaOfRectangle_Response_area()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_robot_interfaces::srv::AreaOfRectangle_Response area(::my_robot_interfaces::srv::AreaOfRectangle_Response::_area_type arg)
  {
    msg_.area = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_interfaces::srv::AreaOfRectangle_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_interfaces::srv::AreaOfRectangle_Response>()
{
  return my_robot_interfaces::srv::builder::Init_AreaOfRectangle_Response_area();
}

}  // namespace my_robot_interfaces

#endif  // MY_ROBOT_INTERFACES__SRV__DETAIL__AREA_OF_RECTANGLE__BUILDER_HPP_
