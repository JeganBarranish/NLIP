import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter 

nltk.download('punkt_tab')   
nltk.download('stopwords')

text = input("Enter the text: ")

# text to lowercase
text = text.lower()

# Tokenization
tokens = word_tokenize(text)

# Punctuation removal
tokens_no_punct = [word for word in tokens if word not in string.punctuation]

# stop words
stop_words = set(stopwords.words('english'))

# Stop word extraction
extracted_stopwords = [word for word in tokens_no_punct if word in stop_words]

# Stop word removal
filtered_words = [word for word in tokens_no_punct if word not in stop_words]

# Topical word )
topical_words = filtered_words

# Frequency counting 
word_frequencies = Counter(topical_words)


print("\n--- RESULTS ---")
print("Original Tokens:", tokens)
print("Tokens after Punctuation Removal:", tokens_no_punct)
print("Extracted Stop Words:", extracted_stopwords)
print("After Stop Word Removal:", filtered_words)
print("Topical Words:", topical_words)
print("Word Frequencies (Topical Words):", dict(word_frequencies)) 