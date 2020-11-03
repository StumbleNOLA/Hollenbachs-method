import numpy as np
import matplotlib.pyplot as plt
import math as math
import sys as sys

from Hollenbach import *
from ProjectData import *   #This is the data for the project vessel
##from ModelData import *   #This is the data used for the ship in Apendix A


# constants
g=9.807 #m/s^2
rho=1026.021 #density (kg/m^3)
nu=1.1892e-6 #m^2/s
rhoair=1.225 #kn/m^3

#Calculations
#LC Calculation:
if LOS<LPP:
    LC=LOS
elif LOS>1.1*LPP:
    LC=1.0667 * LPP
else:
    LC=LPP+(2/3)*(LOS-LPP)
   

VS=Vskn*1852/3600          #convert knots to m/s
Re =VS*LC/nu               #Reynolds Number
Fr=VS/np.sqrt(g*LWL)       #Freud's Number


#Hollenbach's Method: Assume even keel


#Surface Area coefficent (k)
kd=(S0d+S1d*(LOS/LWL)+S2d*(LWL/LPP)+S3d*CB+S4d*(LPP/B)+S5d*(B/T)+S6d*(LPP/T)+S7d*((Ta-Tf)/LPP)+S8d*(D/T))

#Calculate predicted surface area
Sd=kd*LPP*(B+2*T)           #Sd-Surface Area for design waterline
if SAPP>0:
    SAPPmin=SAPP
    SAPPm=SAPP
else:
    SAPPmin=Sd*(.0280+.010**(-1*((LPP*T)/1000))*Sd) 
    SAPPm=Sd*(.0325+.045**(-((LPP*T)/1000)))



from ResistanceMean import *
from ResistanceMin import *



