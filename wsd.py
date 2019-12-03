
import codecs
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import wordnet


def synonymsGet(word):
    synonyms = []

    for s in wordnet.synsets(word):
        for i in s.lemmas():
            synonyms.append(i.name())

    return synonyms

def similarityMeasure(word1, word2):

    word1 = word1 + ".n.01"
    word2 = word2 + ".n.01"
    try:
        w1 = wordnet.synset(word1)
        w2 = wordnet.synset(word2)

        return w1.wup_similarity(w2)

    except:
        return 0
    
def simpleFilter(sentence):

    filtered_sent = []
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(sentence)

    for w in words:
        if w not in stop_words:
            filtered_sent.append(lemmatizer.lemmatize(w))

    return filtered_sent

def advanceFilter(sentence):

    filtered_sent = []
    lemmatizer = WordNetLemmatizer()
    ps = PorterStemmer()

    stop_words = set(stopwords.words("english"))
    words = word_tokenize(sentence)

    for w in words:
        if w not in stop_words:
            filtered_sent.append(lemmatizer.lemmatize(ps.stem(w)))
            for i in synonymsGet(w):
                filtered_sent.append(i)
    return filtered_sent

def findMeaning(sent3):
    
    devicefile = codecs.open("mousedevice.txt", 'r', 'utf-8',errors = 'ignore')
    sent1 = devicefile.read().lower()
    
    animalfile = codecs.open("mouseanimal.txt", 'r', "utf-8", errors = 'ignore')
    sent2 = animalfile.read().lower()

    answer1 = ('Mouse as a computer device')
    answer2 = ('Mouse as an animal')
    
    sent3 = sent3.lower()
    filtered_sent1 = []
    filtered_sent2 = []
    filtered_sent3 = []

    sent31_similarity = 0
    sent32_similarity = 0

    filtered_sent1 = simpleFilter(sent1)
    filtered_sent2 = simpleFilter(sent2)
    filtered_sent3 = simpleFilter(sent3)

    for i in filtered_sent3:

        for j in filtered_sent1:
            sent31_similarity = sent31_similarity + similarityMeasure(i, j)
        for j in filtered_sent2:
            sent32_similarity = sent32_similarity + similarityMeasure(i, j)

    filtered_sent1 = []
    filtered_sent2 = []
    filtered_sent3 = []
    filtered_sent1 = advanceFilter(sent1)
    filtered_sent2 = advanceFilter(sent2)
    filtered_sent3 = advanceFilter(sent3)
    sent1_count = 0
    sent2_count = 0
    
    for i in filtered_sent3:

        for j in filtered_sent1:
            if(i == j):
                sent1_count = sent1_count + 1
        for j in filtered_sent2:
            if(i == j):
                sent2_count = sent2_count + 1

    if((sent1_count + sent31_similarity) > (sent2_count+sent32_similarity)):
        return answer1
    else:
        return answer2