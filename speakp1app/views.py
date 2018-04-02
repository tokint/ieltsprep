from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Ieltsspeakingp1topic, Answers
from operator import itemgetter
from lib.wstat import UserAnswers


@login_required
def index(request):
    full_topic_list = Ieltsspeakingp1topic.objects.all().values('id', 'sp1topic', 'answers__answer', 'answers__id', 'answers__uid')
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
            tpc = {'id': topic['id'], 'sp1topic': topic['sp1topic'],'answers__answer': None, 'answers__id': None, 'answers__uid': None}
            topic_list.append(tpc)
            list_in.append(topic['id'])

    ua = UserAnswers(all_answers, 50)
    wcount = ua.words_count
    topic_list = sorted(topic_list, key=itemgetter('id'))
    context = {'topic_list': topic_list, 'answers' : wcount, 'answered': [answered_count, len(topic_list)-answered_count]}
    return render(request, 'speakp1app/index.html', context)

def topicdetail(request, topic_id):
    try:
        topic = Ieltsspeakingp1topic.objects.get(pk=topic_id)
        answer = Answers.objects.filter(topic=topic_id, uid=request.user.id).first()
    except Ieltsspeakingp1topic.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'speakp1app/detail.html', {'topic': topic, 'answer': answer})

def set_answer(request, topic_id):
    tid = Ieltsspeakingp1topic.objects.get(id=topic_id)
    ans = request.POST['ans']
    uid = request.user.id
    query = Answers(topic=tid, answer=ans, uid=uid)
    query.save()
    url = '/sp1/'
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
