from flask import Flask,render_template

app = Flask(__name__)

all_posts = [
    {
        'title':'post1',
        'content':'this is the content of post 1, LALALALA.',
        'author':'kitty'
    },
    {
        'title':'post1',
        'content':'this is the content of post 2, LALALALA'
    }
]

@app.route('/home')
def index():
#return 'Home Page' #<h1>Home page </h1>
    return render_template('index.html')

@app.route('/post')
def posts():
    return render_template('posts.html',posts = all_posts )


@app.route('/home/users/<string:name>/posts/<int:id>')
def Hello(name,id):
    return 'Hello,'+ name + " your id is:"+str(id)

@app.route('/onlyget',methods=['POST']) #GET or POST
def get_req():
    return " you'll only get"



if __name__ == "__main__":
    app.run(debug=True)