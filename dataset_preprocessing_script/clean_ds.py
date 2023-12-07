import pandas as pd
import ast
from langdetect import detect, LangDetectException

# #FILTER FROM LANG 
def is_ukrainian(text):
    try:
        print(text)
        return detect(text) == 'de'
    except LangDetectException:
        return False

def parse_row(row):
    try:
        
        return ast.literal_eval(row)
    except ValueError:
        return None


df = pd.read_csv('first_10000_deu_ukr_translation_pairs.csv', header=None, names=['data'])
df = df.head(10000)
df['data'] = df['data'].apply(parse_row)

df = df.dropna()

df['is_ukrainian'] = df['data'].apply(lambda x: is_ukrainian(x['de']) if x and 'de' in x else False)

filtered_df = df[df['is_ukrainian']]

filtered_df = filtered_df.drop(columns=['is_ukrainian'])

filtered_df.to_csv('de_uk.csv')




# import pandas as pd
# import ast

# def parse_row(row):
#     try:
#         parsed = ast.literal_eval(row)
#         return parsed.get('de', ''), parsed.get('en', '')
#     except:
#         return '', ''

# df = pd.read_csv('first_10000_deu_ukr_translation_pairs.csv', header=None, names=['data'])

# parsed_data = df['data'].apply(parse_row)
# df['DE'] = parsed_data.apply(lambda x: x[0])
# df['UK'] = parsed_data.apply(lambda x: x[1])

# df = df.drop(columns=['data'])

# print(df.head()) 
# df.to_csv('de_uk.csv', index=False)  




# import pandas as pd
# from pandas import json_normalize

# df = pd.read_csv('de_uk_full.csv') 

# normalized_df = json_normalize(df['train'].apply(eval))
# filtered_df = normalized_df[(normalized_df['Original lang'] == 'deu') & (normalized_df['Target lang'] == 'ukr')]


# first_10000_pairs = filtered_df.head(10000)

# selected_columns = first_10000_pairs[['Text', 'Translated text']]
# selected_columns.columns = ['DE', 'UK']

# selected_columns.to_csv('first_10000_deu_ukr_translation_pairs.csv', index=False)