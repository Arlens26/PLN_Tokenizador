from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
#from django.shortcuts import render
from .forms import TweetForm
from .models import Tweet
###### Libraria sentence piece para words
import sentencepiece as spm


# Create your views here.
		
def catch_index(request):	
	spm.SentencePieceTrainer.train('--input=tweets_clean.txt --model_prefix=m_word --model_type=word --vocab_size=2000')
	sp_word = spm.SentencePieceProcessor()
	sp_word.load('m_word.model')
	tweet = Tweet.objects.order_by('id')
	if request.method == 'POST':
		#return render(request, 'index.html')
		form = TweetForm(request.POST)
		if form.is_valid():			
			#text_tweet = form.save()
			word = sp_word.encode_as_pieces(str(Tweet.tweet))
			word.save()
			#form.save()
			return HttpResponseRedirect('/')
	else:
		form = TweetForm()

	template = loader.get_template('index.html')
	context = {
		'tweet' : tweet,
		'form' : form
	}
		#if form.is_valid():
			#instancia = form.save(commit=False)
			#instancia.save()
	return HttpResponse(template.render(context, request))

def catch_form(request):
	template = loader.get_template('form.html')
	form = TweetForm()
	#tweet = Tweet.objects.order_by('id')
	context = {
		#'tweet' : tweet,
		'form' : form
	}
	return HttpResponse(template.render(context, request))