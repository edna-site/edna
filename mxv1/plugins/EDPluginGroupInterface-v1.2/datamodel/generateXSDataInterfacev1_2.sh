#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id:$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
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


if [ -z "$EDNA_HOME" ]; then
#	This cryptic version is kept in case of need ... showed to be useful for MacOSX users
#	full_path="$(cd "${0%/*}" 2>/dev/null; echo "$PWD"/"${0##*/}")"
	full_path=$( readlink -fn $0)
	export EDNA_HOME=`dirname "$full_path" | sed 's/\/mxv1\/.*\/datamodel$//'`
	echo "Guessing EDNA_HOME= "$EDNA_HOME
fi

xsDataBaseName=XSDataInterfacev1_2
xsdHomeDir=${EDNA_HOME}/mxv1/plugins/EDPluginGroupInterface-v1.2/datamodel
pyHomeDir=${EDNA_HOME}/mxv1/plugins/EDPluginGroupInterface-v1.2/plugins
includeXSDFilePath1=${EDNA_HOME}/kernel/datamodel/XSDataCommon.xsd
includeXSDFilePath2=${EDNA_HOME}/mxv1/datamodel/XSDataMXv1.xsd

${EDNA_HOME}/kernel/datamodel/generateDataBinding.sh ${xsDataBaseName} ${xsdHomeDir} ${pyHomeDir} ${includeXSDFilePath1} 
${EDNA_HOME}/kernel/datamodel/generateDataBinding.sh ${xsDataBaseName} ${xsdHomeDir} ${pyHomeDir} ${includeXSDFilePath2} 

