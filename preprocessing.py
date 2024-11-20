import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

# دانلود دیتای موردنیاز nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# مرحله 1: پیش‌پردازش متن
def preprocess_text(text):
    # توکن‌سازی
    tokens = word_tokenize(text)

    # حذف Stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.lower() not in stop_words]

    # استمینگ
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in tokens]

    # لماتایزیشن
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in stemmed_tokens]

    return lemmatized_tokens
