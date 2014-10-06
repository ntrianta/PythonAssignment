#########################################
# This project is a lab assignment      #
# for the Essential Skills Module.      #
# University of Amsterdam               #
# MSc in System and Network Engineering #
# Nick Trintafyllidis.                  #
# Use it as you wish :)                 #
#########################################

import keyboard
import mouse
import monitor

class Workstation(object):
    def __init__(self):
        self.name = "None"
        self.make = "Dell"
        self.model = "Optiplex 7010"
        self.color = "Black"
        self.os = "Ubuntu 14.10"
        self.connection = "None"
        self.owner = "Nobody"
        self.monitor1 = monitor.DellMonitor()
        self.monitor2 = monitor.DellMonitor()
        self.keyboard = keyboard.DellKeyboard()
        self.mouse = mouse.DellMouse()
        self.monitor1.connect("VGA")
        self.monitor2.connect("VGA")
        self.keyboard.connect("USB")
        self.mouse.connect("USB")

    def printinfo(self):
        print "*****"
        print "Name:" + self.name
        print "Make:" + self.make
        print "Model:" + self.model
        print "Color:" + self.color
        print "Connection:" + self.connection
        print "Operating System:" + self.os
        print "Owner:" + self.owner
        print "*****"

    def printall(self):
        self.printinfo()
        print "Monitor 1:"
        self.monitor1.printinfo()
        print "Monitor 2:"
        self.monitor2.printinfo()
        print "Keyboard:"
        self.keyboard.printinfo()
        print "Mouse:"
        self.mouse.printinfo()

    def connect(self, connection):
        self.connection = connection

    def assign(self, owner):
        self.owner = owner

    def name_it(self, name):
        self.name = name
