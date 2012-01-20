#!/bin/sh -fe
#
# CVS Id $Id: make_icons.sh,v 1.1.1.1 2010/03/08 13:50:45 pjb93 Exp $
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Lesser General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   and the GNU Lesser General Public License  along with this program.  
#   If not, see <http://www.gnu.org/licenses/>.
#
# Run this once to create the required PNGs for icons etc
#
# Note to self for using convert...-draw:
# -draw "circle x0,y0 x1,y1"
# uses x0,y0 = centre and x1,y1 = any point on the perimeter
#
# Warning symbol
#
convert -size 32x32 xc:transparent -fill yellow -stroke orange -draw "polygon 16,4 4,28 28,28" -stroke orange -fill black -pointsize 22 -font Bitstream-Vera-Sans-Mono-Bold -draw "text 10,26 '!'" icons/warning.png
# Make it a bit smaller
convert icons/warning.png -resize 25 icons/warning.png
#
# Info symbol
#
convert -size 32x32 xc:transparent -fill orange -stroke orange -draw "circle 16,16 30,16" -stroke orange -strokewidth 1 -fill white -pointsize 34 -font Century-Schoolbook-Bold -draw "text 9,27 'i'" icons/info.png
# Make it a bit smaller
convert icons/info.png -resize 20 icons/info.png
#
# "Right triangle"
#
convert -size 32x32 xc:transparent -fill blue -stroke blue -strokewidth 2 -draw "polygon 8,4 8,28 24,16" icons/closed.png
# Make it a bit smaller
convert icons/closed.png -resize 20 icons/closed.png
#
# "Down triangle"
#
convert icons/closed.png -rotate 90 icons/open.png
