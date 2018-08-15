from django.http import HttpResponse

def index(request):
	return HttpResponse("hello world its working")

def details(request, question_id):
	return HttpResponse("Return the details of the question: %s" %question_id)


def results(request, question_id):
	return HttpResponse("Result of question no. %s" %question_id)


def vote(request, question_id):
	return HttpResponse("vote is given to question id: %s" %question_id)