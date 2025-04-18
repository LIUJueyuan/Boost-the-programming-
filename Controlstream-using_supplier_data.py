import pandas as pd
# Read the CSV file into a DataFrame
df = pd.read_csv("D:/Personal/study/CS/Python Seminar/github clone/Boost-the-programming-/supplier_data.csv")
print(df.head(3))
# Convert the DataFrame to a list of dictionaries
# Each dictionary represents a row in the DataFrame
records = df.to_dict(orient='records')
# Print the first two records to verify the conversion
print(records[:2])
# Initialize an empty dictionary to store the counts of each supplier
supplier_counts = {}
for record in records:
    supplier = record['Supplier Name']
    if supplier not in supplier_counts:
        supplier_counts[supplier] = 1 # Initialize count to 1 for new suppliers
    else:
        supplier_counts[supplier] += 1 # Increment the count for existing suppliers
# Print the counts of each supplier 
print(supplier_counts)

for record in records:
    cost_str = record['Cost'].replace('$', '') # Remove the dollar sign from the cost string
    cost_str = cost_str.replace(',', '') # Remove commas from the cost string
    cost = float(cost_str) # Convert the cleaned string to a float
    if cost > 500 :
        print(record)

for record in records :
    if '2002' in record['Purchase Date']:
        print(record)

part_total_cost ={}
for record in records :
    part = record['Part Number']
    cost = float(record['Cost'].replace('$', '').replace(',', ''))
    if part not in part_total_cost:
        part_total_cost[part] = cost # Initialize cost for new parts
    else:
        part_total_cost[part] += cost # Increment cost for existing parts
# Print the total cost for each part    
print(part_total_cost)

i=0
while i < len(records) :
    cost = float(records[i]['Cost'].replace('$', '').replace(',', ''))
    if cost > 500 :
        print("find one",records[i])
        break
    i += 1
print("end")

seen = set()
for record in records:
    key = tuple(record.items())
    if key in seen:
        pass  # 什么都不做
    else:
        print("新记录：", record)
        seen.add(key)