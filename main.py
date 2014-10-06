#!/usr/bin/python

########################################
# This project is a lab assignment     #
# for the Essential Skills Module.     #
# University of Amsterdam              #
# MSc in System and Network Engineering#
# Nick Trintafyllidis.                 #
# Use it as you wish :)                #
########################################

import lab
import datacenter

# This file adds some machines to each room and then connects the rooms together.

OS3_lab = lab.Lab()
OS3_servers = datacenter.Datacenter()
OS3_lab.add_workstation("Desktop 17", "network", "Nick Triantafyllidis")
OS3_lab.add_workstation("Desktop 18", "network", "Alex Stavroulakis")
OS3_lab.add_workstation("Desktop 19", "network", "Diana Rusu")
OS3_lab.add_workstation("Desktop 8", "network", "Xavier Torrent Gorjon")
OS3_lab.printall()
OS3_servers.add_server("oxford","network","Nick Triantafyllidis")
OS3_servers.add_server("manchester","network","Alex Stavroulakis")
OS3_servers.add_server("liverpool","network","Diana Rusu")
OS3_servers.add_server("notingham","network","Xavier Torrent Gorjon")
OS3_servers.printall()
OS3_lab.connect("Server room")
OS3_servers.connect("SNE Lab")
OS3_lab.connect("SARA")
OS3_servers.connect("SARA")
OS3_lab.printinfo()
OS3_servers.printinfo()











