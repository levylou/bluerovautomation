; Auto-generated. Do not edit!


(cl:in-package freefloating_gazebo-srv)


;//! \htmlinclude ControlType-request.msg.html

(cl:defclass <ControlType-request> (roslisp-msg-protocol:ros-message)
  ((axes
    :reader axes
    :initarg :axes
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element "")))
)

(cl:defclass ControlType-request (<ControlType-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ControlType-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ControlType-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name freefloating_gazebo-srv:<ControlType-request> is deprecated: use freefloating_gazebo-srv:ControlType-request instead.")))

(cl:ensure-generic-function 'axes-val :lambda-list '(m))
(cl:defmethod axes-val ((m <ControlType-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader freefloating_gazebo-srv:axes-val is deprecated.  Use freefloating_gazebo-srv:axes instead.")
  (axes m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ControlType-request>) ostream)
  "Serializes a message object of type '<ControlType-request>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'axes))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((__ros_str_len (cl:length ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) ele))
   (cl:slot-value msg 'axes))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ControlType-request>) istream)
  "Deserializes a message object of type '<ControlType-request>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'axes) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'axes)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:aref vals i) __ros_str_idx) (cl:code-char (cl:read-byte istream))))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ControlType-request>)))
  "Returns string type for a service object of type '<ControlType-request>"
  "freefloating_gazebo/ControlTypeRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ControlType-request)))
  "Returns string type for a service object of type 'ControlType-request"
  "freefloating_gazebo/ControlTypeRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ControlType-request>)))
  "Returns md5sum for a message object of type '<ControlType-request>"
  "52951d9d51995d256d1f3d1a265444f8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ControlType-request)))
  "Returns md5sum for a message object of type 'ControlType-request"
  "52951d9d51995d256d1f3d1a265444f8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ControlType-request>)))
  "Returns full string definition for message of type '<ControlType-request>"
  (cl:format cl:nil "~%string[] axes~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ControlType-request)))
  "Returns full string definition for message of type 'ControlType-request"
  (cl:format cl:nil "~%string[] axes~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ControlType-request>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'axes) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ControlType-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ControlType-request
    (cl:cons ':axes (axes msg))
))
;//! \htmlinclude ControlType-response.msg.html

(cl:defclass <ControlType-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass ControlType-response (<ControlType-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ControlType-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ControlType-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name freefloating_gazebo-srv:<ControlType-response> is deprecated: use freefloating_gazebo-srv:ControlType-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ControlType-response>) ostream)
  "Serializes a message object of type '<ControlType-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ControlType-response>) istream)
  "Deserializes a message object of type '<ControlType-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ControlType-response>)))
  "Returns string type for a service object of type '<ControlType-response>"
  "freefloating_gazebo/ControlTypeResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ControlType-response)))
  "Returns string type for a service object of type 'ControlType-response"
  "freefloating_gazebo/ControlTypeResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ControlType-response>)))
  "Returns md5sum for a message object of type '<ControlType-response>"
  "52951d9d51995d256d1f3d1a265444f8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ControlType-response)))
  "Returns md5sum for a message object of type 'ControlType-response"
  "52951d9d51995d256d1f3d1a265444f8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ControlType-response>)))
  "Returns full string definition for message of type '<ControlType-response>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ControlType-response)))
  "Returns full string definition for message of type 'ControlType-response"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ControlType-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ControlType-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ControlType-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ControlType)))
  'ControlType-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ControlType)))
  'ControlType-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ControlType)))
  "Returns string type for a service object of type '<ControlType>"
  "freefloating_gazebo/ControlType")