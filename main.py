
#%%IMPORTS
import requests
import os
import logging
import logging.handlers

#%% #Variables modificables
token = "6046833974:AAHftN2qwE7jXha9YR9pnlMGf0Y0J8yhQQQ"
chat_id = '-866701434'
msg = 'Todos somos putos cada 10 minutos'


#%%


def send_telegram_message(msg, chat_id, token = False):
    
    '''This function send a telegram message to an specific chat.
    
    #Pre: #msg: str type. It´s the message I want to send.
          #chat_id: str type. It´s the id of the chat.
          #token: str type. It´s the token of the account. By default is False.'''
          
    import requests
    
    if token:
        pass
    else:
        token = "6046833974:AAHftN2qwE7jXha9YR9pnlMGf0Y0J8yhQQQ" #Token del finanzas bot
    
    
    method = 'sendMessage'
    requests.post('https://api.telegram.org/bot' + token + '/' + method,
                  data = {'chat_id': chat_id,
                          'text': msg})
    
    print("Se ha enviado el mensaje existosamente")
    
#%%

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"

if __name__ == "__main__": 
    
    send_telegram_message(msg, chat_id) 






