from gevent import monkey
monkey.patch_all()
from gevent.lock import BoundedSemaphore
from gevent.pywsgi import WSGIServer
from flask import Flask, request, abort
from geventwebsocket.handler import WebSocketHandler
from chatgpt import ChatGPT


app = Flask(__name__)
bot = ChatGPT()

sem = BoundedSemaphore(1)    # only allows 1 greenlet at one time, others must wait until one is released


@app.route('/chatgpt', methods=['GET', 'POST'])
def link_receiver():
    data = request.json

    if sem.ready():
        sem.acquire()
        response = bot.ask(data["text"])
        sem.release()
        return response
    return abort(500)


if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 8060)
                             , app, handler_class=WebSocketHandler)
    http_server.serve_forever()
