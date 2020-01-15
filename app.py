from flask import Flask, render_template, request
from wsd import findMeaning

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def wsd():
    if request.method == 'POST':
        data = request.form.get('text')
        output = findMeaning(data)
        return render_template('index.html', prediction = 'Context : {}'.format(output))
    return render_template('index.html', prediction = '')

if __name__ == "__main__":
    app.run(port = 3000, debug=False)