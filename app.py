from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mike')
def mike():
    return render_template('mike.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/estimate', methods=['GET'])
def estimate():
    return render_template('estimate.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        num1 = int(request.form['numOne'])
        num2 = int(request.form['numTwo'])
        tank_top = 3.14*(num1*num1)
        tank_sides = 2*(3.14*(num1*num2))
        total_area = tank_top + tank_sides
        total_area_sqft = total_area/144
        mat_cost = total_area_sqft*25
        labor_cost = total_area_sqft*15
        total_cost = mat_cost + labor_cost
        print(total_cost)
    return render_template('estimate.html', myValue=total_cost)


if __name__ == '__main__':
    app.run(debug=True)



