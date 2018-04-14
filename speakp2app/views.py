from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Ieltsspeakingp2topic, Answers
from operator import itemgetter
from lib.wstat import UserAnswers


@login_required

def index(request):
    full_topic_list = Ieltsspeakingp2topic.objects.all().values('id', 'sp2topic','sp2question', 'answers__answer', 'answers__id', 'answers__uid')
    topic_list = [] # collect questions and answers for current user
    list_in = [] # collect question id which is added in topic_list
    all_answers = '' # all answers for staistic
    answered_count = 0
    for topic in full_topic_list :
        if topic['answers__uid'] == request.user.id : # question is answered by current user
            topic_list.append(topic)
            list_in.append(topic['id'])
            all_answers += topic['answers__answer'] + " " # all answers for staistic
            answered_count +=1
        elif topic['answers__uid'] == None: # questions without any answers
            topic_list.append(topic)
            list_in.append(topic['id'])

    for topic in full_topic_list :
        if topic['id'] not in list_in : # other questions
            tpc = {'id': topic['id'], 'sp2topic': topic['sp2topic'],'sp2question':topic['sp2question'],'answers__answer': None, 'answers__id': None, 'answers__uid': None}
            topic_list.append(tpc)
            list_in.append(topic['id'])

    ua = UserAnswers(all_answers, 50)
    wcount = ua.words_count
    topic_list = sorted(topic_list, key=itemgetter('id'))
    context = {'topic_list': topic_list, 'answers' : wcount, 'answered': [answered_count, len(topic_list)-answered_count]}
    return render(request, 'speakp2app/index.html',context)
