from django.http import HttpResponse
from channels.handler import AsgiHandler


def http_consumer(message):
    # Makse a standard HTTP response - access ASGI path attribute directly
    response = HttpResponse("Hello World! You asked for %s" % message.content['path'])
    #Encode the response into message format
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)
