from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def add_sub_psngr():
    lst = [[10,0],[3,5],[5,8]]
    remaining = sum([e[0] - e[1] for e in lst])
    return render_template("add_sub_passengers.html", remaining=remaining)

if __name__ == '__main__':
    app.run(debug=True)
