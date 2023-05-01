from gevent import monkey
monkey.patch_all()
from gevent.lock import BoundedSemaphore
from gevent.pywsgi import WSGIServer
from flask import Flask, request, abort
from geventwebsocket.handler import WebSocketHandler
from revChatGPT.V1 import Chatbot
# from chatgpt import ChatGPT


app = Flask(__name__)
chatbot = Chatbot(config={
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJpZ29yLmFuaWsuOTk1QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlfSwiaHR0cHM6Ly9hcGkub3BlbmFpLmNvbS9hdXRoIjp7InVzZXJfaWQiOiJ1c2VyLTNMSks5RVlTU2pLUnVqS0dZb0dha3c4YSJ9LCJpc3MiOiJodHRwczovL2F1dGgwLm9wZW5haS5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTIxODk4ODAzNjk2NjU1ODc1ODMiLCJhdWQiOlsiaHR0cHM6Ly9hcGkub3BlbmFpLmNvbS92MSIsImh0dHBzOi8vb3BlbmFpLm9wZW5haS5hdXRoMGFwcC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjgyMzU4NDAyLCJleHAiOjE2ODM1NjgwMDIsImF6cCI6IlRkSkljYmUxNldvVEh0Tjk1bnl5d2g1RTR5T282SXRHIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCBtb2RlbC5yZWFkIG1vZGVsLnJlcXVlc3Qgb3JnYW5pemF0aW9uLnJlYWQgb2ZmbGluZV9hY2Nlc3MifQ.gdiTwwZk5Arpc15cWunVROThJXpa1aDUmkIeY-QgtuUF8sO14Zoe7GgLKJdQUnN318YRwOurXjzpYLHozrgYeW87yq3xP2kyZhLJsx9eA4aLJyU6bGrnguxKR7cuHieOFGJki_kvYCoWuFmMgrdhU0HrNxRsbVuLZ7upTy02h7VPZqIOagqqrL2f1eVqEK60ewETXVibEfSNkY4UiE4DyN9EaaSlU97n5qAmIk_n1eG6q5J64xnyX-q1EMqIf7sAwi_mqxhRna9p7ZG3KdJjYkZr9F9jH5bH_apvAZT5Zbtf6jZhwebmHCPqC7w2FYUhFpzwMmGsn-rzX38-bHItFQ"
})

sem = BoundedSemaphore(1)    # only allows 1 greenlet at one time, others must wait until one is released


@app.route('/chatgpt', methods=['GET', 'POST'])
def link_receiver():
    data = request.json

    if sem.ready():
        sem.acquire()
        response = ""
        for data in chatbot.ask(data["text"]):
            response = data["message"]
        sem.release()
        return response
    return abort(500)


if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 8060)
                             , app, handler_class=WebSocketHandler)
    http_server.serve_forever()
