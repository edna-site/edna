#!/bin/csh

# add the test programs to the path
setenv PATH ${PATH}:${XIA2CORE_ROOT}/Test

# next the compiled ones, based on the uname

setenv platform `uname`

# FIXME this needs to account for mac_ppc

if ( "$platform" == "Linux" ) then
    setenv PATH ${PATH}:${XIA2CORE_ROOT}/Test/Compiled/linux_386
else
    setenv arch `uname -a | awk '{print $NF}'`
    if ( "$arch" == "powerpc" ) then
        setenv PATH ${PATH}:${XIA2CORE_ROOT}/Test/Compiled/mac_ppc
    else
        setenv PATH ${PATH}:${XIA2CORE_ROOT}/Test/Compiled/mac_386
    endif
endif

