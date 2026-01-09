from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

cars = [
  {'id':1, 'brand': 'Toyata', 'model': 'Yaris Ative', 'year': 2024, 'price': 620000},
  {'id':2, 'brand': 'Toyata', 'model': 'Yaris Cross', 'year': 2025, 'price': 850000},
  {'id':3, 'brand': 'Mitsubishi', 'model': 'X-Force', 'year': 2025, 'price': 860000}
]

@app.route('/')
def index():
  return render_template('index.html',
                        title='Home Page')

@app.route('/cars')
def show_cars():
  return render_template('car/cars.html',
                        title='Cars Page',
                        cars=cars)

@app.route('/cars/new', methods=['GET', 'POST'])
def new_car():
  if request.method == 'POST':     #กดsubmit 
    brand = request.form['brand']
    model = request.form['model']
    year = int(request.form['year'])
    price =int(request.form['price'])

    length = len(cars)
    id = cars[length-1]['id'] + 1

    car ={'id':id, 'brand': brand, 'model': model, 'year': year, 'price': price}

    cars.append(car)

    return redirect(url_for('show_cars'))

  return render_template('car/new_car.html',
                        title='New Car Page')

