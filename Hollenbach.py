#Hollenbach variables and coefficients

import numpy as np
iobase = 'shipex'

from ProjectData import *   #This is the data for the project vessel

#Placeholders entered but not used yet
#AV=1            #Transverse verticle area above waterline
#NR=1            #Number of rudders (1-2)
#NB=1            #Number of shaft brackets (0-2)
#NT=1            #Number of side thrusters (0-4)
#SAPP=1          #Wetted surface area of appendages


#Hollenbach's method coefficients
S0d=-.6837
S1d=.2771
S2d=.6542
S3d=.6422
S4d=.0075
S5d=.0275
S6d=-.0045
S7d=-.4798
S8d=.0376

S0b=.8037
S1b=.2726
S2b=.7133
S3b=.6699
S4b=.0243
S5b=.0265
S6b=-.0061
S7b=.2349
S8b=.0131

#Hollenbach method - Coefficents of the standard residuary resistance:
#single screw:        
#design draft:
#mean:
b11dm = -.57424
b12dm = 13.3893
b13dm = 90.596
b21dm = 4.6614
b22dm = -39.721
b23dm = -351.483
b31dm = -1.14215
b32dm = -12.3296
b33dm = 459.254
#min
b11dmin = -.91424
b12dmin = 13.3893
b13dmin = 90.596
b21dmin = 4.6614
b22dmin = -39.721
b23dmin = -351.483
b31dmin = -1.14215
b32dmin = -12.3296
b33dmin = 459.254



if CB<.49:
    b11drr=.49
elif CB>.6:b11drr=-.57424
else: 
    b11drr=-.57424-25*((.06-CB)**2)


#Coefficents for correction factors of the dstandard RR coefficents in Hollenbach's method:
#mean RR:
#single screw:
#design draft:
#mean:
a1dm=.3382
a2dm=-.8086
a3dm=-6.0258
a4dm=-3.5632
a5dm=9.4405
a6dm=.0146
a7dm=0
a8dm=0
a9dm=0
a10dm=0



d1dm=.854
d2dm=-1.228
d3dm=.497

e1dm=2.1701
e2dm=-.1602

#min:
a1dmin=.3382
a2dmin=-.8086
a3dmin=-6.0258
a4dmin=-3.5632
a5dmin=0
a6dmin=0
a7dmin=0
a8dmin=0
a9dmin=0
a10dmin=0

c1dmin=0

d1dmin=0
d2dmin=0
d3dmin=0

e1dmin=1
e2dmin=0



# Factors for the lower and upper limit of the range of Froude numbers where CR are valid
#mean RR:
#Single Screw:
#Design Draft:
f1d=.17
f2d=.2
f3d=.6

g1d=.642
g2d=-.635
g3d=.150
