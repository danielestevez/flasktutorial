from app import app

@app.route('/') #decorator here to create mappings for uris
@app.route('/index')
def index():
	return "Hello, World!"
