from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group

# Connected to websocket.connect
def ws_add(message):
    message.reply_channel.send({"accept": True})
    Group("chat").add(message.reply_channel)

def ws_message(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    Group("chat").send({
        "text": "[user] %s" % message.content['text'],
    })

# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)


"""
The following JS was entered into the console to create
a websocket, connect, sent a message.


// Note that the path doesn't matter for routing; any WebSocket
// connection gets bumped over to WebSocket consumers
socket = new WebSocket("ws://" + window.location.host + "/chat/");
socket.onmessage = function(e) {
    alert(e.data);
}
socket.onopen = function() {
    socket.send("hello world");
}
// Call onopen directly if socket is already open
if (socket.readyState == WebSocket.OPEN) socket.onopen();


"""
