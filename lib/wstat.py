import os
import re
from collections import Counter

class UserAnswers:

    def __init__(self, text):
        self.text = text

    def words_count(self):
        text = re.findall(r'\w+', self.text.lower())
#        text = text.replace("\n", "").replace("\r", "")
#        skips = ["i", "am", "is", "i'm", "are", "was", "were", "and", "an" , "a", "to", "for", "the"]
#        words = [i for i in text if i not in skips]

#        word_count = Counter(words)
        word_count = Counter(text)

        uwc = len(word_count) # unique word's count
        wc = sum(word_count.values()) # all word's count
        return {'wc' : wc, 'uwc' : uwc, 'cntr' : dict(word_count.most_common(50))}
