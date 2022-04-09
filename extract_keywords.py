import nltk
import re
from nltk import tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize 
from keybert import KeyBERT

class Extractor:

    def __init__(self, file_name) -> None:
        self._file_name = file_name
        self._description = ""
        with open(self._file_name, "r", encoding="utf8") as file:
            for line in file:
                self._description += line

    def update_description(self, file_name):
        with open(file_name, "r", encoding="utf8") as file:
            for line in file:
                self._description += line
        
    
    def clean(self):
        text = self._description.lower()
        text = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", text)
        stop = stopwords.words('english')
        text = " ".join([word for word in text.split() if word not in (stop)])
        stemmer = PorterStemmer()
        text = " ".join([stemmer.stem(word) for word in text.split()])

        return text

    def generate_keyword_tokens(self):
        tokens = nltk.word_tokenize(self.clean())
        return tokens
    
    def tag_tokens(self, tokens):
        return nltk.pos_tag(tokens)
    
    def extract(self):        
        kw_model = KeyBERT()
        keywords = kw_model.extract_keywords(self._description, stop_words="english", 
                                            keyphrase_ngram_range=(1, 1), top_n=20)
        keywords_list= list(dict(keywords).keys())
        return keywords_list



