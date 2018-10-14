"""
    A simple platform game written in Python

    Copyright (C) 2017-2018  Tiago Martins, Kelvin Ferreira

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os


class Save_Score:
    def __init__(self,score="0"):
        self.score = score

    def writeScore(self,score):

        self.readScore()

        self.score = int(self.score)
        score = int(score)

        if score > self.score:
            file = open("Score.txt","w")

            file.write(str(score))

            file.close()

    def readScore(self):

        if os.path.exists("Score.txt"):
            file = open("Score.txt","r")

            self.score = file.read()

            file.close()

        else:
            self.score = "0"
        
        return self.score