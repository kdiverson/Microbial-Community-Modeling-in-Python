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
__date__ ="$27-Mar-2011 15:01:02$"

from SimPy.SimulationTrace import *

if __name__ == "__main__":
    print "Hello World"

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