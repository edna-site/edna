#!/usr/bin/env python
# XIA2CoreVersion.py
#
#   Copyright (C) 2006 CCLRC, Graeme Winter
#
#   This code is distributed under the BSD license, a copy of which is 
#   included in the root directory of this package.
#
# 6th June 2006
# 
# A file containing the version number of the current xia 2 core.
# 
# History:
# 
# 0.0.1 - initial build 06/06/06 - something which works but may need
#         steady improvement.
# 
# 0.0.2 - added automated loggraph parsing, changed error status output
# 
# 0.0.3 - added support for clusters via a cluster driver factory
# 
# 0.0.4 - added search through path for the executable as part of 
#         setExecutable.
# 
# 0.1.0 - added like_this as well as likeThis methods, used pretty
#         heavily and it seems ok... this version is for DPA 0.1.0.
#         call it 0.1.1.
#
# 0.1.1.1 version for xia2scan for Rajan with new features. 27/OCT/06.
# 
# 0.2.0 - 08/NOV/06 version for xia2dpa 0.2.0.
#
# 0.2.1 - 08/NOV/06 version for xia2dpa 0.2.1.
# 
# 0.2.2 - 21/NOV/06 version for xia2dpa 0.2.2.
#
# 0.2.2.1 - 23/NOV/06 added check in CCP4 decorator that hklin != hklout
#         (to check_hklin.)
# 0.2.2.4 - 01/DEC/06 added handling of broken loggraph output in CCP4
#         decorator.
# --------------------------- UPDATED LICENSE TO BSD ------------------
# 0.2.3 - new license, some bugs fixed
#
# 0.2.4 - likewise
#
# 0.2.5 - keeping step with the main xia2
#
# 0.2.5.1 - small fixes, ditto 0.2.6.0
# 
# 0.2.6.1 - check if the CCP4 program name includes "-" and test in 
#           the get-status method of the CCP4 decorator.
# 
# Idem, to 0.2.6.6, indeed 0.2.7.2 - however some additional puff
# went into the CCP4 decorator...
#
# 0.3.0.0 - added support for Background class - to support parallel
#           with Mosflm. .1 revision cosmetic.
#
# 0.3.1.0 - some small revisions, handling CCP4 loggraph output.

VersionNumber = "0.3.1.6"

Version = "XIA2 Core %s" % VersionNumber
CVSTag = "xia2core-%s" % VersionNumber.replace('.', '_')
Directory = "xia2core-%s" % VersionNumber

if __name__ == '__main__':
    print 'This is XIA 2 Core version %s' % VersionNumber
    print 'This should be in a directory called "%s"' % Directory
    print 'And should be CVS tagged as "%s"' % CVSTag

    
