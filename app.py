from bottle import route, run, template, request, response, static_file
import numpy as np
import json
import life

game_state = None


@route('/')
def index():
    return template('index', title="Главная страница")


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static/')


@route('/the_spread_of_lichen')
def the_spread_of_lichen():
    return template('the_spread_of_lichen', title="Распространение лишая")


@route('/Wolf_island')
def the_spread_of_lichen():
    return template('Wolf_island', title="Волчий остров")


run(host='localhost', port=8080)
