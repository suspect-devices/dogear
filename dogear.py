from flask import Flask, request, url_for, render_template
#from sqlalchemy import create_engine

app = Flask(__name__)
#engine = create_engine('sqlite:///:memory:', echo=True)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/add', methods=['GET','POST'])
def add_url():
    if request.method == 'GET':
        return render_template('add.html')
    else:
        print request.form['url_to_save']
        print request.form['notes']
        print request.form['tags']
        return render_template('add.html')

@app.route('/add/<url_to_save>')
def remote_add_url(url_to_save):
    return url_to_save

if __name__ == '__main__':
    app.run(debug=True)
