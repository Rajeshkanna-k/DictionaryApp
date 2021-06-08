import requests,time
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Word, Visitor
from .forms import RegisterForm
from .forms import WordForm
from PyDictionary import PyDictionary
from collections import Counter
from datetime import date, timedelta


def home(request):
    
    visitor(request)

    isSubmitted = False
    if request.method == 'POST':
        form = WordForm(request.POST)
        form.is_found = True
        if form.is_valid(): 
           isSubmitted = True
           form.save()
        # return HttpResponseRedirect('/Home?submitted=True') 
    
    form = WordForm()
    words = Word.objects.all()
    wordsCount=words.count()    

    word = ""
    if wordsCount != 0:
         word = str(words[wordsCount-1])
        
    synonyms = PyDictionary.synonym(word) 
    antonyms = PyDictionary.antonym(word)
    
    obj = words[wordsCount-1]
    if synonyms !=None and antonyms !=None:
         obj.is_found = True
         obj.save()
    else:
         obj.is_found = False
         obj.save()

    word_data = {
             'word' : word,
             'synonyms' : synonyms,
             'antonyms' : antonyms,
    }
    context = {'word_data' : word_data, 'form' : form, 'isSubmitted': isSubmitted}
    return render(request, 'index.html', context)

def analatics(request): 
    words_lst = Word.objects.all().order_by('name')

    # filtered_wrdlst = words_lst (lambda a : a.is_found == True)
    filtered_wrdlst = Word.objects.filter(is_found = True)

    most_word_search = {}
    for wrd in filtered_wrdlst:
        wrd = str(wrd).lower() 
        if wrd not in most_word_search:
             most_word_search[wrd] = 1
        else: 
             most_word_search[wrd] += 1

    word_counter = Counter(most_word_search) 

    show_Most_Search_Words = []
    for word, count in word_counter.most_common(4):
         show_Most_Search_Words.append(str(word))  

    #Filter out the words were not found in dictionary
    templst = list(Word.objects.filter(is_found = False))

    filtered_Not_Found_Word = set()

    for item in templst:
         if item not in filtered_Not_Found_Word:
             filtered_Not_Found_Word.add(str(item))
    
    show_Visitors_Counts = Visitor.objects.all().order_by("-created_date")

    show_Visitors_Counts = show_Visitors_Counts[:5]

    context = {'show_Most_Search_Words' : show_Most_Search_Words, 'filtered_Not_Found_Word' : filtered_Not_Found_Word,
               'show_Visitors_Counts': show_Visitors_Counts
              }    
    return render(request,'analatics.html', context)

# User Register
def register(request):
    
    isRegisteredUserValid = False
    if request.method=="POST":
        user_form=RegisterForm(request.POST)
        if user_form.is_valid():
             isRegisteredUserValid = True
             user_form.save()
             messages.success(request,'User has been registered.')
            # time.sleep(10)
        #  return render(request,'home.html', {'isRegisteredUserValid':isRegisteredUserValid}) 
        return HttpResponseRedirect('/') #?q=' + str(isRegisteredUserValid)
    else:
        user_form=RegisterForm()
   
    return render(request, 'registration/register.html', { 'user_form': user_form}) #, 'isRegisteredUserValid':isRegisteredUserValid}////registration/register.html
    
def visitor(request):
     print("Calling vistor func...................")

     strDateValue = Visitor.objects.filter(created_date=str(date.today())).all()
     vCount= 0
     dateValue = ""
     if strDateValue.count() != 0:
         for item in strDateValue:
             vCount = item.visitors_count
             dateValue = str(item.created_date)

     num_visits = request.session.get('num_visits', 0)
     request.session['num_visits'] = num_visits + 1
     
     if vCount != 0 and dateValue != "":
         num_visits= vCount + 1

     visitors = Visitor.objects.all().order_by("created_date")
     visitorsCount = visitors.count()
     obj = visitors[visitorsCount-1]
     print("obj value of visitors[visitorsCount-1", obj.created_date)
     if strDateValue.count() == 0:
         objCreate = Visitor(visitors_count = 1, created_date = date.today())
         objCreate.save()
     elif obj.created_date == date.today():
         if num_visits == 0 or num_visits == 1:
              obj.visitors_count = vCount + 1
         else:
             obj.visitors_count = num_visits
         obj.save()
       
     show_Visitors_Counts = list(visitors)
    #  strDateValue = Visitor.objects.filter(created_date=str(date.today() - timedelta(days=1))).all() #.first()

     visitor_context = {'show_Visitors_Counts': show_Visitors_Counts}

     return render(request, 'analatics.html', visitor_context)


