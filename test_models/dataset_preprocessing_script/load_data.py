from datasets import load_dataset
import pandas as pd
import requests
import pandas as pd
from io import StringIO
# def load_data_opus():
#     dataset = load_dataset("opus100", "de-uk")

#     df = pd.DataFrame(dataset['train'])

#     # Save the DataFrame as a CSV file
#     csv_file_path = 'opus100_de_uk.csv'
#     df.to_csv(csv_file_path, index=False)

#     print(f"CSV file saved as {csv_file_path}")

# load_data_opus()
# ---------------
# df = pd.read_csv('opus100_de_uk.csv')
# print(df.head(5))


import requests
import pandas as pd
from io import StringIO

def load_data_tatoeba():
    dataset = load_dataset('trondizzy/uk_en_combined_sets')
    df = pd.DataFrame(dataset)
    df.to_csv('uk_en_train.csv', index=False)
    

# Call the function
load_data_tatoeba()
df = pd.read_csv('uk_en_train.csv')
print(df.head(1))

