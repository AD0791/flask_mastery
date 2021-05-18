from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html",name="MR Davidson")

if __name__ == '__main__':
    app.run(port=1300,debug=True)



