# Strength Reduction Factor, et
def Check_maximum_reinforcement(et):
    
    #Check maximum reinforcement
    if et < 0.004:
        print("Error: The given section not a beam!")
        phi = 0.0
    elif et < 0.005:
        phi = 0.65 + (et-0.002)*200/3
    else:
        phi = 0.85
    return phi


def TBeam(fy, fck, bw, d, dt, As, b, hf):
    # nominal flexural strength
    a = As * fy / (0.85 * fck * b)
    
    b1 = 0.8
    
    c = a / b1
    
    if a < hf:
        Mn = As * fy * (d - a/2) * 1E-6
    else:
        Asf = 0.85* fck *(b - bw) * hf / fy
        a = (As - Asf) * fy / (0.85 * fck * bw)
        Mn = (Asf * fy * (d - hf/2) + (As - Asf) * fy * (d - a/2)) * 1E-6

    et = 0.0033 * ( dt-c ) / c
    
    phi = Check_maximum_reinforcement(et)
    
    #Check maximum reinforcement
    fr = 0.63 * (fck**0.5)
    h = dt + 60
    yt = (b * hf* (h-hf/2) + bw *(h - hf)**2 / 2) / (b* hf + bw * (h - hf))
    Ig = b * (hf**3) / 12 + b * hf * (h - hf / 2 - yt)**2 + bw * (h - hf)**3 /12 + bw * (h - hf) * (yt - h / 2 + hf/2)**2 
    Mcr = fr * Ig / yt * 1E-6
    
    # design strength
    pMn = phi * Mn
    
    if pMn < 1.2 * Mcr:
        Mn = pMn = 0.0

    return pMn,Mn,phi,et,c,a,yt,Ig,Mcr



D22 = 387.1
D25 = 506.7
D29 = 642.6

T1 = [400, 27, 400, 515, 540, 8*D25, 900, 150]
T2 = [400, 21, 300, 415, 440, 8*D25, 700, 120]
T3 = [400, 21, 300, 415, 440, 8*D22, 700, 120]
T4_5 = [400, 21, 300, 510, 540, 8*D25, 600, 120]


Tlist = [T1,T2,T3,T4_5]
for i in range(len(Tlist)):
   fy, fck, bw, d, dt, As, b, hf = Tlist[i][0], Tlist[i][1], Tlist[i][2], Tlist[i][3], Tlist[i][4], Tlist[i][5], Tlist[i][6], Tlist[i][7]
   pMn,Mn,phi,et,c,a,yt,Ig,Mcr = TBeam(fy, fck, bw, d, dt, As, b, hf)
   print(f'[Dbeam] a = {a:.1f} mm, c = {c:.1f}mm, et = {et:.4f}, Mn = {Mn:.1f}kN.m, phi = {phi:.1f}, pMn = {pMn:.1f}kN.m, Mcr = {Mcr:.1f}kN.m')