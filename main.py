from flask import Flask, flash, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = b'fdgfdgtftgf'

cars = [
  {'id':1, 'brand': 'Toyota', 'model': 'Yaris Ative', 'year': 2024, 'price': 620000},
  {'id':2, 'brand': 'Toyota', 'model': 'Yaris Cross', 'year': 2025, 'price': 850000},
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
    if length>0:
      id = cars[length-1]['id'] + 1
    else:
      id = 1

    car ={'id':id, 'brand': brand, 'model': model, 'year': year, 'price': price}

    cars.append(car)
    flash('Add new car successfully', 'success')

    return redirect(url_for('show_cars'))

  return render_template('car/new_car.html',
                        title='New Car Page')


@app.route('/cars/<int:id>/edit', methods=['GET','POST'])
def edit_car(id):
  for c in cars:
    if id == c['id']:
      car = c
      break

  if request.method == 'POST':     #กดsubmit 
    brand = request.form['brand']
    model = request.form['model']
    year = int(request.form['year'])
    price =int(request.form['price'])
    # id =int(request.form['id'])

    for car in cars:
      if id == car['id']:
        car['brand'] = brand
        car['model'] = model
        car['year'] = year
        car['price'] = price
        flash('Update car successfully', 'success')
        break

    return redirect(url_for('show_cars'))

  return render_template('car/edit_car.html',
                        title='Edit Car Page',
                        car=car)

@app.route('/cars/<int:id>/delete')
def delete_car(id):
  for car in cars:
    if id == car['id']:
      cars.remove(car)
      flash('Delete car successfully', 'success')
      break

  return redirect(url_for('show_cars'))


@app.route('/cars/search')
def search_car():
  brand = request.args.get('brand','').lower()
  tmp_cars = []
  for car in cars:
    if brand in car['brand'].lower():
      tmp_cars.append(car)
  
  return render_template('car/search_cars.html',
                        title='Search Car Page',
                        cars=tmp_cars)