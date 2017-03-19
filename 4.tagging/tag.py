import nltk 
from nltk.corpus import state_union 
from nltk.tokenize import PunktSentenceTokenizer ##Unsupervised machine learnoing tokenizer

train_text = state_union.raw("2005-GWBush.txt") 
sample_text = state_union.raw("2006-GWBush.txt") 
print(sample_text)
custom_sent_tokenizer = PunktSentenceTokenizer(train_text) 
#PunktSentenceTokenizer is an sentence boundary detection algorithm that must be trained to be used [1]. NLTK already includes a 
#pre-trained version of the PunktSentenceTokenizer.

tokenized = custom_sent_tokenizer.tokenize(sample_text) 

def process_content():
	try:
		for i in tokenized[:5]:
			words = nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)
			print(tagged)

	except Exception as e:
		print(str(e))

process_content()



