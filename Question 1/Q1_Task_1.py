import pandas as pd

# Define the file paths
csv_files = [
    r'CSV1.csv', 
    r'CSV2.csv', 
    r'CSV3.csv', 
    r'CSV4.csv'
]

columns_to_check = ['SHORT-TEXT', 'TEXT']
output_txt_file = 'Q1_extracted_texts.txt'

def extract_and_save_text(df, column_name, output_file, mode='a'):
    """Extracts text from the specified column and saves it to a text file."""
    if column_name in df.columns:
        texts = df[column_name].dropna().tolist()  # Drop NaN values
        with open(output_file, mode, encoding='utf-8') as outfile:
            for text in texts:
                outfile.write(text + '\n')
        return True
    return False

# Process each CSV file and extract text from the appropriate columns
with open(output_txt_file, 'w', encoding='utf-8') as outfile:
    outfile.write("")  # Clear the file at the beginning

for i, csv_file in enumerate(csv_files):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file)
        
        # Check for both possible column names and save text if the column exists
        saved = False
        for column in columns_to_check:
            if extract_and_save_text(df, column, output_txt_file, 'a'):
                print(f"Extracted text from '{column}' in {csv_file}.")
                saved = True
                break  # Stop checking other columns if one is found
        
        if not saved:
            print(f"None of the specified columns found in {csv_file}.")
    
    except FileNotFoundError:
        print(f"Error: The file '{csv_file}' does not exist.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{csv_file}' is empty.")
    except Exception as e:
        print(f"An unexpected error occurred while processing '{csv_file}': {str(e)}")

