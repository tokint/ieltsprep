from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Ieltswritingp2topic, Answers
from operator import itemgetter
from lib.wstat import UserAnswers

def index(request):
    full_topic_list = Ieltswritingp2topic.objects.all().values('id', 'wr2topic','wr2question','wr2sampleurl', 'answers__answer', 'answers__id', 'answers__uid')
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
            tpc = {'id': topic['id'], 'wr2topic': topic['wr2topic'],'wr2question':topic['wr2question'],'wr2sampleurl':topic['wr2sampleurl'],'answers__answer': None, 'answers__id': None, 'answers__uid': None}
            topic_list.append(tpc)
            list_in.append(topic['id'])

    ua = UserAnswers(all_answers, 50)
    wcount = ua.words_count
    topic_list = sorted(topic_list, key=itemgetter('id'))
    context = {'topic_list': topic_list, 'answers' : wcount, 'answered': [answered_count, len(topic_list)-answered_count]}
    return render(request, 'writep2app/index.html',context)

def set_answer(request, topic_id):
    tid = Ieltswritingp2topic.objects.get(id=topic_id)
    ans = request.POST['ans']
    uid = request.user.id
    query = Answers(topic=tid, answer=ans, uid=uid)
    query.save()
    url = '/wr2/'
    return redirect(url)

def del_answer(request, answer_id):
    tid = Answers.objects.get(id=answer_id)

    if tid.uid == request.user.id :
        tid.delete()
        resp = "OK"
    else:
        resp = "DENY"

    return HttpResponse(resp)

def upd_answer(request, answer_id):
    auid = Answers.objects.get(id=answer_id)
    uid = request.user.id

    if auid.uid == uid :
        ans = request.POST['ans']
        auid.answer = ans
        auid.save()
        resp = "OK"
    else:
        resp = "DENY"

    return HttpResponse(resp)
