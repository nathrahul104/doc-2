mlist=[25,22,15,25,25,22,22,22]
feq={}
for items in mlist:
    if items not in feq:
        feq[items]=mlist.count(items)
for key,values in feq.items():
    print(key," ",values)
    
xxxxxxxxx
