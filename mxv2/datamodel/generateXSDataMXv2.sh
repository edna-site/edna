#
#    Project: MXv2
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


full_path="$(cd "${0%/*}" 2>/dev/null; echo "$PWD"/"${0##*/}")"
export EDNA_HOME=`dirname "$full_path" | sed 's/\/mxv2\/datamodel$//'`

xsDataBaseName=XSDataMXv2
xsdHomeDir=${EDNA_HOME}/mxv2/datamodel
pyHomeDir=${EDNA_HOME}/mxv2/src
includeXSDFilePath=${EDNA_HOME}/kernel/datamodel/XSDataCommon.xsd

sh ${EDNA_HOME}/kernel/datamodel/generateDataBinding.sh ${xsDataBaseName} ${xsdHomeDir} ${pyHomeDir} ${includeXSDFilePath} 
