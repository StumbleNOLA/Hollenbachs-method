#Ship Data for the Project
#
import numpy as np
iobase = 'shipex'

# General ship properties 
LPP=162.4       #Length between perpendiculars (m)
LWL=167.21      #Length on the waterline (m)
LOS=172.90      #Length over wetted surface (m)
B=24.8          #Beam (m)
T=9.6           #Draft (m)
V=28201.0       #displacement m^3
SBK=50          #wetted surface area of bilge keels (m^2)
AVS=508.80      #Transverse area above the waterline (m^2)
ABT=24          #Bulbous bow cross section area at FP (m^2)
dTH=1.2         #diameter of bow thruster tunnel (m)
D=6.693         #Propeller diameter (m)
PD=.9421        #Pitch-diameter ratio
AEAO=.6431      #expanded area ratio
Z=5             #number of propeller blades

#Ship speeds
Vser=18        #Ship Service Speed (knots)
Vl=15          #Ship speed to consider (lower bound)
Vh=20          #Ship speed to consider (upper bound)
Vskn=np.linspace(Vl,Vh, num=int ((Vh-Vl)*2+1))


#Parameters for Hollenbach's method
Ta=T          #molded draft at aft perpendicular change this if not on even keel
Tf=T          #molded draft at aft perpendicular change this if not on even keel
CB=V/(B*T*LPP)  #Block coefficient based on LPP


#Additional values needed
k2i = .4        #Computed by hand from the k2 table
SAPP =0         #Surface Area of projections = 0 unless given
CDA = 0         #Air Drag coefficent = 0 unless given