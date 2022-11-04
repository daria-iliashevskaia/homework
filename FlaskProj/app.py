from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from config import Config


# настройка приложения и соединения с БД
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


# создание модели "сотрудники" БД
class Employees(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))


# обработчик для главной страницы, выводит список всех сотрудников из БД
@app.route('/')
def index():
    employees = Employees.query.all()
    return render_template('index.html', title='Главная', employees=employees)


# обработчик для ввода информации о новом сотруднике, сохраняет введённую инфо в БД
@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        res = request.form.to_dict()
        employee = Employees(
            name=res['name'],
            email=res['email'],
            phone=res['phone']
        )
        db.session.add(employee)
        db.session.commit()
        return redirect('/')

    return render_template('index.html', title='Главная')


# обработчик для изменения информации о сотруднике, редактирует информацию в БД
@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        res = request.form.to_dict()
        employee = Employees.query.get(res['id'])

        employee.name = res['name']
        employee.email = res['email']
        employee.phone = res['phone']

        db.session.add(employee)
        db.session.commit()

        return redirect('/')

    return render_template('index.html', title='Главная')


# обработчик для удаления записи о сотруднике
@app.route('/delete/<employee_id>')
def delete(employee_id):
    res = Employees.query.get(employee_id)
    db.session.delete(res)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':

    # with app.app_context():
    #     db.create_all()

    app.run(debug=True)



