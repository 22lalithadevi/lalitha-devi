gene=int(input("enter no of patients: "))
list=[]
gene_list=[]
for i in range(gene):
    temp=float(input(f"enter the patient {i} data: "))
    list.append(temp)
for  temp in list:
    if i<5:
        gene_list.append("Underexpressed")
    elif i>=5 and i<=15:
        gene_list.append("Normal")
    else:
        gene_list.append("Overexpressed")
print(gene_list)