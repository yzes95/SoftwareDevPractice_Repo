import csv
# with open("student2.csv") as file:
#     writer= csv.DictReader(file)
#     #writer.writerow({"name": "yahya", "home": "egypt"})
#     #writer.writerow({"name": "asd", "home": "dfg"})
#     for _ in writer:
#         print("not empty")
#     else:
#         print("empty")

try:
    with open("test.txt") as file:
        writer= csv.DictReader(file)
except FileNotFoundError:
    with open("test.txt","a") as file:
        writer= csv.DictWriter(file, fieldnames=["Cycle_No", "Total_Items_Produced", "Total_Working_Hours", \
                                                 "Items_Produced_OP_Mode", "Working_HRS_OP_Mode", \
                                                 "Items_Produced_FP_Mode", "Working_HRS_FP_Mode"])
        #later we will add operator name and number of products producded by each operator
        writer.writeheader()