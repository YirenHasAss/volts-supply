import X9C103_BCM as pot

#Setting pins - note the BCM board numbering convention has been used.
CS = 16
INC = 20
UD = 21
key = 1
#Setup the GPIO inputs/outputs on the Raspberry Pi
pot.initiate(CS,INC,UD)

#Activate the pot for receiving wiper move instructions
pot.activate(CS,INC,UD)

#Set the wiper to move up
#moving wiper up = 1, moving wiper down = 0
#for flag = 1, each step will increase 0.05 volts. Otherwise, it will decrease 0.05 volts.

while key == 1:
    flag = input("input your flag ( To increase volts : 1, to decrease volts : 0 ) : ")
    volts = input("input the voltage you want to supply : ")
    steps = volts/0.05

    pot.wiperset(CS,INC,UD,flag)
    pot.wipermove(CS,INC,UD,steps)
    key = input("input 1 to adjust volts, 0 to disconnect : ")

pot.disconnect(CS,INC,UD)


