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


export TANGO_HOST=mufid6:20000

PathToProg=$( readlink -fn $0 )
export EDNA_HOME=$(dirname "${PathToProg}" | sed 's/\/diffractionCTv1\/bin$//')
export EDNA_SITE=ESRF

export TestSpace=/tmp/${USER}_edna_test
if [ ! -d $TestSpace ] ;
then
	mkdir $TestSpace
fi


Version=redhate4_64
txt=$(grep "release 5" /etc/redhat-release)
if [ -n "$txt" ]
then 
	Version=redhate5_64
	export PYTHONPATH=/segfs/tango/release/$Version/PyTango/lib/python2.6/site-packages 
	export LD_LIBRARY_PATH=/segfs/tango/release/$Version/lib:/segfs/tango/release/$Version/PyTango/lib:$LD_LIBRARY_PATH
	export PYTHON=/sware/isdd/soft/python/v2.6.6_20110224/centos5-x86_64/bin/python
	#/sware/exp/scisoft/tools-x86_64/bin/python
fi
txt=$(grep "release 4" /etc/redhat-release)
if  [ -n "$txt" ]
then 
	Version=redhate4_64
	export PYTHONPATH=/segfs/tango/release/$Version
	export LD_LIBRARY_PATH=/segfs/tango/release/$Version/PyTango:/segfs/tango/release/$Version/lib:$LD_LIBRARY_PATH
	export PYTHON=/opt/pxsoft/tools/python/v2.5.4/redhate4-x86_64/bin/python 
fi

#if [ ! -z $(echo $PythonProg|grep server) ]
#then
#	echo "Server Mode"
#	echo $PYTHON -u $PythonProg id22
#	cd $TestSpace
#	$PYTHON -u $PythonProg id22
#else
#	echo "Client Mode"
#	echo $PYTHON -u $PythonProg $1" (and maybe others)"
#	$PYTHON -u $PythonProg $*
#fi 

 
