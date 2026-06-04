import csv

files = ["file1.csv", "file2.csv", "file3.csv"]
output_file = "final_output.csv"

final_rows = []

for file in files:
    with open(file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header

        for row in reader:
            # Step 1: Filter pink morsels
            if row[0].strip().lower() == "pink morsels":
                
                price = float(row[1])
                quantity = float(row[2])
                date = row[3]
                region = row[4]

                # Step 2: Calculate sales
                sales = price * quantity

                # Step 3: Keep only required fields
                final_rows.append([sales, date, region])

# Write final output file
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)

    # Header
    writer.writerow(["Sales", "Date", "Region"])

    # Data
    writer.writerows(final_rows)

print("Final file created successfully ✅")
