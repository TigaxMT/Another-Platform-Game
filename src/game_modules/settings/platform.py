"""
    A simple Game to test neural networks , machine learning etc

    Copyright (C) 2017  Tiago Martins, Kelvin Ferreira

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


"""
    Define platform contants
"""

class PlatformSettings:
    """
        Define some platform settings
    """
    WIDTH = 800
    HEIGHT = 600
    FPS = 60

    # The platform png is 195x71
    # This platform is the base platform
    PLATFORM_LIST = [(0, HEIGHT - 71, 195, 71)]
