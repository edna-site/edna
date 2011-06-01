#!/bin/sh
#
#    Project: DiffractCTv1
#             http://www.edna-site.org
#
#    File: "$Id: $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author: Olof Svensson (svensson@esrf.fr)
#					   Jerome Kieffer (kieffer@esrf.fr
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    and the GNU Lesser General Public License  along with this program.  
#    If not, see <http://www.gnu.org/licenses/>.
#

# This program is designed to setup the edna-tango-server on a computer to accept
# On-Line data analysis calculations 


export TANGO_HOST=mufid6:20000

abs_path=$(readlink -fn ${0})
export EDNA_HOME=$(dirname "${abs_path}" | sed 's/\/diffractionCTv1\/bin$//')
#export EDNA_HOME=$HOME/workspace/edna
export EDNA_SITE=ESRF

TestSpace=/tmp/${USER}_edna_test
if [ ! -d $TestSpace ] ;
then
	mkdir $TestSpace
fi
cd $TestSpace


###here starts the mess 


Version=redhate4_64
txt=$(grep "release 5" /etc/redhat-release)
if [ -n "$txt" ]
then 
	Version=redhate5_64
	export PYTHONPATH=/segfs/tango/release/redhate4_64
	export LD_LIBRARY_PATH=/segfs/tango/release/redhate4_64/PyTango:$LD_LIBRARY_PATH:/segfs/tango/release/redhate4_64/lib
fi
txt=$(grep "release 4" /etc/redhat-release)
if  [ -n "$txt" ]
then 
	Version=redhate4_64
	export PYTHONPATH=/segfs/tango/release/$Version
	export LD_LIBRARY_PATH=/segfs/tango/release/$Version/PyTango:$LD_LIBRARY_PATH
fi
echo Linux Version= $Version
echo EDNA home= $EDNA_HOME

export LD_LIBRARY_PATH=/segfs/tango/release/$Version/lib:$LD_LIBRARY_PATH
/opt/pxsoft/tools/python/v2.5.4/redhate4-x86_64/bin/python -u $EDNA_HOME/diffractionCTv1/bin/edna-tango-server.py id22

 