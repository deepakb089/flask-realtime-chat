from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True

@app.route("/")
def show_chat_page():
	return render_template("chat.html")
	
if __name__ == "__main__":
	app.run()
