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

OS3_lab = lab.Lab()
OS3_servers = datacenter.Datacenter()
OS3_lab.add_workstation("Desktop 17", "network", "Nick Triantafyllidis")
OS3_lab.add_workstation("Desktop 18", "network", "Alex Stavroulakis")
OS3_lab.add_workstation("Desktop 19", "network", "Diana Rusu")
OS3_lab.add_workstation("Desktop 8", "network", "Xavier Torrent Gorjon")
OS3_lab.printall()











