import spacy as sp
import scispacy as scsp
from collections import Counter
import pandas as pd

# <link to your team's Github group>
# Load the SciSpacy model for processing medical text
nlp = sp.load("en_core_sci_lg-0.5.4\en_core_sci_lg-0.5.4\en_core_sci_lg\en_core_sci_lg-0.5.4")
#nlp.max_length = 140737148 # or higher
def extract_medical_terms(text):
    # Process the text using SciSpacy model
    doc = nlp(text)
    
    # Extract medical entities (terms)
    medical_terms = [ent.text for ent in doc.ents]
    
    return medical_terms

def count_word_occurrences(terms):
    # Count occurrences of each term
    term_counts = Counter(terms)
    
    return term_counts

def read_text_file(file_path):
    # Read the text file
    chunk_size = 1024  # Number of bytes to read at a time

    with open(file_path, 'r') as file:
        while True:
            thetext = file.readlines(chunk_size)
            if not thetext:
                break
            for line in thetext:
                # Process each line
                text = line
                print(text)
    return text

def save_to_csv(term_counts, output_file):
    # Convert the counter to a pandas dataframe
    df = pd.DataFrame(term_counts.items(), columns=['Term', 'Count'])
    
    # Save the dataframe to a CSV file
    df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    # Specify file paths
    input_file = "C:\pythonscripts\medicalpy\medic_text.txt"  # Path to input text file
    output_file = "C:\pythonscripts\medicalpy\medical_term_counts.csv"  # Path to save the output CSV

    # Read the text file
    text = read_text_file(input_file)
    
    # Extract medical terms
    medical_terms = extract_medical_terms(text)
    
    # Count occurrences of each medical term
    term_counts = count_word_occurrences(medical_terms)
    
    # Save the results to a CSV file
    save_to_csv(term_counts, output_file)
