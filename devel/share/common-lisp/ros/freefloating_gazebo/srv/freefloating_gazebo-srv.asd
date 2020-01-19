
(cl:in-package :asdf)

(defsystem "freefloating_gazebo-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ControlType" :depends-on ("_package_ControlType"))
    (:file "_package_ControlType" :depends-on ("_package"))
  ))