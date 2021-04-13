from flask import render_template


class HomeController():
    def __init__(self):
        pass

    def index(self):
        user = {'nombre': 'Josue'}
        return render_template('index.html', user=user)


homecontroller = HomeController()
