// Generated by gencpp from file husky_highlevel_controller/MulTwoInts.msg
// DO NOT EDIT!


#ifndef HUSKY_HIGHLEVEL_CONTROLLER_MESSAGE_MULTWOINTS_H
#define HUSKY_HIGHLEVEL_CONTROLLER_MESSAGE_MULTWOINTS_H

#include <ros/service_traits.h>


#include <husky_highlevel_controller/MulTwoIntsRequest.h>
#include <husky_highlevel_controller/MulTwoIntsResponse.h>


namespace husky_highlevel_controller
{

struct MulTwoInts
{

typedef MulTwoIntsRequest Request;
typedef MulTwoIntsResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct MulTwoInts
} // namespace husky_highlevel_controller


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::husky_highlevel_controller::MulTwoInts > {
  static const char* value()
  {
    return "94ad1411057ad93d39d73409d0884011";
  }

  static const char* value(const ::husky_highlevel_controller::MulTwoInts&) { return value(); }
};

template<>
struct DataType< ::husky_highlevel_controller::MulTwoInts > {
  static const char* value()
  {
    return "husky_highlevel_controller/MulTwoInts";
  }

  static const char* value(const ::husky_highlevel_controller::MulTwoInts&) { return value(); }
};


// service_traits::MD5Sum< ::husky_highlevel_controller::MulTwoIntsRequest> should match
// service_traits::MD5Sum< ::husky_highlevel_controller::MulTwoInts >
template<>
struct MD5Sum< ::husky_highlevel_controller::MulTwoIntsRequest>
{
  static const char* value()
  {
    return MD5Sum< ::husky_highlevel_controller::MulTwoInts >::value();
  }
  static const char* value(const ::husky_highlevel_controller::MulTwoIntsRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::husky_highlevel_controller::MulTwoIntsRequest> should match
// service_traits::DataType< ::husky_highlevel_controller::MulTwoInts >
template<>
struct DataType< ::husky_highlevel_controller::MulTwoIntsRequest>
{
  static const char* value()
  {
    return DataType< ::husky_highlevel_controller::MulTwoInts >::value();
  }
  static const char* value(const ::husky_highlevel_controller::MulTwoIntsRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::husky_highlevel_controller::MulTwoIntsResponse> should match
// service_traits::MD5Sum< ::husky_highlevel_controller::MulTwoInts >
template<>
struct MD5Sum< ::husky_highlevel_controller::MulTwoIntsResponse>
{
  static const char* value()
  {
    return MD5Sum< ::husky_highlevel_controller::MulTwoInts >::value();
  }
  static const char* value(const ::husky_highlevel_controller::MulTwoIntsResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::husky_highlevel_controller::MulTwoIntsResponse> should match
// service_traits::DataType< ::husky_highlevel_controller::MulTwoInts >
template<>
struct DataType< ::husky_highlevel_controller::MulTwoIntsResponse>
{
  static const char* value()
  {
    return DataType< ::husky_highlevel_controller::MulTwoInts >::value();
  }
  static const char* value(const ::husky_highlevel_controller::MulTwoIntsResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // HUSKY_HIGHLEVEL_CONTROLLER_MESSAGE_MULTWOINTS_H
