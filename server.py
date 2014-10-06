#########################################
# This project is a lab assignment      #
# for the Essential Skills Module.      #
# University of Amsterdam               #
# MSc in System and Network Engineering #
# Nick Trintafyllidis.                  #
# Use it as you wish :)                 #
#########################################

class Server(object):
    def __init__(self):
        self.name = "None"
        self.make = "IBM"
        self.os = "Ubuntu 14.10 Server"
        self.connection = "None"
        self.owner = "Nobody"

    def printinfo(self):
        print "*****"
        print "Name:" + self.name
        print "Make:" + self.make
        print "Connection:" + self.connection
        print "Operating System:" + self.os
        print "Owner:" + self.owner
        print "*****"

    def connect(self, connection):
        self.connection = connection

    def assign(self, owner):
        self.owner = owner

    def name_it(self, name):
        self.name = name
