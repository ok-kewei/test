// Generated by gencpp from file husky_highlevel_controller/RadianToAngle.msg
// DO NOT EDIT!


#ifndef HUSKY_HIGHLEVEL_CONTROLLER_MESSAGE_RADIANTOANGLE_H
#define HUSKY_HIGHLEVEL_CONTROLLER_MESSAGE_RADIANTOANGLE_H

#include <ros/service_traits.h>


#include <husky_highlevel_controller/RadianToAngleRequest.h>
#include <husky_highlevel_controller/RadianToAngleResponse.h>


namespace husky_highlevel_controller
{

struct RadianToAngle
{

typedef RadianToAngleRequest Request;
typedef RadianToAngleResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct RadianToAngle
} // namespace husky_highlevel_controller


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::husky_highlevel_controller::RadianToAngle > {
  static const char* value()
  {
    return "8dd47fc5494973709ed579a85c77ce44";
  }

  static const char* value(const ::husky_highlevel_controller::RadianToAngle&) { return value(); }
};

template<>
struct DataType< ::husky_highlevel_controller::RadianToAngle > {
  static const char* value()
  {
    return "husky_highlevel_controller/RadianToAngle";
  }

  static const char* value(const ::husky_highlevel_controller::RadianToAngle&) { return value(); }
};


// service_traits::MD5Sum< ::husky_highlevel_controller::RadianToAngleRequest> should match
// service_traits::MD5Sum< ::husky_highlevel_controller::RadianToAngle >
template<>
struct MD5Sum< ::husky_highlevel_controller::RadianToAngleRequest>
{
  static const char* value()
  {
    return MD5Sum< ::husky_highlevel_controller::RadianToAngle >::value();
  }
  static const char* value(const ::husky_highlevel_controller::RadianToAngleRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::husky_highlevel_controller::RadianToAngleRequest> should match
// service_traits::DataType< ::husky_highlevel_controller::RadianToAngle >
template<>
struct DataType< ::husky_highlevel_controller::RadianToAngleRequest>
{
  static const char* value()
  {
    return DataType< ::husky_highlevel_controller::RadianToAngle >::value();
  }
  static const char* value(const ::husky_highlevel_controller::RadianToAngleRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::husky_highlevel_controller::RadianToAngleResponse> should match
// service_traits::MD5Sum< ::husky_highlevel_controller::RadianToAngle >
template<>
struct MD5Sum< ::husky_highlevel_controller::RadianToAngleResponse>
{
  static const char* value()
  {
    return MD5Sum< ::husky_highlevel_controller::RadianToAngle >::value();
  }
  static const char* value(const ::husky_highlevel_controller::RadianToAngleResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::husky_highlevel_controller::RadianToAngleResponse> should match
// service_traits::DataType< ::husky_highlevel_controller::RadianToAngle >
template<>
struct DataType< ::husky_highlevel_controller::RadianToAngleResponse>
{
  static const char* value()
  {
    return DataType< ::husky_highlevel_controller::RadianToAngle >::value();
  }
  static const char* value(const ::husky_highlevel_controller::RadianToAngleResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // HUSKY_HIGHLEVEL_CONTROLLER_MESSAGE_RADIANTOANGLE_H
