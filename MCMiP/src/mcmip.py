#! /usr/bin/python

#  Copyright (C) 2011 Kathryn Iverson <kd.iverson at gmail.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

__author__="Kathryn Iverson <kd.iverson at gmail.com>"
__date__ ="$19-Mar-2011 13:34:06$"

from SimPy.SimulationTrace import *


class Environment():
    def __init__(self):
        c = Resource(capacity=100,name='carbon',unitName='sugar')
        h = Resource(capacity=150,name='hydrogen',unitName='H2')
        n = Resource(capacity=25,name='nitrogen',unitName='amonia')
        o = Resource(capacity=50,name='oxygen',unitName='O2')

    def get_carbon(self):
        return self.c
    def get_hydrogen(self):
        return self.h
    def get_nitrogen(self):
        return self.n
    def get_oxygen(self):
        return self.o
    
    def eat_carbon(self,value):
        self.c = self.c-value
    def eat_hydrogen(self,value):
        self.h = self.h-value
    def eat_nitrogen(self,value):
        self.n = self.n-value
    def eat_oxygen(self,value):
        self.o = self.o-value

    def add_carbon(self,value):
        self.c = self.c+value
    def add_hydrogen(self,value):
        self.h = self.h+value
    def addt_nitrogen(self,value):
        self.n = self.n+value
    def add_oxygen(self,value):
        self.o = self.o+value


class Microbe(Process):
    def __init__(self,name,cc):
        Process.__init__(self,name=name)
        self.cc = cc

    def go(self,env):
        if env.get_carbon() > 10:
            print now( ), self.name, "born"
            env.eat_carbon(20)
            yield hold,self,100.0
        else:
            print now( ), self.name, "died"

initialize( )
env = Environment() #initialize the environment
m1  = Microbe("microbe1",2000)       # a new microbe
activate(m1,m1.go(env),at=6.0) # activate at time 6.0
m2  = Microbe("microbe2",1600)       # another new microbe
activate(m2,m2.go(env))        # activate at time 0
simulate(until=200)
print 'Current time is ',now( ) # will print 106.