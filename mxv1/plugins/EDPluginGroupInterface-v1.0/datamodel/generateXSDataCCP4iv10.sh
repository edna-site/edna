#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id:$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
#
#    Contributing author:    Karl Levik (karl.levik@diamond.ac.uk)
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
  echo "ERROR! EDNA_HOME not defined"
  exit 1
fi

xsDataBaseName=XSDataCCP4iv10
xsdHomeDir=${EDNA_HOME}/mxv1/plugins/EDPluginGroupInterface-v1.0/datamodel
pyHomeDir=${EDNA_HOME}/mxv1/plugins/EDPluginGroupInterface-v1.0/plugins
includeXSDFilePath1=${EDNA_HOME}/kernel/datamodel/XSDataCommon.xsd
includeXSDFilePath2=${EDNA_HOME}/mxv1/datamodel/XSDataMXv1.xsd

${EDNA_HOME}/kernel/datamodel/generateDataBinding.sh ${xsDataBaseName} ${xsdHomeDir} ${pyHomeDir} ${includeXSDFilePath1} 
${EDNA_HOME}/kernel/datamodel/generateDataBinding.sh ${xsDataBaseName} ${xsdHomeDir} ${pyHomeDir} ${includeXSDFilePath2} 

