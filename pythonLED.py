#!/usr/bin/python
import sys
LED3_PATH = "/sys/class/leds/beaglebone:green:usr3"

def write2LED(fileName, value, path=LED3_PATH):
    """This function writes to the passed value to the file in the path"""
    fo = open(path + fileName, "w")
    fo.write(value)
    fo.close()
    return


def removeTrigger():
    """Writes "none" in trigger"""
    write2LED("/trigger","none")
    return

print("Starting the Scrpt")
if len(sys.argv) != 2:
    """"Checks if number of arguments are right"""
    print("Wrong number of arguments")
    sys.exit(2)
    
if sys.argv[1] == "on":
    """Turns on LED3"""
    print("LED3 on")
    removeTrigger()
    write2LED("/brightness", "1")
elif sys.argv[1] == "off":
    """Turns off LED3"""
    print("LED3 off")
    removeTrigger()
    write2LED("/brightness", "0")
elif sys.argv[1] == "flash":
    """LED3 starts flashing 50ms on, 50ms off (needs sudo)"""
    print("LED3 flashing")
    removeTrigger()
    write2LED("/trigger", "timer")
    write2LED("/delay_on", "50")
    write2LED("/delay_off", "50")
else:
    print("Wrong arguments")
    
print("Script Done")
    
    
