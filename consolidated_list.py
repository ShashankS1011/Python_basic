s1=[100,200,300,350,650,750,830,906,1100]
s2=[20,23,32,35,45,80,90,100,250]
s3=[]
c=0
d=0
while c<len(s1) and d<len(s2):
    if(s1[c]>s2[d]):
        s3.append(s2[d])
        d=d+1
    elif(s1[c]<s2[d]):
        s3.append(s1[c])
        c+=1
while c<len(s1):
    s3.append(s1[c])
    c+=1
while d<len(s2):
    s3.append(s2[d])
    d+=1
print("Consolidated list:",s3)