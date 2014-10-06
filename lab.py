import workstation

class Lab(object):

    def __init__(self):
        self.name = "B1.23 Lab"
        self.workstations = []

    def add_workstation(self,name,connection,owner):

        temp = workstation.Workstation()
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