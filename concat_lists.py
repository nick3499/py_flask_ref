from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def concat_lists():
    l1 = [1, 2, 3, 4]
    l2 = [5, 6, 7, 8]
    l3 = sorted(list(set(l1 + l2)))
    return render_template("concat_lists.html", concatenated=l3)

if __name__ == '__main__':
    app.run(debug=True)
