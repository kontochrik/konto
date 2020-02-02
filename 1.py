AP=(input ("enter a text:"))
def replaceOriginal(AP,omae):
    q=['']*omae
    for i in range(omae):
        q[i]=AP[omae-1-i]
        if (AP[i]!= "a" and AP[i]!="e" and AP[i]!= "i" and AP[i]!='o' and AP[i]!="u"):
            print (q[i],end='')
            print()



omae=len(AP)
replaceOriginal(AP,omae)
