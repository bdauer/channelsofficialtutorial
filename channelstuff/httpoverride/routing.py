from channels.routing import route
from httpoverride.consumers import ws_message

channel_routing = [
    route("websocket.receive", ws_message),
]
