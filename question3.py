list=["reeshubh - meerut","imtiyaz - delhi","nilima - cochin","rati - shimla","ayishah - delhi",
"raghu - shimla","naseer - kanpur","karthikyan - delhi","salma - jaipur","pankaj -delhi",
"brijesh - delhi","govind - delhi", "puneet - shimla","sidhhi - delhi","suman - jaipur",
"rajiv - shimla","mohindar - delhi","rajendra - jaipur","priyanka - shimla","neela - delhi", ]
file=open("name & state.txt","w")
i=0
while i<len(list):
    file.write(list[i])
    file.write("\n")
    i+=1
file.close()

file=open("name & state.txt","r")
for i in (file):
    if "delhi" in i :
        file2= open("delhi.txt","a")
        file2.write(i)
    elif "shimla" in i :
        file3=open("shimla.txt","a")
        file3.write(i)
    else:
        file4=open("others.txt","a")
        file4.write(i)
file.close()