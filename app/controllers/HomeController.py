from flask import render_template


class HomeController():
    def __init__(self):
        pass

    def index(self):
        """ user = {'nombre': 'Josue'}
        return render_template('index.html', user=user) """
        from app.models.User import User
        users = User.query.all()
        return render_template('index.html', users=users)


homecontroller = HomeController()
