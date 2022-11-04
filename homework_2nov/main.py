from Models import *


def user_date():

    with open('users.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    users = []

    for d in data:
        user = User(id=d['id'],
                    first_name=d['first_name'],
                    last_name=d['last_name'],
                    age=d['age'],
                    email=d['email'],
                    role=d['role'],
                    phone=d['phone']
                    )
        users.append(user)

    return users


def order_date():
    with open('orders.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    orders = []

    for d in data:
        order = Order(id=d['id'],
                    name=d['name'],
                    description=d['description'],
                    start_date=d['start_date'],
                    end_date=d['end_date'],
                    address=d['address'],
                    customer_id=d['customer_id'],
                    executor_id=d['executor_id']
                    )
        orders.append(order)

    return orders


if __name__ == "__main__":

    with app.app_context():

        db.drop_all()
        db.create_all()

        users = user_date()
        db.session.add_all(users)
        db.session.commit()

        orders = order_date()
        db.session.add_all(orders)
        db.session.commit()