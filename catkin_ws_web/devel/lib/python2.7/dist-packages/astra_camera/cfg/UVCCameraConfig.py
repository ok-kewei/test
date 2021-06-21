## *********************************************************
##
## File autogenerated for the libuvc_camera package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 246, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 291, 'description': 'Vendor ID, hex digits (use camera of any vendor if null).', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'vendor', 'edit_method': '', 'default': '', 'level': 3, 'min': '', 'type': 'str'}, {'srcline': 291, 'description': 'Product ID, hex digits (use camera of any model if null).', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'product', 'edit_method': '', 'default': '', 'level': 3, 'min': '', 'type': 'str'}, {'srcline': 291, 'description': 'Serial number, arbitrary string (use camera of any serial number if null).', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'serial', 'edit_method': '', 'default': '', 'level': 3, 'min': '', 'type': 'str'}, {'srcline': 291, 'description': 'Index into the list of cameras that match the above parameters.', 'max': 2147483647, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'index', 'edit_method': '', 'default': 0, 'level': 3, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'Image width.', 'max': 2147483647, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'width', 'edit_method': '', 'default': 640, 'level': 3, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'Image height.', 'max': 2147483647, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'height', 'edit_method': '', 'default': 480, 'level': 3, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'Format of video stream from camera.', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'video_mode', 'edit_method': "{'enum_description': 'Video stream format', 'enum': [{'srcline': 36, 'description': 'Use any uncompressed format', 'srcfile': '/home/kewei/catkin_ws_web/src/ros_astra_camera/cfg/UVCCamera.cfg', 'cconsttype': 'const char * const', 'value': 'uncompressed', 'ctype': 'std::string', 'type': 'str', 'name': 'uncompressed'}, {'srcline': 37, 'description': 'User any compressed format', 'srcfile': '/home/kewei/catkin_ws_web/src/ros_astra_camera/cfg/UVCCamera.cfg', 'cconsttype': 'const char * const', 'value': 'compressed', 'ctype': 'std::string', 'type': 'str', 'name': 'compressed'}, {'srcline': 38, 'description': 'YUYV', 'srcfile': '/home/kewei/catkin_ws_web/src/ros_astra_camera/cfg/UVCCamera.cfg', 'cconsttype': 'const char * const', 'value': 'yuyv', 'ctype': 'std::string', 'type': 'str', 'name': 'yuyv'}, {'srcline': 39, 'description': 'UYVY', 'srcfile': '/home/kewei/catkin_ws_web/src/ros_astra_camera/cfg/UVCCamera.cfg', 'cconsttype': 'const char * const', 'value': 'uyvy', 'ctype': 'std::string', 'type': 'str', 'name': 'uyvy'}, {'srcline': 40, 'description': 'RGB', 'srcfile': '/home/kewei/catkin_ws_web/src/ros_astra_camera/cfg/UVCCamera.cfg', 'cconsttype': 'const char * const', 'value': 'rgb', 'ctype': 'std::string', 'type': 'str', 'name': 'rgb'}, {'srcline': 41, 'description': 'BGR', 'srcfile': '/home/kewei/catkin_ws_web/src/ros_astra_camera/cfg/UVCCamera.cfg', 'cconsttype': 'const char * const', 'value': 'bgr', 'ctype': 'std::string', 'type': 'str', 'name': 'bgr'}, {'srcline': 42, 'description': 'MJPEG', 'srcfile': '/home/kewei/catkin_ws_web/src/ros_astra_camera/cfg/UVCCamera.cfg', 'cconsttype': 'const char * const', 'value': 'mjpeg', 'ctype': 'std::string', 'type': 'str', 'name': 'mjpeg'}, {'srcline': 43, 'description': 'gray8', 'srcfile': '/home/kewei/catkin_ws_web/src/ros_astra_camera/cfg/UVCCamera.cfg', 'cconsttype': 'const char * const', 'value': 'gray8', 'ctype': 'std::string', 'type': 'str', 'name': 'gray8'}]}", 'default': 'uncompressed', 'level': 3, 'min': '', 'type': 'str'}, {'srcline': 291, 'description': 'Camera speed, frames per second.', 'max': 1000.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'frame_rate', 'edit_method': '', 'default': 15.0, 'level': 3, 'min': 0.1, 'type': 'double'}, {'srcline': 291, 'description': 'Method for determining the timestamp.', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'timestamp_method', 'edit_method': "{'enum_description': 'Methods for determining the timestamp', 'enum': [{'srcline': 53, 'description': 'Time of publication', 'srcfile': '/home/kewei/catkin_ws_web/src/ros_astra_camera/cfg/UVCCamera.cfg', 'cconsttype': 'const char * const', 'value': 'pub', 'ctype': 'std::string', 'type': 'str', 'name': 'PubTime'}, {'srcline': 54, 'description': 'Time when raw frame capture began', 'srcfile': '/home/kewei/catkin_ws_web/src/ros_astra_camera/cfg/UVCCamera.cfg', 'cconsttype': 'const char * const', 'value': 'start', 'ctype': 'std::string', 'type': 'str', 'name': 'FrameStartTime'}, {'srcline': 55, 'description': 'Time when raw frame capture ended', 'srcfile': '/home/kewei/catkin_ws_web/src/ros_astra_camera/cfg/UVCCamera.cfg', 'cconsttype': 'const char * const', 'value': 'stop', 'ctype': 'std::string', 'type': 'str', 'name': 'FrameStopTime'}, {'srcline': 56, 'description': 'Time when camera-to-host transfer completed', 'srcfile': '/home/kewei/catkin_ws_web/src/ros_astra_camera/cfg/UVCCamera.cfg', 'cconsttype': 'const char * const', 'value': 'hostrcpt', 'ctype': 'std::string', 'type': 'str', 'name': 'HostReceiptTime'}]}", 'default': 'start', 'level': 3, 'min': '', 'type': 'str'}, {'srcline': 291, 'description': 'ROS tf frame of reference, resolved with tf_prefix unless absolute.', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'frame_id', 'edit_method': '', 'default': 'camera', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 291, 'description': 'Path to camera calibration file.', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'camera_info_url', 'edit_method': '', 'default': '', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 291, 'description': 'Scanning mode.', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'scanning_mode', 'edit_method': "{'enum_description': 'Scanning modes', 'enum': [{'srcline': 72, 'description': '', 'srcfile': '/home/kewei/catkin_ws_web/src/ros_astra_camera/cfg/UVCCamera.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'Interlaced'}, {'srcline': 73, 'description': '', 'srcfile': '/home/kewei/catkin_ws_web/src/ros_astra_camera/cfg/UVCCamera.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'Progressive'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'Auto exposure mode.', 'max': 3, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'auto_exposure', 'edit_method': "{'enum_description': 'Auto-exposure modes', 'enum': [{'srcline': 80, 'description': 'Manual exposure, manual iris', 'srcfile': '/home/kewei/catkin_ws_web/src/ros_astra_camera/cfg/UVCCamera.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'Manual'}, {'srcline': 81, 'description': 'Auto exposure, auto iris', 'srcfile': '/home/kewei/catkin_ws_web/src/ros_astra_camera/cfg/UVCCamera.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'Auto'}, {'srcline': 82, 'description': 'manual exposure, auto iris', 'srcfile': '/home/kewei/catkin_ws_web/src/ros_astra_camera/cfg/UVCCamera.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'Shutter_Priority'}, {'srcline': 83, 'description': 'auto exposure, manual iris', 'srcfile': '/home/kewei/catkin_ws_web/src/ros_astra_camera/cfg/UVCCamera.cfg', 'cconsttype': 'const int', 'value': 3, 'ctype': 'int', 'type': 'int', 'name': 'Aperture_Priority'}]}", 'default': 3, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'In auto mode or shutter priority mode, allow the device to vary frame rate.', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'auto_exposure_priority', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'Length of exposure, seconds.', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'exposure_absolute', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': 0.0001, 'type': 'double'}, {'srcline': 291, 'description': 'Aperture, f.', 'max': 655.35, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'iris_absolute', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'Maintain focus automatically.', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'auto_focus', 'edit_method': '', 'default': True, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 291, 'description': 'Absolute focal distance, millimeters.', 'max': 65536, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'focus_absolute', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'Pan (clockwise), arc seconds.', 'max': 648000, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'pan_absolute', 'edit_method': '', 'default': 0, 'level': 0, 'min': -648000, 'type': 'int'}, {'srcline': 291, 'description': 'Tilt (up), arc seconds.', 'max': 648000, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'tilt_absolute', 'edit_method': '', 'default': 0, 'level': 0, 'min': -648000, 'type': 'int'}, {'srcline': 291, 'description': 'Roll (clockwise), degrees.', 'max': 180, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'roll_absolute', 'edit_method': '', 'default': 0, 'level': 0, 'min': -180, 'type': 'int'}, {'srcline': 291, 'description': 'Image capture disabled.', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'privacy', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 291, 'description': 'Backlight compensation, device-dependent (zero for none, increasing compensation above zero).', 'max': 65536, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'backlight_compensation', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'Brightness, device dependent.', 'max': 32767, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'brightness', 'edit_method': '', 'default': 0, 'level': 0, 'min': -32768, 'type': 'int'}, {'srcline': 291, 'description': 'Contrast, device dependent.', 'max': 32767, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'contrast', 'edit_method': '', 'default': 0, 'level': 0, 'min': -32768, 'type': 'int'}, {'srcline': 291, 'description': 'Gain, device dependent.', 'max': 65536, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'gain', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'Power line frequency anti-flicker processing.', 'max': 2, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'power_line_frequency', 'edit_method': "{'enum_description': 'Power line frequency modes', 'enum': [{'srcline': 146, 'description': 'Disabled', 'srcfile': '/home/kewei/catkin_ws_web/src/ros_astra_camera/cfg/UVCCamera.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'Disabled'}, {'srcline': 147, 'description': '50 Hz', 'srcfile': '/home/kewei/catkin_ws_web/src/ros_astra_camera/cfg/UVCCamera.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'Freq_50'}, {'srcline': 148, 'description': '60 Hz', 'srcfile': '/home/kewei/catkin_ws_web/src/ros_astra_camera/cfg/UVCCamera.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'Freq_60'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'Automatic hue control.', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'auto_hue', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 291, 'description': 'Hue, degrees.', 'max': 180.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'hue', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -180.0, 'type': 'double'}, {'srcline': 291, 'description': 'Saturation, device dependent (zero for grayscale).', 'max': 65536, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'saturation', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'Image sharpness, device dependent.', 'max': 65536, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'sharpness', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'Gamma.', 'max': 5.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'gamma', 'edit_method': '', 'default': 1.0, 'level': 0, 'min': 0.01, 'type': 'double'}, {'srcline': 291, 'description': 'Automatic white balance.', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'auto_white_balance', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 291, 'description': 'White balance temperature, degrees.', 'max': 65536, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'white_balance_temperature', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'Blue or U component of white balance, device-dependent.', 'max': 65536.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'white_balance_BU', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'Red or V component of white balance, device-dependent.', 'max': 65536.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'white_balance_RV', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': 0.0, 'type': 'double'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

UVCCamera_uncompressed = 'uncompressed'
UVCCamera_compressed = 'compressed'
UVCCamera_yuyv = 'yuyv'
UVCCamera_uyvy = 'uyvy'
UVCCamera_rgb = 'rgb'
UVCCamera_bgr = 'bgr'
UVCCamera_mjpeg = 'mjpeg'
UVCCamera_gray8 = 'gray8'
UVCCamera_PubTime = 'pub'
UVCCamera_FrameStartTime = 'start'
UVCCamera_FrameStopTime = 'stop'
UVCCamera_HostReceiptTime = 'hostrcpt'
UVCCamera_Interlaced = 0
UVCCamera_Progressive = 1
UVCCamera_Manual = 0
UVCCamera_Auto = 1
UVCCamera_Shutter_Priority = 2
UVCCamera_Aperture_Priority = 3
UVCCamera_Disabled = 0
UVCCamera_Freq_50 = 1
UVCCamera_Freq_60 = 1
