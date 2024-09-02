import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Append the path to the nltk_data directory in your project
nltk.data.path.append(r'C:\Users\junai\ResuMeister\backend\nltk_data')

# Test if stopwords and punkt work correctly
print("Stopwords:", stopwords.words('english'))

text = "This is a test sentence."
tokens = word_tokenize(text)
print("Tokens:", tokens)
