from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def render_main():
	return render_template('index.html')

@app.route('/departures/<departure>')
def render_departures(departure):
	return render_template('departure.html')

@app.route('/tours/<int:id>/')
def render_tours(id):
	return render_template('tour.html')

@app.route('/test/<role>')
def render_test(role):
	return render_template('test2.html', role="admin")

@app.route('/base/')
def render_base():
	return render_template('base2.html')

app.run()