from django.shortcuts import render
from .ai import response, greeting, sent_tokens 


def home(request):
#The chatbot
#refactor
    if request.method == 'POST':
        user_response = request.form.get('input')
        user_response = user_response.lower()
        if user_response != 'bye':
            if user_response == 'thanks' or user_response == 'thank you':
                flash("Marcus Aurelius: You are welcome..")
            else:
                if greeting(user_response) != None:
                    flash("Marcus Aurelius: " + greeting(user_response))
                else:
                    flash("Marcus Aurelis: "+response(user_response))
                    sent_tokens.remove(user_response)
        else:
            flash("Marcus Aurelius: Good bye my friend!")

    return render(request, 'chatbot/index.html')

def ai_page(request):
    return render(request, "chatbot/AI.html")

def stoicism(request):
    return render(request, 'chatbot/stoicism.html')
