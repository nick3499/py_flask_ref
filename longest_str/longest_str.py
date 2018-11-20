from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def longest_str():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    n = 0
    for i in range(len(days)):
        if len(days[i]) > n:
            n = len(days[i])
    return render_template("longest_str.html", longest=n)

if __name__ == '__main__':
    app.run(debug=True)
