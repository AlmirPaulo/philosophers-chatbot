from django.shortcuts import render
from .forms import AskForm
from .ai import response, greeting, sent_tokens 


def home(request):
#The chatbot
    if request.method == 'POST':
        form = AskForm(request.POST)         
        user_response = form['question'].value()
        if form.is_valid:
            answer = ''
            user_response = user_response.lower()
            if user_response != 'bye':
                if user_response == 'thanks' or user_response == 'thank you':
                     answer = "Marcus Aurelius: You are welcome..."
                else:
                    if greeting(user_response) != None:
                        answer = "Marcus Aurelius: " + greeting(user_response)
                    else:
                        answer = "Marcus Aurelis: "+response(user_response)
                        sent_tokens.remove(user_response)
            else:
                answer = "Marcus Aurelius: Good bye my friend!"
    else:
        form = AskForm()

    return render(request, 'chatbot/index.html', {'form':form , 'answer':answer})

def ai_page(request):
    return render(request, "chatbot/AI.html")

def stoicism(request):
    return render(request, 'chatbot/stoicism.html')
