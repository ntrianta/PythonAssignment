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