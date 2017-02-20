from channels.routing import route

channel_routing = [
    route("http.request", "httpoverride.consumers.http_consumer"),
]
