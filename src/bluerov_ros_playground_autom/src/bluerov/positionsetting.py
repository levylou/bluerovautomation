#!/usr/bin/env python

import rospy
import time
from tkinter import *
try:
    import pubs
    import subs
except:
    import bluerov.pubs as pubs
    import bluerov.subs as subs

pub = pubs.Pubs()
sub = subs.Subs()

from bluerov_ros_playground.msg import Custom
from std_msgs.msg import Float32

d = []
x = []
y = []
z = []
yaw = []
#roll = []

def set_action():
    global d
    x_value = float(x_eingabe.get())
    y_value = float(y_eingabe.get())
    z_value = float(z_eingabe.get())
    yaw_value = float(yaw_eingabe.get())
    #roll_value = float(roll_eingabe.get())

    if (x_value == "" or y_value == "" or z_value == "" or yaw_value == ""): # or roll_value == ""
        result_label.config(text = "Gib zuerst Werte ein.")
    elif z_value >= 0:
        result_label.config(text = "Z muss negativ sein.")
    elif (yaw_value < -3.1415 or yaw_value > 3.1415): #roll_value < -3.1415 or roll_value > 3.1415 or 
        result_label.config(text = "Yaw muss in Rad eingeragen werden.")
    else:
        d = [float(x_value),float(y_value),float(z_value),float(yaw_value)] #,float(roll_value)
        data = Custom()
        data.id = "positions"
        data.data =  d
        pub.set_data('/desiredposition', data)
        result_label.config(text = "Neue Zielwerte eingetragen")
        x_label_old.config(text = d[0])
        y_label_old.config(text = d[1])
        z_label_old.config(text = d[2])
        yaw_label_old.config(text = d[3])
        #roll_label_old.config(text = d[4])
        return d

def next_action():
    #if (sub.get_data()['next_pos']['id'] == "fetch"):
    #    fetch = sub.get_data()['next_pos']['data']
    #if fetch == 1:
    global x, y, z, yaw #, roll

    x_value = float(x_eingabe.get())
    y_value = float(y_eingabe.get())
    z_value = float(z_eingabe.get())
    yaw_value = float(yaw_eingabe.get())
    #roll_value = float(roll_eingabe.get())

    if (x_value == "" or y_value == "" or z_value == "" or yaw_value == ""): # or roll_value == ""
        result_label.config(text = "Gib zuerst Werte ein.")
    elif z_value >= 0:
        result_label.config(text = "Z muss negativ sein.")
    elif (yaw_value < -3.1415 or yaw_value > 3.1415): #roll_value < -3.1415 or roll_value > 3.1415 or 
        result_label.config(text = "Yaw muss in Rad eingetragen werden.")
    else:
        x.append(x_value)
        y.append(y_value)
        z.append(z_value)
        yaw.append(yaw_value)
        #roll.append(roll_value)
        x_label_next.config(text = x)
        y_label_next.config(text = y)
        z_label_next.config(text = z)
        yaw_label_next.config(text = yaw)
        #roll_label_next.config(text = roll)
        result_label.config(text = "Naechste Zielwerte eingetragen")
        return x, y, z, yaw #, roll


fenster = Tk()
fenster.title("Zieleingabe")

x_eingabe = Entry(fenster, bd = 5, width = 10)
x_label = Label(fenster, text = "X:")
x_label_old = Label(fenster, text = -2)
x_label_next= Label(fenster)
y_eingabe = Entry(fenster, bd = 5, width = 10)
y_label = Label(fenster, text = "Y:")
y_label_old = Label(fenster, text = 2)
y_label_next= Label(fenster)
z_eingabe = Entry(fenster, bd = 5, width = 10)
z_label = Label(fenster, text = "Z:")
z_label_old = Label(fenster, text = -1.5)
z_label_next= Label(fenster)
yaw_eingabe = Entry(fenster, bd = 5, width = 10)
yaw_label = Label(fenster, text = "Yaw:")
yaw_label_old = Label(fenster, text = 0)
yaw_label_next= Label(fenster)
#roll_eingabe = Entry(fenster, bd = 5, width = 10)
#roll_label = Label(fenster, text = "Roll:")
#roll_label_old = Label(fenster, text = 0.01)
#roll_label_next= Label(fenster)

stat_label = Label(fenster, text = "aktuelle Zielposition")
next_label = Label(fenster, text = "naechste Zielpositionen")
result_label = Label(fenster, width = 50)
set_button = Button(fenster, text = "aktuelle Zielposition aendern", command = set_action)
next_button = Button(fenster, text = "naechste Zielposition einfuegen", command = next_action)
exit_button = Button(fenster, text = "Beenden", command = fenster.quit)

stat_label.grid(row = 0, column = 2)
next_label.grid(row = 0, column = 3)
x_label.grid(row = 1, column = 0)
x_eingabe.grid(row = 1, column = 1)
x_label_old.grid(row = 1, column = 2)
x_label_next.grid(row = 1, column = 3)
y_label.grid(row = 2, column = 0)
y_eingabe.grid(row = 2, column = 1)
y_label_old.grid(row = 2, column = 2)
y_label_next.grid(row = 2, column = 3)
z_label.grid(row = 3, column = 0)
z_eingabe.grid(row = 3, column = 1)
z_label_old.grid(row = 3, column = 2)
z_label_next.grid(row = 3, column = 3)
yaw_label.grid(row = 4, column = 0)
yaw_eingabe.grid(row = 4, column = 1)
yaw_label_old.grid(row = 4, column = 2)
yaw_label_next.grid(row = 4, column = 3)
#roll_label.grid(row = 5, column = 0)
#roll_eingabe.grid(row = 5, column = 1)
#roll_label_old.grid(row = 5, column = 2)
#roll_label_next.grid(row = 5, column = 3)
set_button.grid(row = 7, column = 2)
next_button.grid(row = 7, column = 3)
exit_button.grid(row = 7, column = 0)
result_label.grid(row = 6, column = 0, columnspan = 3)

rospy.init_node('positionsetting_node', log_level=rospy.DEBUG)
pub.subscribe_topic('/desiredposition', Custom)
sub.subscribe_topic('/next_pos', Custom)

try:
    if (sub.get_data()['next_pos']['id'] == "fetch"):
        next_pos = sub.get_data()['next_pos']['data']
        print next_pos
    if (next_pos[0] == 1.0):
        d[0] = x.pop(0)
        d[1] = y.pop(0)
        d[2] = z.pop(0)
        d[3] = yaw.pop(0)
        #d[4] = roll.pop(0)
        data = Custom()
        data.id = "positions"
        data.data =  d
        pub.set_data('/desiredposition', data)
        x_label_old.config(text = d[0])
        y_label_old.config(text = d[1])
        z_label_old.config(text = d[2])
        yaw_label_old.config(text = d[3])
        #roll_label_old.config(text = d[4])
        x_label_next.config(text = x)
        y_label_next.config(text = y)
        z_label_next.config(text = z)
        yaw_label_next.config(text = yaw)
        #roll_label_next.config(text = roll)
except Exception as error:
    print ('d.pop[0] error:', error)

mainloop()

