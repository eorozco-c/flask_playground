from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times=5)	# observa los 2 nuevos argumentos nombrados!

@app.route('/play/<int:cant>')
def play(cant):
    return render_template("play.html", cantidad=cant)	# observa los 2 nuevos argumentos nombrados!

@app.route('/play/<int:cant>/<color>')
def play_2(cant,color):
    return render_template("index.html", cantidad=cant,color=color)	# observa los 2 nuevos argumentos nombrados!

if __name__=="__main__":
    app.run(debug=True)
