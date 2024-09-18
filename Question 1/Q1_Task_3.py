import pandas as pd
from collections import Counter
from transformers import AutoTokenizer
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

output_txt_file = 'Q1_extracted_texts.txt'
top_words_csv = 'Q1_top_30_words.csv'

# Task 3.1: Count the Top 30 Most Common Words and Store in a CSV File
def count_top_words(text_file, output_csv):
    try:
        with open(text_file, 'r', encoding='utf-8') as file:
            text = file.read()

        if not text.strip():  # Check if the file is empty
            print(f"Error: The file '{text_file}' is empty.")
            return

        # Split the text into words and count occurrences
        words = text.split()
        word_counts = Counter(words)

        # Get the 30 most common words
        top_30_words = word_counts.most_common(30)

        # Store the result in a CSV file
        df_top_words = pd.DataFrame(top_30_words, columns=['Word', 'Count'])
        df_top_words.to_csv(output_csv, index=False)

        print(f"\nTask 3.1: Top 30 words saved to {output_csv}\n")
    except FileNotFoundError:
        print(f"Error: The file '{text_file}' was not found.")
    except Exception as e:
        print(f"An error occurred while counting words: {str(e)}")

# Task 3.2: Count Unique Tokens Using Transformers AutoTokenizer (with Chunking and Truncation)
def count_unique_tokens(text_file, chunk_size=5000, max_length=500):
    try:
        tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased", use_fast=True)

        token_counts = Counter()

        with open(text_file, 'r', encoding='utf-8') as file:
            while True:
                # Read the file in chunks
                chunk = file.read(chunk_size)
                if not chunk:
                    break  # End of file

                # Tokenize the chunk with truncation to handle long sequences
                tokens = tokenizer.tokenize(chunk, truncation=True, max_length=max_length)

                # Count token occurrences
                token_counts.update(tokens)

        # Get the 30 most common tokens
        top_30_tokens = token_counts.most_common(30)
        
        print(f"\nTask 3.2: Top 30 tokens:\n {top_30_tokens}")
        return top_30_tokens

    except FileNotFoundError:
        print(f"Error: The file '{text_file}' was not found.")
    except Exception as e:
        print(f"An error occurred while counting tokens: {str(e)}")

# Run the function for Task 3.1
count_top_words(output_txt_file, top_words_csv)

# Run the function for Task 3.2
count_unique_tokens(output_txt_file)
