#!/bin/bash

# add the test programs to the path
export PATH=${PATH}:${XIA2CORE_ROOT}/Test

# check now according to platform

platform=`uname`

if [ "$platform" = "Darwin" ]; then
    arch=`uname -a | awk '{print $NF}'`
    if [ "$arch" == "powerpc" ]; then
	export PATH=${PATH}:${XIA2CORE_ROOT}/Test/Compiled/mac_ppc
    elif [ "$arch" == "i386" ]; then
	export PATH=${PATH}:${XIA2CORE_ROOT}/Test/Compiled/mac_386
    fi
elif [ "$platform" = "Linux" ]; then
    export PATH=${PATH}:${XIA2CORE_ROOT}/Test/Compiled/linux_386
fi

