from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def high_adj_num_prod():
    arr = [3, 6, -2, -5, 7, 3]
    product = arr[0] * arr[1]
    for i in range(len(arr)-1):
        if (arr[i] * arr[i+1]) > product:
            product = arr[i] * arr[i+1]
    return render_template("highest_adj_el_product.html", highest=product)

if __name__ == '__main__':
    app.run(debug=True)
