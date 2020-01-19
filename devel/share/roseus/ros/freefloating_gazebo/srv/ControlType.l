;; Auto-generated. Do not edit!


(when (boundp 'freefloating_gazebo::ControlType)
  (if (not (find-package "FREEFLOATING_GAZEBO"))
    (make-package "FREEFLOATING_GAZEBO"))
  (shadow 'ControlType (find-package "FREEFLOATING_GAZEBO")))
(unless (find-package "FREEFLOATING_GAZEBO::CONTROLTYPE")
  (make-package "FREEFLOATING_GAZEBO::CONTROLTYPE"))
(unless (find-package "FREEFLOATING_GAZEBO::CONTROLTYPEREQUEST")
  (make-package "FREEFLOATING_GAZEBO::CONTROLTYPEREQUEST"))
(unless (find-package "FREEFLOATING_GAZEBO::CONTROLTYPERESPONSE")
  (make-package "FREEFLOATING_GAZEBO::CONTROLTYPERESPONSE"))

(in-package "ROS")





(defclass freefloating_gazebo::ControlTypeRequest
  :super ros::object
  :slots (_axes ))

(defmethod freefloating_gazebo::ControlTypeRequest
  (:init
   (&key
    ((:axes __axes) (let (r) (dotimes (i 0) (push "" r)) r))
    )
   (send-super :init)
   (setq _axes __axes)
   self)
  (:axes
   (&optional __axes)
   (if __axes (setq _axes __axes)) _axes)
  (:serialization-length
   ()
   (+
    ;; string[] _axes
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _axes)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string[] _axes
     (write-long (length _axes) s)
     (dolist (elem _axes)
       (write-long (length elem) s) (princ elem s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string[] _axes
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _axes (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _axes i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;;
   self)
  )

(defclass freefloating_gazebo::ControlTypeResponse
  :super ros::object
  :slots ())

(defmethod freefloating_gazebo::ControlTypeResponse
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass freefloating_gazebo::ControlType
  :super ros::object
  :slots ())

(setf (get freefloating_gazebo::ControlType :md5sum-) "52951d9d51995d256d1f3d1a265444f8")
(setf (get freefloating_gazebo::ControlType :datatype-) "freefloating_gazebo/ControlType")
(setf (get freefloating_gazebo::ControlType :request) freefloating_gazebo::ControlTypeRequest)
(setf (get freefloating_gazebo::ControlType :response) freefloating_gazebo::ControlTypeResponse)

(defmethod freefloating_gazebo::ControlTypeRequest
  (:response () (instance freefloating_gazebo::ControlTypeResponse :init)))

(setf (get freefloating_gazebo::ControlTypeRequest :md5sum-) "52951d9d51995d256d1f3d1a265444f8")
(setf (get freefloating_gazebo::ControlTypeRequest :datatype-) "freefloating_gazebo/ControlTypeRequest")
(setf (get freefloating_gazebo::ControlTypeRequest :definition-)
      "
string[] axes
---

")

(setf (get freefloating_gazebo::ControlTypeResponse :md5sum-) "52951d9d51995d256d1f3d1a265444f8")
(setf (get freefloating_gazebo::ControlTypeResponse :datatype-) "freefloating_gazebo/ControlTypeResponse")
(setf (get freefloating_gazebo::ControlTypeResponse :definition-)
      "
string[] axes
---

")



(provide :freefloating_gazebo/ControlType "52951d9d51995d256d1f3d1a265444f8")


