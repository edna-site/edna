#!/usr/bin/python

__authors__=["Manuel Taurel", "Staffan Ohlsson"]

import PyTango
import time

class CB(object):
    def push_event(self, event):
        if event.attr_value is not None:
            if event.attr_value.name=="statisticsCollected":
               print("%s:  %s"%(time.ctime(),event.attr_value.name))
               print(event.attr_value.value)
            else:
               print("%s: %s %s"%(time.ctime(),event.attr_value.name, event.attr_value.value))
        else:
            print("Please investigate !!!")
            print event
dev=PyTango.DeviceProxy("dau/edna/1")
print("Tango event watcher for EDNA")
print("Press ctrl-C to quit")
cb=CB()
dev.subscribe_event("jobSuccess", PyTango.EventType.CHANGE_EVENT, cb, [], True) 
dev.subscribe_event("jobFailure", PyTango.EventType.CHANGE_EVENT, cb, [], True) 
dev.subscribe_event("statisticsCollected", PyTango.EventType.CHANGE_EVENT, cb, [], True) 

while True:
    time.sleep(1)
