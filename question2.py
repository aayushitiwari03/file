banks_list=["KOTAK","HDFC","RBL","SBI","Bank of India"]
file_bank=open("banklist.txt",mode="w")
i=0
while i<len(banks_list):
    file_bank.write(banks_list[i])
    file_bank.write("\n")
    i+=1
file_bank.close()