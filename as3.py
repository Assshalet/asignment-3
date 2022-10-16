from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def NFT():
    return "<p>NFT</p>"



@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('aaaa.html', name=name)

# allow both GET and POST requests
@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        name = request.form.get('name')
        framework = request.form.get('framework')
        return '''
                  <h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>Name <input type="text" name="language"></label></div>
               <div><label>Framework: <input type="text" name="framework"></label></div>
               <input type="submit" value="Submit">
           </form>'''

if __name__ == '__main__':
    app.run(debug=True) #