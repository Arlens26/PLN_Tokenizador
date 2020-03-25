from django.db import models

###### Libraria sentence piece para words
import sentencepiece as spm

# Create your models here.
class Tweet(models.Model):

	'''def __init__(self,tweet):
   		self.tweet=tweet '''

	# Administración de modelos 
	#text = models.CharField(max_length=500)
	tweet = models.TextField(max_length=500)
	#contenido = models.TextField()
	name = "Tweet"

	def __str__(self):
		'''spm.SentencePieceTrainer.train('--input=tweets_clean.txt --model_prefix=m_word --model_type=word --vocab_size=2000')
		sp_word = spm.SentencePieceProcessor()
		sp_word.load('m_word.model')
		word = sp_word.encode_as_pieces(self.tweet)'''
		return self.name+str(self.id)
	
	# Modelo de palabra
'''	def word_train(self):
		spm.SentencePieceTrainer.train('--input=tweets_clean.txt --model_prefix=m_word --model_type=word --vocab_size=2000')
		sp_word = spm.SentencePieceProcessor()
		sp_word.load('m_word.model')
		word = sp_word.encode_as_pieces(self.tweet)
		return word

	# Modelo de subpalabras
	def subword_train():	
		spm.SentencePieceTrainer.train('--input=tweets_clean.txt --model_prefix=m_user --user_defined_symbols=<sep>,<cls> --vocab_size=2000')
		sp_user = spm.SentencePieceProcessor()
		sp_user.load('m_user.model')

'''	