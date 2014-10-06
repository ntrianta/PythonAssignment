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