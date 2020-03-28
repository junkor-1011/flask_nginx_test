#!/usr/bin/env python

import json, io, datetime, codecs, os, random
from uuid import uuid4
from hashlib import md5


from flask import Flask, render_template, request, jsonify, make_response,\
    send_file, session, abort, flash, url_for, redirect



app = Flask(__name__)

app.secret_key = md5(str(uuid4()).encode()).hexdigest()


@app.route('/')
def index():
    now = datetime.datetime.now().strftime('%H:%M:%S.%f')
    return f'<h2>hello world <br> time:({now})</h2>\n'


@app.route('/tmp')
def sample():
    now = datetime.datetime.now().strftime('%H:%M:%S.%f')
    return f'<h1>tmp({now})</h1>\n'


@app.route('/test', methods=['GET'])
def test():
    title = "test-page"
    return render_template('test.html', title=title)


if __name__ == '__main__':
    app.debug = True
    app.run(
            #host='0.0.0.0',
            #port=5000,
            #ssl_context=('ssl/server.crt', 'ssl/server.key'),
            #threaded=True,        
    )
