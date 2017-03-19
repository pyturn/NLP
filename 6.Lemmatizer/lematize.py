import nltk
#import nltk.tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import state_union

'''sample_text = state_union.raw("2005-GWBush.txt")
tokenized = nltk.sent_tokenize(sample_text)
print (len(tokenized))

lemmatizer = WordNetLemmatizer()

for i in tokenized[:5]:
	words = nltk.word_tokenize(i)
	tagged = nltk.pos_tag(words)
	#print (tagged)
	for j in range(len(tagged)):
		print(lemmatizer.lemmatize(tagged[j][0], pos = tagged[j][1]))'''
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("best", pos="a"))
#print(lemmatizer.lemmatize("Barack", pos="NNP"))