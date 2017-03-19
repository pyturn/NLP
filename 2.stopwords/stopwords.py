from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

Example_sentence = "This is sample sentence showing off the stop words."

stop_words = set(stopwords.words('english'))

#print (stop_words) # Default stop words in English.
'''
for i in Example_sentence:
	if i not in stop_words:
		print (i)'''
word_tokens = word_tokenize(Example_sentence)
filtered_sentence = []
for w in word_tokens:
	if w not in stop_words:
		filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)