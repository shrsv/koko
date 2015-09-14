#!/usr/bin/python

import nltk
import string
import freq
import inv_dict
from math import floor

def tagger(that):

    # Tokenize and pos tag the original text after removing punctuation
    # Punctuation removal code from SO available at:
    #    http://stackoverflow.com/questions/11692199/string-translate-with-unicode-data-in-python
    #
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    text = nltk.word_tokenize(that.translate(remove_punctuation_map))
    tagged = nltk.pos_tag(text)

    # Initialize lemmatizer object
    # What is it used to? This:
    # >> lmtzr.lemmatize("dogs") # dog
    # >> lmtzr.lemmatize("churches") # church
    lmtzr = nltk.stem.wordnet.WordNetLemmatizer()

    # A list of words we avoid in tags:
    # if, or, about, because, until, etc.
    stop_words = nltk.corpus.stopwords.words('english')

    cleaned_up = []

    for word, word_type in tagged:
        word = word.lower()
        # Catches all nouns except the stop words
        if len(word) >= 3 and word not in stop_words and word_type.startswith('NN') == True:
            # Find word base
            # ex: dogs => dog, gods => god
            word = lmtzr.lemmatize(word)
            cleaned_up.append(word)

    # Make a dictionary of the following format:
    # {
    #   "dogs" : 3,
    #   "gods": 2,
    #   "tigers": 2
    # }
    word_freq = freq.freq(cleaned_up)

    # Flip the above dictionary to get:
    # {
    #    3 : ["dogs"]
    #    2: ["gods", "tigers"]
    #}
    freq_word = inv_dict.inv_dict(word_freq)

    freqs = freq_word.keys()
    # Greater to smaller
    freqs.sort(reverse=True)

    threshold = floor(max(freqs)/3)
    tags = []

    for key in freqs:
        if key >= threshold:
            tags.extend(freq_word[key])

    return tags
    # debug purposes
    # for key in freq_word:
    #     if key >= threshold:
    #         print key, " -> ", freq_word[key]

if __name__ == "__main__":
    with open("manny_god_delusion_review.md") as f:
        that = f.read()
    print tagger(that)
