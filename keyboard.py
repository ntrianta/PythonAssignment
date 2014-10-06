#########################################
# This project is a lab assignment      #
# for the Essential Skills Module.      #
# University of Amsterdam               #
# MSc in System and Network Engineering #
# Nick Trintafyllidis.                  #
# Use it as you wish :)                 #
#########################################


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
