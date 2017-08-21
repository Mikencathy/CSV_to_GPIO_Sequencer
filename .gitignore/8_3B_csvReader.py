# This will read data on a CSV File line by line.
# The data will be then fed to the GPIO pins fot output
# Cycles will continue infinetly



#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
import time
rNum = 8
colVal = 0
togOut = 0
realPin = 0
repeat = 0
pins = 11 #sub 1 to Total Pins
delay = 1
pinList = [5,7,8,10,11,12,13,15,16,18,19,21,22,23,24,26]

# Initialize GPIO pins
#for i in pinList:
#   GPIO.setup(i,GPIO.OUT)
#   GPIO.output(i,True)



# Select File to open and delay
print('Select CSV file to use')
file = input("-->")
print('Enter stepping time')
delay = input("-->")

      

print('Use Ctrl-C to stop Execution')
 
#Open file
myCsv = open(file, 'r')

# Read file and Convert to readable string
allText = myCsv.read()

#Break up string by rows
rows = allText.split('\n')
#print(rows)

#Run Forever

while 3 == 3:
     
     

     #Loop thru row by row
     length = (len(rows)) #number of rows
     #print('Total Lines = ', length - 1)

     for rNum in range(1, length -1):
          cNum = rows[rNum].split(',')
          print(cNum)
          outputPin = 1
          #cNum are the line values
          time.sleep(float(delay))
          for value in cNum:
               tog = 0
               if value =='1': tog = 1
               if value == ',': continue
               
               # GPIO pin cross Reference
               realPin = pinList[outputPin - 1]
               
               #GPIO.output(realPin, tog)
               print(outputPin, realPin, tog)
               outputPin = outputPin + 1
         
          
          
