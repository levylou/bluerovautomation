;; Auto-generated. Do not edit!


(when (boundp 'bluerov_ros_playground::Custom)
  (if (not (find-package "BLUEROV_ROS_PLAYGROUND"))
    (make-package "BLUEROV_ROS_PLAYGROUND"))
  (shadow 'Custom (find-package "BLUEROV_ROS_PLAYGROUND")))
(unless (find-package "BLUEROV_ROS_PLAYGROUND::CUSTOM")
  (make-package "BLUEROV_ROS_PLAYGROUND::CUSTOM"))

(in-package "ROS")
;;//! \htmlinclude Custom.msg.html


(defclass bluerov_ros_playground::Custom
  :super ros::object
  :slots (_id _data ))

(defmethod bluerov_ros_playground::Custom
  (:init
   (&key
    ((:id __id) "")
    ((:data __data) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _id (string __id))
   (setq _data __data)
   self)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; string _id
    4 (length _id)
    ;; float32[] _data
    (* 4    (length _data)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _id
       (write-long (length _id) s) (princ _id s)
     ;; float32[] _data
     (write-long (length _data) s)
     (dotimes (i (length _data))
       (sys::poke (elt _data i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _id
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _id (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32[] _data
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _data (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _data i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get bluerov_ros_playground::Custom :md5sum-) "fedf71ab0b24ef8723140dca2d5458bc")
(setf (get bluerov_ros_playground::Custom :datatype-) "bluerov_ros_playground/Custom")
(setf (get bluerov_ros_playground::Custom :definition-)
      "string id
float32[] data


")



(provide :bluerov_ros_playground/Custom "fedf71ab0b24ef8723140dca2d5458bc")


