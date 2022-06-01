#https://github.com/josipk/MicroBit_WS_Python
import sys, os
import serial as ser
import matplotlib.pyplot as plt
import numpy as np

def main():

	s1 = ser.Serial('/dev/ttyACM0', 115200)
	plt.close('all')
	#plt.figure()
	figure, axis = plt.subplots(2, 2)
	plt.ion()
	plt.show()


	temp1 = np.array([]);
	temp2 = np.array([]);
	hum2 = np.array([]);
	air = np.array([]);

	while True:
		a1 = s1.readline()
		a1 = a1.decode('utf-8')
		b1 = a1.split(",")
		if(len(b1) > 3 and b1[0] == "0"): 
			print(b1)

			try:
				temp1 = np.append(temp1, float(b1[1]))
				temp2 = np.append(temp2, float(b1[2]))	
				hum2 = np.append(hum2, float(b1[3]))	
				air = np.append(air, float(b1[4]))						
			
				if len(temp1) > 200:
					temp1 = temp1[1:]
					temp2 = temp2[1:]
					hum2 = hum2[1:]
					air = air[1:]

				x=np.arange(0, len(temp1))
							
				#plt.cla()
				#plt.ylim(0, 100)
				#plt.plot(x, data, color='r',)
				#plt.plot(x, data2, color='g',)
				
				axis[0, 0].clear()
				axis[0, 0].plot(x, temp1)
				axis[0, 0].set_title("Temperature 1")
		  
				axis[0, 1].clear()
				axis[0, 1].plot(x, temp2)
				axis[0, 1].set_title("Temperature 2")
				  
				axis[1, 0].clear()
				axis[1, 0].plot(x, hum2)
				axis[1, 0].set_title("Humidity")
				  
				axis[1, 1].clear()
				axis[1, 1].plot(x, air)		
				axis[1, 1].set_title("AIR")


				axis[0, 0].set_ylim([-20, 80])
				axis[0, 1].set_ylim([0, 60])
				axis[1, 0].set_ylim([0, 100])
				axis[1, 1].set_ylim([200, 1050])

				
				plt.pause(0.01)
			except KeyboardInterrupt:
				print("Bye")
				sys.exit()
			except:
				pass

	s1.close()	



if __name__ == '__main__':
    print('start')
    main()
    print('exit')


