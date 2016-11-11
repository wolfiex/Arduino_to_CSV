import pylab  as plt
import pandas as pd
import numpy  as np
import serial,os,wx


#pip install pyserial

global myport


def getport():
    global myport
    ports = os.popen('ls /dev/tty.*').read().split('\n')
    for i in ports: 
	    if 'usb' in i:
		    myport = i
		    print 'selecting', myport
		    
		
		



#def parse_input(inp)				    
    
		 
		 
		 
		 
		 
		 



class Board (object):
    
    def __init__(self, number):
        self.no =  number
        self.data = []
        
    def append(self,string):
        self.data.append(string.split(',')[1:])
             
    def to_pandas(self):
        self.df = pd.DataFrame( self.data , columns=['Sensor1','Sensor2','Sensor3','Sensor3','Sensor4','Sensor5','Sensor6','Sensor7','Sensor8']) 
        
    
    


def go(): 
    print 'ggoogogoogogog'

from wx.lib.plot import PolyLine, PlotCanvas, PlotGraphics
 





import sys
sys.exit()


for i in xrange(8): 
    exec ('global Board%i'%i)
    exec ("Board%i = pd.DataFrame(columns=['Sensor1','Sensor2','Sensor3','Sensor3','Sensor4','Sensor5','Sensor6','Sensor7','Sensor8'])"%i)
    
    
    




		    
		
ser = serial.Serial(myport, 9600)
		
myfile =  open("test.txt", "a") 



while running == True: 
	data=ser.readline()
	myfile.write(data)
	print data	





X = np.linspace(0,2,1000)
Y = X**2 + np.random.random(X.shape)

plt.ion()
graph = plt.plot(X,Y)[0]

while True:
    Y = X**2 + np.random.random(X.shape)
    graph.set_ydata(Y)
    plt.draw()
    
    
    
    
'''
Board0,0.00003504,0.00000000,0.00001594,0.00001801,0.00002674,0.00002235,0.00002411,0.00002529
Board1,0.00003908,0.00000000,0.00002754,0.00000000,0.00001338,0.00003560,0.00001473,0.00002125
Board2,0.00000000,0.00001838,0.00000000,0.00000000,0.00000000,0.00000000,0.00000000,0.00002529

Board0,0.00003510,0.00000000,0.00001596,0.00001804,0.00002679,0.00002239,0.00002414,0.00002533
Board1,0.00003914,0.00000000,0.00002758,0.00000001,0.00001340,0.00003565,0.00001476,0.00002129
Board2,0.00000001,0.00001841,0.00000000,0.00000000,0.00000000,0.00000000,0.00000000,0.00002533
'''    

