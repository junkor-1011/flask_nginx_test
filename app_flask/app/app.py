#!/usr/bin/env python

import json, io, datetime, codecs, os, random
from uuid import uuid4
from hashlib import md5, sha256


from flask import Flask, render_template, request, jsonify, make_response,\
    send_file, session, abort, flash, url_for, redirect



app = Flask(__name__)

app.secret_key = md5(str(uuid4()).encode()).hexdigest()     # 要らないかも?
app.config['SECRET_KEY'] = sha256(str(uuid4()).encode()).hexdigest()


@app.before_request
def before_request():
   if request.path.startswith('/static/'):
       return
   if session.get('username') is not None:
       return
   if request.path == '/login':
       return
   return redirect('/login')


@app.errorhandler(401)
def unauthorized_error_handle(error):
    return render_template('401.html'), 401


@app.route('/', methods=['get'])
def site_root():
    return redirect("/menu")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and _is_account_valid():
        uid = request.form['uid']
        username, setting = _get_user_info(uid)
        session['uid'] = uid
        session['username'] = username
        session['setting'] = setting

        return redirect(url_for('menu'))    # auth success
    elif request.method == 'POST' and (not _is_account_valid()):
        abort(status=401)

    else:
        title = "login"
        return render_template('login.html', title=title)


@app.route('/logout')
def logout():
    session.pop('uid', None)
    session.pop('username', None)
    session.pop('setting', None)
    return redirect(url_for('login'))


@app.route('/menu', methods=['GET'])
def menu():
    title = "Main Menu"
    return render_template('menu.html', title=title)

#@app.route('/')
#def index():
#    now = datetime.datetime.now().strftime('%H:%M:%S.%f')
#    return f'<h2>hello world <br> time:({now})</h2>\n'


@app.route('/tmp')
def sample():
    now = datetime.datetime.now().strftime('%H:%M:%S.%f')
    return f'<h1>tmp({now})</h1>\n'


@app.route('/test', methods=['GET'])
def test():
    title = "test-page"
    return render_template('test.html', title=title)


def _is_account_valid():    # TMP
    uid = request.form.get('uid')
    pwd = request.form.get('pwd')
    if uid == 'admin' and pwd == 'pwd':
        # auth-success
        return True

    # auth-failed
    return False


def _get_user_info(uid):
    """
    uidをキーにしてDataBaseから諸々の必要情報を引っ張ってくるイメージ

    :arg
    """
    # TMP   暫定処置
    name = uid      # ToDo: DBから持ってくるようにする
    setting = {}    # ToDO: DBから持ってくるようにする
    return name, setting


if __name__ == '__main__':
    app.debug = True
    app.run(
            #host='0.0.0.0',
            #port=5000,
            #ssl_context=('ssl/server.crt', 'ssl/server.key'),
            #threaded=True,        
    )
