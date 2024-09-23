from sentence_transformers import SentenceTransformer
import csv


mpnet_model = SentenceTransformer('all-mpnet-base-v2')
vectors_from_texts = []


#open the csv file
with open('10000.csv', mode='r', newline='') as infile:
    reader = csv.reader(infile)
    rows = list(reader)  # Read all rows into a list

for row in rows:
    if row: #skip the empty rows
        definition_1 = row[1] #get the definitions generated by Gemini using the prompt: "What is the meaning of this word: [word]?"
        definition_2 = row[2] #get the definitions generated by Gemini using the prompt: "Define this word: [word]."
        embeddings_1 = mpnet_model.encode(definition_1) #extract the embeddings
        embeddings_2 = mpnet_model.encode(definition_2) #extract the embeddings
        #print(embeddings_1)
        print(len(embeddings_1))
        print(len(embeddings_2))
        row[3] = embeddings_1
        row[4] = embeddings_2

#write the output back into the file
with open('10000.csv', mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(rows)


#Github: 2006coder






