#!/usr/bin/python

class DellKeyboard(object):
    def __init__(self):
        self.make = "Dell"
        self.model = "KB212-B"
        self.color = "Black"
        self.connection="none"

    def printinfo(self):
        print "*****"
        print "Make:" + self.make
        print "Model:" + self.model
        print "Color:" + self.color
        print "Connection:" + self.connection
        print "*****"


    def connect(self, connection):
        self.connection = connection

class DellMouse(object):
    def __init__(self):
        self.make = "Dell"
        self.model = "MS111-L"
        self.color = "Black"
        self.connection = "none"

    def printinfo(self):
        print "*****"
        print "Make:" + self.make
        print "Model:" + self.model
        print "Color:" + self.color
        print "Connection:" + self.connection
        print "*****"


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
        print "*****"
        print "Make:" + self.make
        print "Model:" + self.model
        print "Size:" + self.size
        print "Color:" + self.color
        print "Connection:" + self.connection
        print "*****"


    def connect(self, connection):
        self.connection = connection


class Workstation(object):
    def __init__(self):
        self.name = "None"
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

class Lab(object):

    def __init__(self):
        self.name = "B1.23 Lab"
        self.workstations = []

    def add_workstation(self,name,connection,owner):

        temp = Workstation()
        temp.name_it(name)
        temp.connect(connection)
        temp.assign(owner)
        self.workstations.append(temp)

    def printinfo(self):
        print self.name
        for i in self.workstations:
            print i.name + " " + i.owner + " " + i.connection

    def printall(self):
        self.printinfo()
        print "\t"
        for i in self.workstations:
            i.printall()


OS3_lab = Lab()
OS3_lab.add_workstation("Desktop 17", "network", "Nick Triantafyllidis")
OS3_lab.add_workstation("Desktop 18", "network", "Alex Stavroulakis")
OS3_lab.add_workstation("Desktop 19", "network", "Diana Rusu")
OS3_lab.add_workstation("Desktop 8", "network", "Xavier Torrent Gorjon")
OS3_lab.printall()










