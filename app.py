import os
import tornado.ioloop
import tornado.web
import tornado.websocket

# TODO move this to cfg
PORT = 8080

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("html/index.html")

class PageNotFoundHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect("/", True)

class LettersSolverHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("html/lettersSolver.html")

class NumbersSolverHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("html/numbersSolver.html")

class RandomNumberDisplayHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("html/randomNumberDisplay.html")

def make_app():
    root = os.path.dirname(os.path.abspath(__file__))
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/letters", LettersSolverHandler),
        (r"/numbers", NumbersSolverHandler),
        (r"/display", RandomNumberDisplayHandler),
        (r"/resources/js/(.*)", tornado.web.StaticFileHandler, {"path": "js/"}),
        (r"/resources/css/(.*)", tornado.web.StaticFileHandler, {"path": "css/"}),
    ], default_handler_class=PageNotFoundHandler,)

if __name__ == "__main__":
    app = make_app()
    app.listen(PORT)
    print("Now serving on port {0}".format(PORT))
    tornado.ioloop.IOLoop.current().start()
