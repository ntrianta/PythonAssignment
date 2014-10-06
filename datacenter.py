########################################
# This project is a lab assignment     #
# for the Essential Skills Module.     #
# University of Amsterdam              #
# MSc in System and Network Engineering#
# Nick Trintafyllidis.                 #
# Use it as you wish :)                #
########################################

import server

class Datacenter(object):

    def __init__(self):
        self.name = "OS3 Server Room"
        self.servers = []
        self.connections = []

    def add_server(self,name,connection,owner):

        temp = server.Server()
        temp.name_it(name)
        temp.connect(connection)
        temp.assign(owner)
        self.servers.append(temp)

    def connect(self, connection):
        self.connections.append(connection)

    def printinfo(self):
        print "*****"
        print self.name
        for i in self.servers:
            print i.name + " " + i.owner + " " + i.connection
        print "connected to:"
        for i in self.connections:
            print i
        print "*****"


    def printall(self):
        self.printinfo()
        print "\t"
        for i in self.servers:
            i.printinfo()
