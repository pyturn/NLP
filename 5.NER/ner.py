import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import state_union 

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union("2006-GWBush.txt")
custom_sent_tokenizer = PumpktSentencetokenizer(train_text) 
tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
	try:
		for i in tokenized[:5]:
			words = nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)
			namedEnt = nltk.ne_chunk(tagged,binary =True)
			namedEnt.draw()
	except Exception as e:
		print(str(e))

process_content()