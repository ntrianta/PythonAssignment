#!/usr/bin/python

class DellKeyboard(object):
    def __init__(self):
        self.make = "Dell"
        self.model = "KB212-B"
        self.color = "Black"
        self.connection="none"

    def printinfo(self):
        print self.make
        print self.model
        print self.color
        print self.connection

    def connect(self, connection):
        self.connection = connection

class DellMouse(object):
    def __init__(self):
        self.make = "Dell"
        self.model = "MS111-L"
        self.color = "Black"
        self.connection = "none"

    def printinfo(self):
        print self.make
        print self.model
        print self.color
        print self.connection

    def connect(self, connection):
       self.connection = connection


class DellMonitor(object):
    def __init__(self):
        self.make = "Dell"
        self.model = "2209WAf"
        self.size = "22 inch"
        self.color = "Black & Silver"
        self.connection="none"

    def printinfo(self):
        print self.make
        print self.model
        print self.size
        print self.color
        print self.connection

    def connect(self, connection):
        self.connection = connection


class Workstation(object):
    def __init__(self):
        self.make = "Dell"
        self.model = "Optiplex 7010"
        self.color = "Black"
        self.os = "Ubuntu 14.10"
        self.connection = "None"
        self.owner="Nobody"
        self.monitor1 = DellMonitor()
        self.monitor2 = DellMonitor()
        self.keyboard = DellKeyboard()
        self.mouse = DellMouse()
        self.monitor1.connect("VGA")
        self.monitor2.connect("VGA")
        self.keyboard.connect("USB")
        self.mouse.connect("USB")

    def printinfo(self):
        print self.make
        print self.model
        print self.color
        print self.connection
        print self.os
        print self.owner

    def printall(self):
        self.printinfo()
        self.monitor1.printinfo()
        self.monitor2.printinfo()
        self.keyboard.printinfo()
        self.mouse.printinfo()





