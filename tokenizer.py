import csv
from collections import Counter
from transformers import AutoTokenizer

def count_unique_tokens(file_path, model_name='bert-base-uncased', max_length=512, top_n=30):
    # Initialize the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Read the text from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text in chunks
    tokens = []
    for i in range(0, len(text), max_length):
        chunk = text[i:i + max_length]
        tokens.extend(tokenizer.tokenize(chunk))

    # Count the frequency of each token
    token_counts = Counter(tokens)

    # Get the top N most common tokens
    top_tokens = token_counts.most_common(top_n)

    return top_tokens

def write_to_csv(data, output_file_path):
    # Write the top 30 tokens and their counts to a CSV file
    with open(output_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Token', 'Count'])
        writer.writerows(data)


if __name__ == "__main__":
    input_file_path = 'medic_text.txt'  # Replace with your .txt file path
    output_file_path = 'top_30_tokens.csv'  # Desired output CSV file path
    model_name = 'bert-base-uncased'  # Replace with the tokenizer model name if needed

    top_30_tokens = count_unique_tokens(input_file_path, model_name)
    write_to_csv(top_30_tokens, output_file_path)

    print(f'Top 30 tokens have been written to {output_file_path}')
