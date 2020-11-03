from ProjectData import LPP, B, T, D, CB, V


#Permissable Range of primary dimensions for Hollenbach's method
Vhmax=1             #displacement range 
LPPhmin=42          #Min LPP
LPPhmax=205         #max LPP
LPP_Bhmin=4.71      #Min length to beam ratio
LPP_Bhmax=7.11      #max length to beam ratio
B_Thmin=1.99        #min beam to draft ratio
B_Thmax=4.00        #maximum beam to draft ratio
D_Thmin=.43        #min prop diameter-draft ratio
D_Thmax=.84        #Max pop diameter-draft ratio
CBhmin=.60          #Min block coefficent
CBhmax=.83          #Max block coeffience ratio

LPP_V3min=4.49      #Min length-displacement ratio LPP/ cuberoot volume
LPP_V3hmax=6.01      #Min length-displacement ratio LPP/ cuberoot volume




print ("")
print ("")
#print("Conformity of proposed vessel with Hollenbach's Method Test")

#min/max LPP test
minmaxtest=0
#LPP inside range
if LPP>=LPPhmin and LPP<=LPPhmax:
    #print("LPP inside range")
    pass
else:
    print("LPP outside range")
    print ("LPP Range", LPPhmin, "to", LPPhmax, "LPP is", LPP)
    minmaxtest=minmaxtest+1
    
#min/max LPP/B test
if LPP/B>=LPP_Bhmin and LPP/B<=LPP_Bhmax:
    #print("LPP/B inside range")
    pass
else:
    print("LPP/B outside range")
    print ("LPP/B Range", LPP_Bhmin, "to", LPP_Bhmax, "LPP/B is", LPP/B)
    minmaxtest=minmaxtest+1

#min/max B/T test
if B/T>=B_Thmin and B/T<=B_Thmax:
    #print("B/T inside range")
    pass
else:
    print("B/T outside range")
    print ("B/T Range", B_Thmin, "to", B_Thmax, "B/T is", B/T)
    minmaxtest=minmaxtest+1

#min/max Prop Diameter / draft test
if D/T>=D_Thmin and D/T<=D_Thmax:
    #print("Prop Diameter/Draft inside range")
    pass
else:
    print("Prop Diameter/Draft outside range")
    print ("Prop Diameter/Draft Range", D_Thmin, "to", D_Thmax, "D/T is", D/T)
    minmaxtest=minmaxtest+1

#min/max Block Coefficent test
if CB>=CBhmin and CB<=CBhmax:
    #print("CB inside range")
    pass
else:
    print("CB outside range")
    print ("CB Range", CBhmin, "to", CBhmax, "CB is", CB)
    minmaxtest=minmaxtest+1

#min/max LPP/VOL test
if LPP/V**(1/3)>=LPP_V3min and LPP/V**(1/3)<=LPP_V3hmax:
    #print("Length-Displacement inside range")
    pass
else:
     print("Length-Displacement outside range")
     print ("L-D Range", LPP_V3min, "to", LPP_V3hmax, "L-D is", LPP/V**(1/3))
     minmaxtest=minmaxtest+1


if minmaxtest==0:
    print("The proposed vessel conforms to the requirements to be analyzed by Hollenbach's method")
else:
    print("The proposed vessel does not conform to the requirements to be analyzed by Hollenbach's method")

