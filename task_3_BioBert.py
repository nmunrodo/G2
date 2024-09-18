import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import pandas as pd
from tqdm import tqdm

# Load the BioBERT model for NER
model_name = "dmis-lab/biobert-base-cased-v1.1"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

# Initialize the NER pipeline with max_length (accounting for special tokens)
ner_pipeline = pipeline(
    "ner",
    model=model,
    tokenizer=tokenizer,
    aggregation_strategy="simple",
    #truncation=True,
    #max_length=512  # The max length should include the special tokens added by the tokenizer
)


# Function to read file in chunks
def read_in_chunks(file_object, chunk_size=1024):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


# Function to extract drugs and diseases using BioBERT NER
def extract_entities(text_chunk):
    # Tokenize the input chunk to ensure proper truncation
    tokenized_input = tokenizer(text_chunk, truncation=True, max_length=512, return_tensors="pt")

    truncated_text = tokenizer.decode(tokenized_input["input_ids"][0], skip_special_tokens=True)
    # Run the NER pipeline on the truncated tokenized input
    ner_results = ner_pipeline(truncated_text)

    drugs = []
    diseases = []

    for entity in ner_results:
        entity_group = entity.get('entity_group','').lower()
        if "drug" in entity_group:
            drugs.append(entity['word'])
        elif "disease" in entity_group:
            diseases.append(entity['word'])

    return drugs, diseases


# Read the source text file in chunks and process it
source_file = "medic_text.txt"
drugs_list = []
diseases_list = []

with open(source_file, "r", encoding="utf-8") as file:
    for chunk in tqdm(read_in_chunks(file, chunk_size=4096)):
        drugs, diseases = extract_entities(chunk)
        drugs_list.extend(drugs)
        diseases_list.extend(diseases)

# Count the occurrences of each drug and disease
drugs_count = pd.Series(drugs_list).value_counts()
diseases_count = pd.Series(diseases_list).value_counts()

# Create a DataFrame with the results
df_drugs = pd.DataFrame(drugs_count, columns=["count"]).reset_index().rename(columns={"index": "drug"})
df_diseases = pd.DataFrame(diseases_count, columns=["count"]).reset_index().rename(columns={"index": "disease"})

# Save the results to CSV
df_drugs.to_csv("extracted_drugs.csv", index=False)
df_diseases.to_csv("extracted_diseases.csv", index=False)

print("Entities extracted and saved to CSV files.")
