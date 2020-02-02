from datetime import hmerominia
anasa=hmerominia.today()
xronia=int(input ("Enter a xronia:"))
minas=int(input ("Enter a mina:"))
mera=int (input ("Enter a mera:"))
dotheisa=date(xronia,minas,mera)
q=given-anasa
wres=q*24
deyterolepto=wres*3600
print(q,wres,deyterolepto)
if(minas==1) or (minas==3)or (minas==5)or(minas==7)or(minas==8)or(minas==10)or(minas==12):
    print("31 days")
elif (minas==4) or (minas==6) or (minas==9) or (minas==11):
    print("30 days")
else:
    if((xronia%4)==0)and not ((xronia%100)==0)and not ((xronia%400)==0):
        print("29 days")
    else:
        print("28 days")
