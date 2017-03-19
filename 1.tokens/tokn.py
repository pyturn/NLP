from nltk.tokenize import sent_tokenize , word_tokenize 

Example_text = "Hello Mr. Smith, how are you doing today? The weather is great and Python is awesome. The sky is pinkish blue. You should not eat cardboard."

print (sent_tokenize(Example_text))

for w in word_tokenize(Example_text):
	print (w)