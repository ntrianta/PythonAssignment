########################################
# This project is a lab assignment     #
# for the Essential Skills Module.     #
# University of Amsterdam              #
# MSc in System and Network Engineering#
# Nick Trintafyllidis.                 #
# Use it as you wish :)                #
########################################

import workstation

class Lab(object):

    def __init__(self):
        self.name = "B1.23 Lab"
        self.workstations = []
        self.connections = []


    def add_workstation(self,name,connection,owner):

        temp = workstation.Workstation()
        temp.name_it(name)
        temp.connect(connection)
        temp.assign(owner)
        self.workstations.append(temp)

    def connect(self, connection):
        self.connections.append(connection)

    def printinfo(self):
        print "*****"
        print self.name
        print "Machines:"
        for i in self.workstations:
            print i.name + " " + i.owner + " " + i.connection
        print "Connected to:"
        for i in self.connections:
            print i
        print "*****"


    def printall(self):
        self.printinfo()
        print "\t"
        for i in self.workstations:
            i.printall()