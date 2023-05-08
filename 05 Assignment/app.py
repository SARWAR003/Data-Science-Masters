from flask import Flask, render_template
from bokeh.embed import server_document

app = Flask(__name__)

@app.route('/')
def index():
    # generate a URL to the Bokeh server application
    bokeh_url = server_document('http://localhost:5006/myapp')
    # pass the URL to the template and render it
    return render_template('index.html', bokeh_url=bokeh_url)

if __name__ == '__main__':
    app.run(debug=True)


