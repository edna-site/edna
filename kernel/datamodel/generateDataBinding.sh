#!/bin/bash
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id:$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Marie-Francoise Incardona (incardon@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
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

usage="Usage: $0 XSDataBaseName XSDHomeDir PyHomeDir [XSDIncludeFile]"

if [ -z $PYTHON ];
then
    echo "Note: If you encounter a python error at this step, "
    echo "      please check that the \$PYTHON environment variable "
    echo "      correspond to the python binary you intent to use."    
    export PYTHON=$(which python)
    echo "\$PYTHON = $PYTHON" 
fi

if [ -z "$EDNA_HOME" ]; then
  full_path="$(cd "${0%/*}" 2>/dev/null; echo "$PWD"/"${0##*/}")"
  export EDNA_HOME=`dirname "$full_path" | sed 's/\/kernel\/datamodel$//'`
fi

xsDataBaseName=$1
xsdHomeDir=$2
pyHomeDir=$3


if [ $# -eq 3 ]; then
    
    ${PYTHON} ${EDNA_HOME}/kernel/datamodel/EDGenerateDS.py -f --use-old-getter-setter  -a "xs:" -o ${pyHomeDir}/${xsDataBaseName}.py ${xsdHomeDir}/${xsDataBaseName}.xsd 

elif [ $# -eq 4 ]; then
    TMP_DIR=${EDNA_HOME}/tmp
    if [ ! -d ${TMP_DIR} ]; then
        mkdir ${TMP_DIR} 
    fi
    cp ${EDNA_HOME}/kernel/datamodel/process_includes.py ${TMP_DIR}
    cp $4 ${TMP_DIR} 
    cp ${xsdHomeDir}/${xsDataBaseName}.xsd ${TMP_DIR}
    cd ${TMP_DIR}
    ${PYTHON} process_includes.py ${xsDataBaseName}.xsd ${xsDataBaseName}_PI.xsd
    ${PYTHON} ${EDNA_HOME}/kernel/datamodel/EDGenerateDS.py -f --use-old-getter-setter -o ${pyHomeDir}/${xsDataBaseName}.py ${TMP_DIR}/${xsDataBaseName}_PI.xsd
else
  echo $usage
fi

# Patch the file for bug #394
${PYTHON} ${EDNA_HOME}/kernel/datamodel/patchGenerateDSDataBinding.py ${pyHomeDir}/${xsDataBaseName}.py
