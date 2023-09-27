from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('council.html')
@app.route('/codefest')
def codefest():
    return render_template('codefest.html')
if __name__ == '__main__':
    app.run(debug=True)
