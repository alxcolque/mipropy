from flask import render_template
class PrincipalController():
    def __init__(self):
        pass

    def index(self):
        
        return render_template('welcome.html')


principalcontroller = PrincipalController()
