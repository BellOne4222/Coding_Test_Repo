def Betal(fck):
    if fck <= 28.0:
        betal = 0.85
    elif fck > 28.0:
        betal = 0.85 - 0.007 * (fck - 28.0)
        
    if betal < 0.65:
        betal = 0.65
    return betal
      

# Strength Reduction Factor, et
def Strength_Reduction_Factor(et):
   if et >= 0.005 :
      phi = 0.85
   elif et < 0.002 :
      phi = 0.65
   else :
      phi = 0.65 +( et - 0.002 ) * ( 0.2 / 0.003 )
   return phi



def Dbeam(fy, fck, b, d, dt, As, Asp, dp) :
   #design flexura1 strength of singly reinforced concrete beam (MPa,mm) 

   #return (pMn, Mn, phi, et, c, a)

   # nominal flexural strength
   
   a = ( As - Asp ) * fy / (0.85 * fck * b)
   # assumtions : fck <= 40mpa
   b1 = 0.8
   c = a / b1
   Es = 0.0033 * ( c - dp ) / c

   if Es > 0.002:
      Mn = ( Asp * fy * ( d - dp ) + ( As - Asp ) * fy * ( d - a/2)) * 1E-6 
   else:
      x = 0.85 * fck * b
      y = 0.0033 * 200000 * Asp - As * fy
      z = -0.0033 * 200000 * Asp * b1 * dp
      a = (-y+(y**2 - 4 * x  * z)**0.5) / (2 * x)
      fs = Es * 200000
      Mn = ( 0.85 * fck * a * b *(d-a/2) + Asp * fs * (d- a/2) ) * 1E-6

    # check the extreme tensile strain(=et)

   et = 0.0033 * ( dt-c ) / c
   if et < 0.004:
      Mn = 0.0
   
   phi = Strength_Reduction_Factor(et)

   # design strength
   pMn = phi * Mn

   #check minimum reinforcement
   fr = 0.63 * (fck**0.5)
   h = dt + 60
   Ig = b * h**3 / 12
   yt = h /2
   Mcr = fr * Ig / yt * 1E-6
   if pMn < 1.2 * Mcr:
      Mn = pMn = 0.0

   # return analysis results
   return pMn, Mn, phi ,et, c, a   

D22 = 387.1
D25 = 566.7
D29 = 642.6

D1 = [400, 24, 400, 515, 540, 8*D25, 2*D22, 60]
D2 = [400, 27, 400, 710, 740, 8*D22, 2*D22, 60]
D3 = [300, 21, 400, 515, 540, 8*D22, 2*D22, 60]
D4_2 = [400, 21, 300, 515, 540, 387.1*8, 387.1*2, 60]
D4_3 = [400, 21 ,300, 515, 540, 387.1*8, 387.1*4,60]

Dlist = [D1,D2,D3,D4_2,D4_3]

for i in range(len(Dlist)):
   fy, fck, b, d, dt, As, Asp, dp = Dlist[i][0], Dlist[i][1], Dlist[i][2], Dlist[i][3], Dlist[i][4], Dlist[i][5], Dlist[i][6], Dlist[i][7]
   pMn, Mn, phi, et, c, a = Dbeam(fy, fck, b, d, dt, As, Asp, dp)
   print(f'[Dbeam] a={a:6.1f} mm, c={c:6.1f}mm,et={et: 7.4f},Mn={Mn:6.1f}kN.m, phi={phi: 6.3f},pMn={pMn:6.1f}kN.m')

