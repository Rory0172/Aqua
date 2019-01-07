from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello():
   return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    print(username)
    password= request.args.get('password')
    print(password)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()