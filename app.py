from flask import Flask, render_template, request
import random

app = Flask(__name__,
            static_folder='templates',
            static_url_path='/static')

base_grid = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],

    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],

    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9],
]
def generate_puzzle():
    grid = []
    for row in base_grid:
        grid.append(list(row))
    for _ in range(40):
        row=random.randint(0,8)
        col=random.randint(0,8)

        grid[row][col] = 0

    return grid

@app.route("/")
def home():
    return render_template("index.html", grid=None)

@app.route("/game")
def game():
    grid = generate_puzzle()
    return render_template("index.html", grid=grid)

@app.route("/check", methods=["POST"])
def check():
    errors = 0

    for row in range(9):
        for col in range(9):
            field_name = f"cell_{row}_{col}"
            value = request.form.get(field_name, "")

            if str(base_grid[row][col]) != value:
                errors += 1

    if errors == 0:
        return render_template("index2.html")
    else:
        return render_template("index3.html")

if __name__ == "__main__":
    app.run(debug=True)
