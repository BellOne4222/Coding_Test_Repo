count=int(input())

n=input()

l=[]

for j in range(count*2+3):

    l.append([])



for i in range(len(n)):

    if (n[i] in ['0','2','3','5','6','7','8','9']):

        l[0].append(" "+count*"-"+" ")

    else:

        l[0].append(" "+count*" "+" ")	#뚜껑

	

    if (n[i] in ['0','4','8','9']):

        for k in range(1,count+1):

            l[k].append("|"+count*" "+"|")

    elif (n[i] in ['5','6']):

        for k in range(1,count+1):

            l[k].append("|"+count*" "+" ")

    else:

        for k in range(1,count+1):

            l[k].append(" "+count*" "+"|")	#위쪽 양옆

	#중간
    if (n[i] in ['0','1','7']):
    	l[count+1].append(" "*(count+2))
    else:
        l[count+1].append(" "+"-"*count+" ")
			

    if(n[i] in ['0','6','8']):	

        for k in range(count+2,2*count+2):

            l[k].append("|"+count*" "+"|")

    elif(n[i]=='2'):

        for k in range(count+2,2*count+2):

            l[k].append("|"+count*" "+" ")

    else:

        for k in range(count+2,2*count+2):

            l[k].append(" "+count*" "+"|")	#아래 양옆

		 

    if(n[i] in ['0','2','3','5','6','8','9']):		

        l[-1].append(" "+count*"-"+" ")

    else:

        l[-1].append(" "+count*" "+" ")	#바닥

		 

for k in l:

	print(" ".join(k))