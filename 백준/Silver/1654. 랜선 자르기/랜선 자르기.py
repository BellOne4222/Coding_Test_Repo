import sys

k,n = map(int,sys.stdin.readline().split())

cables = []
for _ in range(k):
    cable = int(sys.stdin.readline().rstrip())
    cables.append(cable)

cables = sorted(cables) # [457, 539, 743, 802]

nCable = 1
mCable = max(cables)

while nCable <= mCable:
    dCable = (mCable + nCable) // 2
    cableCnt = 0

    for i in range(len(cables)):
        cableCnt += cables[i] // dCable 
    
    if cableCnt < n:
        mCable = dCable -1
    elif cableCnt >= n:
        nCable = dCable + 1

print(mCable)