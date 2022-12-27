lsteven=[]
lstodd=[]
while(True):
    
    n=int(input("enter a value(-1 to end):"))
    if n==-1:
        break
    elif n%2==0:
        lsteven.append(n)
    elif
    n%2==1:
        lstodd.append(n)
        
print("even:",*lsteven)
print("min:",min(lsteven))
print("max:",max(lsteven))
print("avg:",round(sum(lsteven)/len(lsteven),1))

        
print("odd:",*lstodd)
print("min:",min(lstodd))
print("max:",max(lstodd))
print("avg:",round(sum(lstodd)/len(lstodd),1))
