# -*- coding: utf8 -*-
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id:$"
#
#    Copyright (C) 2012-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Jérôme Kieffer (jerome.kieffer@esrf.fr)
# 
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

"""
Set an environment variable "EDNA_LOCK" to help debugging 
any dead-locks- inside EDNA 
"""

__authors__ = [ "Jérôme Kieffer" ]
__contact__ = "jerome.kieffer@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120401"
import uuid, sys, os, traceback
import threading
_Semaphore = threading._Semaphore

if os.environ.get("EDNA_LOCK", False):
    class Semaphore(_Semaphore):
        """
        threading.Semaphore like class with helper for fighting dead-locks
        """
        def __init__(self, *arg, **kwarg):
            _Semaphore.__init__(self, *arg, **kwarg)
            self.blocked = []

        def acquire(self, *arg, **kwarg):
            if self._Semaphore__value == 0:
                uid = uuid.uuid4()
                self.blocked.append(uid)
                sys.stderr.write("Blocking sem %s" %
                                 os.linesep.join([str(uid)] + \
                                        traceback.format_stack()[:-1] + [""]))
            return _Semaphore.acquire(self, *arg, **kwarg)

        def release(self, *arg, **kwarg):
            if self.blocked:
                try:
                    uid = self.blocked.pop()
                except Exception:
                    pass
                else:
                    sys.stderr.write("Released sem %s %s" % (uid, os.linesep))
            _Semaphore.release(self, *arg, **kwarg)

        def __enter__(self):
            self.acquire()
            return self

        def __exit__(self, *arg, **kwarg):
            self.release()
else:
    Semaphore = threading.Semaphore

