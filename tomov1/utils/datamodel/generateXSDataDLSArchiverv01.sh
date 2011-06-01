#!/bin/bash
#
#    Project: The EDNA Prototype
#             http://www.edna-site.org
#
#    File: "$Id: generateXSDataMOSFLMv01.sh 482 2008-07-31 15:06:56Z svensson $"
#
#    Copyright (C) 2008 European Synchrotron Radiation Facility
#                       Grenoble, France
#
#    Principal authors: Marie-Francoise Incardona (incardon@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
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

PYTHON=python
xsDataBaseName=XSDataDLSArchiverv01
pluginHome=${EDNA_HOME}/tomov1/plugins/EDPluginDLSArchiver-v0.1

cp ${EDNA_HOME}/tomov1/utils/datamodel/process_includes.py ${EDNA_HOME}/tomov1/tmp
cp ${EDNA_HOME}/tomov1/datamodel/XSDataCommonv01.xsd ${EDNA_HOME}/tomov1/tmp
cp ${pluginHome}/datamodel/${xsDataBaseName}.exsd ${EDNA_HOME}/tomov1/tmp

cd ${EDNA_HOME}/tomov1/tmp

${PYTHON} process_includes.py ${xsDataBaseName}.exsd ${xsDataBaseName}_PI.exsd

${PYTHON} ${EDNA_HOME}/tomov1/utils/datamodel/EDGenerateDS.py -f --use-old-getter-setter -o ${pluginHome}/plugins/${xsDataBaseName}.py ${EDNA_HOME}/tomov1/tmp/${xsDataBaseName}_PI.exsd
