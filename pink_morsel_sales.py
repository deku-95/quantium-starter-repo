import csv
#Create a list of files to open
files = ['data/daily_sales_data_0.csv', 'data/daily_sales_data_1.csv', 'data/daily_sales_data_2.csv']
writer = csv.writer(open('data/output.csv', 'w', newline=''))
# Write Sales, Date and Region on Top
writer.writerow(['Sales', 'Date', 'Region'])
#For each file will write the data into the output file
for file in files:
    reader = csv.reader(open(file, 'r'))
    for row in reader:
        # Only get the product called pink morsel
        if row[0] == 'pink morsel':  
        # Then write the rest of the data. Also multiply the price by the quantity in a new variable called "sales"
            sales = round(float(row[1][1:]) * int(row[2]), 2)
            writer.writerow([sales, row[3], row[4]])
