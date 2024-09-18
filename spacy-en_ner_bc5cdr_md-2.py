import spacy
import pandas as pd
from collections import Counter

# Load the model (adjust the model name if necessary)
nlp = spacy.load("en_ner_bc5cdr_md")  # or "en_ner_bc5cdr_md"


# Function to extract diseases and drugs entities
def extract_entities(text):
    doc = nlp(text)
    diseases = []
    drugs = []

    for ent in doc.ents:
        if ent.label_ == "DISEASE":  # Check this label according to your model
            diseases.append(ent.text)
        elif ent.label_ == "CHEMICAL":  # Check this label according to your model
            drugs.append(ent.text)

    return diseases, drugs


# Read the input text file
with open('medic_text.txt', 'r') as file:
    text = file.read()

# Split text into smaller chunks (e.g., 100,000 characters each) if needed
chunk_size = 100000  # Adjust the size based on your memory limits
chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

all_diseases = []
all_drugs = []

# Process each chunk separately
for chunk in chunks:
    diseases, drugs = extract_entities(chunk)
    all_diseases.extend(diseases)
    all_drugs.extend(drugs)

# Count occurrences of each disease
disease_counts = Counter(all_diseases)
drug_counts = Counter(all_drugs)

# Create a DataFrame for diseases
disease_data = pd.DataFrame(disease_counts.items(), columns=['Disease', 'Count'])

# Create a DataFrame for drugs
drug_data = pd.DataFrame(drug_counts.items(), columns=['Drug', 'Count'])

# Create a DataFrame with total counts
total_count = len(all_diseases) + len(all_drugs)
total_data = pd.DataFrame([{'Type': 'Total', 'Count': total_count}])

# Save the DataFrames to CSV files
disease_data.to_csv('diseases_counts.csv', index=False)
drug_data.to_csv('drugs_counts.csv', index=False)
total_data.to_csv('total_counts.csv', index=False)

print("Entities have been counted and saved to CSV files.")
