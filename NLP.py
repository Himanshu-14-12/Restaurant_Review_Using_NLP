import pandas as pd

dataset = pd.read_csv("Restaurant_Reviews.tsv", delimiter="\t", quoting=3)

import re
import nltk

nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for _ in range(0,1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][_])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')
    review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
    review = ' '.join(review)
    corpus.append(review)
    
    