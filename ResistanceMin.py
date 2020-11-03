#For mean values append m to the variables
#For design draft
#Assumes 1 shaft



from Hollenbach import *
from ProjectData import *
from Project2 import *

FN=VS/np.sqrt(g*LC)        #Special Freud Number using LC instead of LWL

#1) Frictional Resistance       RFm
CFmin=.075/((np.log10(Re)-2)**2)




#2) Residuary Resistance        RRm
##This is the meat and potatoes of the method


#Correction Factors:
#High Freud Number factor: (kFr, c1b, c1d)
kFrmin=1

#Length Factor:
kLmin=1

#beam-draft ratio factor
if B/T <1.99:
    kBTmin=1.99**a1dmin
else:
    kBTmin=(B/T)**a1dmin

    #Length-beam ration factor:
if LPP/B <=7.11:
    kLBmin=(LPP/B)**a2dmin
else:
    kLBmin=7.11**a2dmin

#wetted length ratio factor:
if LOS/LWL <=1.05:
    kLLmin=(LOS/LWL)**a3dmin
else:
    kLLmin=1.05**a3dmin

#aft overhang ratio 
if LWL/LPP <=1.06:
   kAOmin=(LWL/LPP)**a4dmin 
else:
   kAOmin=1.06**a4dmin

#trim correction factor:
kTrmin=(1+(Ta-Tf)/LPP)**a5dmin

#propeller factor:
if D/Ta<.43:
    kPrmin=.43**a6dmin
elif D/Ta>.84:
    kPrmin=.84
else: 
    kPrmin=(D/Ta)**a6dmin


CRstdmin=b11drr + b12dmin * FN +b13dmin *FN**2+(b21dmin + b22dmin *FN + b23dmin *FN**2)*CB+(b31dmin +b32dmin *FN+ b33dmin *FN**2)*CB**2

    
CRBTmin=CRstdmin * kFrmin * kLmin * kBTmin * kLBmin * kLLmin * kAOmin *kTrmin * kPrmin



CRmin=1000*CRBTmin*(B*T/(10*Sd))





#3) Correlation Allowance       RAm
if LPP<175:
    CAmin=(.35-.002*LPP)*.001
else:
    CAmin=0




#4) Appendage Resistance        RAPPm
k2eqmin=(1+k2i)*SAPPmin

RAPPmin=.5*rho*nu**2*SAPPmin*(k2eqmin)*k2i*CFmin

CDTHmin=.003+.003*(10*dTH/T-1)
RTHmin=rho*VS**2*np.pi*dTH**2*CDTHmin

CAPPmin=(RAPPmin+RTHmin)/(.5*rho*VS**2*Sd)




#5) Environmental Resistance    Renvm
if CDA>0: 
    CDA=CDA                                      #If CDA is available then it retains it
else:
    CDA=.8                                     #If CDA is not available it sets it to .8 as a default

CAASmin=CDA * (rhoair*AVS)/(rho*Sd)                
Cwindmin = 0                                       #Place Holder
Cwavesmin = 0                                      #Place Holder

Cenvmin = CAASmin + Cwindmin + Cwavesmin

CTmin=CFmin+CRmin+CAmin+CAPPmin+Cenvmin

RTmin=.5*rho*VS**2*Sd*CTmin