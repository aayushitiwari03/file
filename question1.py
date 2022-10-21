list=["priyanak - shimla","neela - delhi","sashi - jaipur","sarika - delhi","dipti - shimla",
"harshad - delhi ","trishna - delhi ","pradeep - delhi","sekhar - delhi","nand - delhi",
"annop - delhi","balwindar - jaipur"]
f=open("people2.trt","w")
i=0
c=0
while i<len(list):
    f.write(list[i])
    f.write("\n")
    c+=1
    i+=1
print(c)
f.close()

