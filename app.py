import os
import tornado.ioloop
import tornado.web
import tornado.websocket
import gameData

# TODO move this to cfg
PORT = 80

data = gameData.GameData()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("html/index.html")

class PageNotFoundHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect("/", True)

class LettersSolverHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("html/lettersSolver.html")

class ControlHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("html/control.html")

class DisplayHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("html/display.html")

class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")

    def check_origin(self, origin):
        return True

class ControlWebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("Control WebSocket opened")
        self.write_message(data.toJSON())

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")

    def check_origin(self, origin):
        return True


def make_app():
    root = os.path.dirname(os.path.abspath(__file__))
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/letters", LettersSolverHandler),
        (r"/control", ControlHandler),
        (r"/display", DisplayHandler),
        (r"/resources/js/(.*)", tornado.web.StaticFileHandler, {"path": "js/"}),
        (r"/resources/css/(.*)", tornado.web.StaticFileHandler, {"path": "css/"}),
        (r"/socControl", ControlWebSocketHandler),
        (r"/websocket", EchoWebSocket)
    ], default_handler_class=PageNotFoundHandler,
       autoreload=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(PORT)
    print("Now serving on port {0}".format(PORT))
    tornado.ioloop.IOLoop.current().start()
