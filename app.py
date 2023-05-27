from bottle import route, run, template, request, response, static_file
import numpy as np
import json
import life

game_state = None


@route('/')
def index():
    return template('index')


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static/')


run(host='localhost', port=8080)
