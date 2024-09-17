import pandas as pd
import spacy
from collections import Counter
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import warnings

# Suppress specific warnings related to truncation
warnings.filterwarnings("ignore")

output_txt_file = 'merged_texts.txt'

# Define maximum token length for BioBERT (510 tokens, plus 2 for [CLS] and [SEP])
MAX_TOKEN_LENGTH = 500

# Try to load the SpaCy models with error handling
def load_spacy_model(model_path):
    try:
        return spacy.load(model_path)
    except OSError as e:
        print(f"Error: Failed to load the SpaCy model '{model_path}'. {str(e)}")
        return None

# Try to load BioBERT model and tokenizer with error handling
def load_biobert_pipeline(model_name):
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForTokenClassification.from_pretrained(model_name)
        return pipeline("ner", model=model, tokenizer=tokenizer)
    except Exception as e:
        print(f"Error: Failed to load BioBERT model '{model_name}'. {str(e)}")
        return None

# Function to extract entities using SpaCy models
def extract_entities_spacy(text_file, model, label_filter):
    try:
        with open(text_file, 'r', encoding='utf-8') as file:
            text = file.read()

        if model is None:
            print("Error: No model available for entity extraction.")
            return []

        doc = model(text)
        entities = [ent.text for ent in doc.ents if ent.label_ in label_filter]
        return entities
    except FileNotFoundError:
        print(f"Error: The file '{text_file}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred during entity extraction: {str(e)}")
        return []

# Function to extract entities using BioBERT with correct truncation and chunking
def extract_entities_biobert(text_file, biobert_pipeline, max_length=MAX_TOKEN_LENGTH):
    try:
        with open(text_file, 'r', encoding='utf-8') as file:
            text = file.read()

        if biobert_pipeline is None:
            print("Error: No BioBERT pipeline available for entity extraction.")
            return [], []

        # Tokenize the text and apply truncation and padding
        tokenizer = biobert_pipeline.tokenizer
        tokens = tokenizer(text, truncation=True, padding='max_length', max_length=max_length, return_overflowing_tokens=True, return_tensors="pt")

        # Ensure the total number of tokens is within the 512 limit, including [CLS] and [SEP]
        input_texts = tokenizer.batch_decode(tokens['input_ids'], skip_special_tokens=True)

        diseases, drugs = [], []
        for chunk in input_texts:
            entities = biobert_pipeline(chunk)  # Pass text chunks to the BioBERT pipeline
            diseases += [entity['word'] for entity in entities if entity['entity'] == 'B-Disease']
            drugs += [entity['word'] for entity in entities if entity['entity'] == 'B-Drug']

        return diseases, drugs

    except FileNotFoundError:
        print(f"Error: The file '{text_file}' was not found.")
        return [], []
    except Exception as e:
        print(f"An error occurred during BioBERT entity extraction: {str(e)}")
        return [], []

# Load models with error handling
nlp_sci_sm = load_spacy_model("en_core_sci_sm")
biobert_pipeline = load_biobert_pipeline("dmis-lab/biobert-base-cased-v1.1")

# Extract diseases and drugs using SpaCy models with error handling
diseases_sci_sm = extract_entities_spacy(output_txt_file, nlp_sci_sm, ['DISEASE'])

# Extract diseases and drugs using BioBERT with correct chunking
diseases_biobert, drugs_biobert = extract_entities_biobert(output_txt_file, biobert_pipeline)

# Compare the results of SpaCy models and BioBERT
print(f"SpaCy (en_core_sci_sm) detected {len(diseases_sci_sm)} diseases")
print(f"BioBERT detected {len(diseases_biobert)} diseases and {len(drugs_biobert)} drugs")

# Output most common entities if found
if diseases_biobert:
    print("Most common diseases detected by BioBERT:", Counter(diseases_biobert).most_common(5))
else:
    print("No diseases detected by BioBERT.")
    
if drugs_biobert:
    print("Most common drugs detected by BioBERT:", Counter(drugs_biobert).most_common(5))
else:
    print("No drugs detected by BioBERT.")
