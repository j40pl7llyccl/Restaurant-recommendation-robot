# views.py
from django.views import generic
from message_handler import post_facebook_message
from query_processor import sayHi

class fbChatBotView(generic.View):
    # ... Django視圖代碼 ...
    
    #csrf(?)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)
    
    #to get facebook webhook and verify
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == 'a8b5b1a6a7b2b9a7':    
            return HttpResponse(self.request.GET['hub.challenge'])
    
    # Post function to handle Facebook messages
    def post(self, request):
        message_entries = json.loads(self.request.body.decode('utf-8'))['entry']
        for entry in message_entries:
            messaging = entry['messaging']
            for message in messaging:
                if 'message' in message:
                    senderID = message['sender']['id']
                    senderText = message['message']['text']
                    post_facebook_message(senderID,sayHi(senderText))
        return HttpResponse()   