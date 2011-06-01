#
#    Project: The EDNA Archive Project
#             http://www.edna-site.org
#
#    File: "$Id:$"
#
#    Copyright (C) 2008-2009 Diamond Light Source
#                            Chilton, Didcot, UK
#
#    Principal author:       Mark Basham (mark.basham@diamond.ac.uk)
#
#    Contributing authors:   Olof Svensson (svensson@esrf.fr) 
#                            Marie-Francoise Incardona (incardon@esrf.fr)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


if [ -z "$EDNA_HOME" ]; then
  echo "ERROR! EDNA_HOME not defined"
  exit 1
fi

echo ${EDNA_HOME}

xsDataBaseName=XSDataExecSRBRegisterv10
xsdHomeDir=${EDNA_HOME}/darcv1/plugins/EDPluginExecSRBRegister-v1.0/datamodel
pyHomeDir=${EDNA_HOME}/darcv1/plugins/EDPluginExecSRBRegister-v1.0/plugins
includeXSDFilePath=${EDNA_HOME}/kernel/datamodel/XSDataCommon.xsd

${EDNA_HOME}/kernel/datamodel/generateDataBinding.sh ${xsDataBaseName} ${xsdHomeDir} ${pyHomeDir} ${includeXSDFilePath} 
