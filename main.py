import os
import tornado.ioloop
import tornado.web
import tornado.websocket

# TODO move this to cfg
PORT = 8888

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")

    def check_origin(self, origin):
        return True


def make_app():
    root = os.path.dirname(os.path.abspath(__file__))
    return tornado.web.Application([
        (r"/resources/(.*)", tornado.web.StaticFileHandler, {"path": root}),
        (r"/websocket", EchoWebSocket)
    ], default_handler_class=MainHandler)

if __name__ == "__main__":
    app = make_app()
    app.listen(PORT)
    print("Now serving on port {0}".format(PORT))
    tornado.ioloop.IOLoop.current().start()
