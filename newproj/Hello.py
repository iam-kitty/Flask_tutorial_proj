
from flask import Flask,redirect,url_for
app = Flask(__name__)


@app.route('/hello/<name>')
def hello_world(name1):
   return 'hello world %s!' % name1
#app.add_url_rule('/','hello',hello_world)


@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'blog no: %d'% postID

@app.route('/rev/<float:Revno>')
def show_no(Revno):
    return 'revno: %f' %Revno

@app.route('/python/')
def hello_python():
    return 'hello python'

@app.route('/flask')
def hello_flask():
    return 'hello flask'

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest



@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest = name))

if __name__ == '__main__':
    app.run(debug=True)
