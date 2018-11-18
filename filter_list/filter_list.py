from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def filter_list():
    l = [1, 2, 'a', 'b']
    f = list(filter(lambda x: type(x) == int, l))
    return render_template("filter_list.html", filtered=f)

if __name__ == '__main__':
    app.run(debug=True)

# print(filter_list([1, 2, 'a', 'b']), [1, 2])
# print(filter_list([1, 'a', 'b', 0, 15]), [1, 0, 15])
# print(filter_list([1, 2, 'aasf', '1', '123', 123]), [1, 2, 123])
