from flask import Flask, request, abort
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from gpt4free import you


app = Flask(__name__)


@app.route('/chatgpt', methods=['GET', 'POST'])
def chatgpt():
    data = request.json

    response = you.Completion.create(
        prompt=data['text'],
        detailed=False,
        include_links=False)
    print(response.dict())  # TEMP
    print("\n\n")
    return response.dict()['text']


if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 8060)
                             , app, handler_class=WebSocketHandler)
    http_server.serve_forever()
