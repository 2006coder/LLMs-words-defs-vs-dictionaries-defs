import google.generativeai as genai
import csv
genai.configure(api_key="your api key")
model = genai.GenerativeModel("gemini-1.5-flash")
import time

# Read the input CSV file
with open('1000.csv', mode='r', newline='') as infile:
    reader = csv.reader(infile)
    rows = list(reader)  # Read all rows into a list


check = 1 #this variable shows us how many words that are successfully got the definitions.
# Process each row and update the second column
for row in rows:
    if row:  # Check if the row is not empty
        word = row[0]
        if len(row) > 1 and row[2] !="N/A" and row[2]:  # Skip if the second column already has a definition
            print(f"Skipping {word}, already has a definition.")
            continue
        print()
        print()
        print()
        print(word)
        definition = ""
        count = 0
        while definition == "" and count < 4:
            print("attempt", count + 1)
            try:
                definition = str((model.generate_content("Define this word: " + word + ".")).text)
            except:
                pass
            count = count + 1
            time.sleep(2)
            if count == 3:
                definition = "N/A"

        print(definition)
        if len(row) > 1:
            row[2] = definition  # Update the second column if it exists
        else:
            row.append(definition)  # Add the definition if the second column does not exist
        print("successful! " + str(check))
        check = check + 1
    time.sleep(2)
    if check % 10 == 0:
        time.sleep(3)

# Write output back to the csv file again.
with open('1000.csv', mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(rows)


#github: 2006coder