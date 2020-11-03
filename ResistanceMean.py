#For mean values append m to the variables
#For design draft
#Assumes 1 shaft


import numpy as np
from Hollenbach import *
from ProjectData import *
from Project2 import *

FN=VS/np.sqrt(g*LC)        #Special Freud Number using LC instead of LWL



#1) Frictional Resistance       RFm
CFm=.075/((np.log10(Re)-2)**2)




#2) Residuary Resistance        RRm
##This is the meat and potatoes of the method


#Correction Factors:
#High Freud Number factor: (kFrm)
Frcrit = d1dm+d2dm*CB+d3dm*CB**2

c1dm=FN/Frcrit

kFrm = np.ones_like(FN)
greater_than_vals = (FN / Frcrit) ** c1dm
kFrm[FN >= Frcrit] = greater_than_vals[FN >= Frcrit]



#np.where(FN<Frcrit[kFrm=1,kFrm=(FN/Frcrit)**c1dm])

#Previous attempt at finding kFrm
#if FN<Frcrit:
#    kFrm=1
#else:
#    kFrm=(FN/Frcrit)**c1dm



c1b=10*CB*(FN/Frcrit - 1)    #line 138
c1d=(FN/Frcrit)    #line 97

    #Length Factor:
kLm=e1dm * LPP**e2dm                #here the divide by meters is excluded but implied

    #beam-draft ratio factor
if B/T <1.99:
    kBTm=1.99**a1dm
else:
    kBTm=(B/T)**a1dm

    #Length-beam ration factor:
if LPP/B <=7.11:
    kLBm=(LPP/B)**a2dm
else:
    kLBm=7.11**a2dm

    #wetted length ratio factor:
if LOS/LWL <=1.05:
    kLLm=(LOS/LWL)**a3dm
else:
    kLLm=1.05**a3dm

    #aft overhang ratio 
if LWL/LPP <=1.06:
   kAOm=(LWL/LPP)**a4dm 
else:
   kAOm=1.06**a4dm

    #trim correction factor:
kTrm=(1+(Ta-Tf)/LPP)**a5dm

    #propeller factor:
if D/Ta<.43:
    kPrm=.43**a6dm
elif D/Ta>.84:
    kPrm=.84
else: 
    kPrm=(D/Ta)**a6dm


CRstdm=b11drr + b12dm * FN +b13dm *FN**2+(b21dm + b22dm *FN + b23dm *FN**2)*CB+(b31dm +b32dm *FN+ b33dm *FN**2)*CB**2

    
CRBTm=CRstdm * kFrm * kLm * kBTm * kLBm * kLLm * kAOm *kTrm * kPrm

CRm=1000*CRBTm*(B*T/(10*Sd))









#3) Correlation Allowance       RAm
if LPP<175:
    CAm=(.35-.002*LPP)*.001
else:
    CAm=0




#4) Appendage Resistance        RAPPm
k2eqm=(1+k2i)*SAPPm

RAPPm=.5*rho*nu**2*SAPPm*(k2eqm)*k2i*CFm

CDTHm=.003+.003*(10*dTH/T-1)
RTHm=rho*VS**2*np.pi*dTH**2*CDTHm

CAPPm=(RAPPm+RTHm)/(.5*rho*VS**2*Sd)






#5) Environmental Resistance    Renvm
if CDA>0: 
    CDA=CDA                                      #If CDA is available then it retains it
else:
    CDA=.8                                     #If CDA is not available it sets it to .8 as a default

CAASm=CDA * (rhoair*AVS)/(rho*Sd)                
Cwindm = 0                                       #Place Holder
Cwavesm = 0                                      #Place Holder

Cenvm = CAASm + Cwindm + Cwavesm

#Total Resistance
CTm=CFm+CRm+CAm+CAPPm+Cenvm

RTm=.5*rho*VS**2*Sd*CTm