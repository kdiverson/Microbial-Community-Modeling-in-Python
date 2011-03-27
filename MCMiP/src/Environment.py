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
__date__ ="$27-Mar-2011 15:00:07$"

from SimPy.SimulationTrace import *

if __name__ == "__main__":
    print "Hello World"

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