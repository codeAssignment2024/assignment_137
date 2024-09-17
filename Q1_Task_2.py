#imports 
import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

#Installation Command:
    ##Install the libraries(SpaCy – ‘en_core_sci_sm’).
        ###python -m spacy download en_core_sci_sm
    ##Transformer Install Command
        ###pip install transformers

#Sample Usage in my code

## spacy
def load_spacy_model(model_path):
    try:
        return spacy.load(model_path)
    except OSError as e:
        print(f"Error: Failed to load the SpaCy model '{model_path}'. {str(e)}")
        return None

    nlp_sci_sm = load_spacy_model("en_core_sci_sm")


## transformers
def load_biobert_pipeline(model_name):
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForTokenClassification.from_pretrained(model_name)
        return pipeline("ner", model=model, tokenizer=tokenizer)
    except Exception as e:
        print(f"Error: Failed to load BioBERT model '{model_name}'. {str(e)}")
        return None

biobert_pipeline = load_biobert_pipeline("dmis-lab/biobert-base-cased-v1.1")
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased", use_fast=True)

    

