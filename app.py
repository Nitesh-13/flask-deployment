from flask import Flask, render_template, send_file

app = Flask(__name__, template_folder="templates")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/test")
def test():
    with open("test.txt") as f:
        f.write("Hello world")
    return send_file("test.txt")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)