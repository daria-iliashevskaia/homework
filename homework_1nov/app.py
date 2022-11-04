from flask import Flask, render_template, request

app = Flask(__name__)


# обработчик для просмотра страницы пользователя с использованием шаблона
@app.route('/users/<int:id>')
def users(id):
    return render_template(
        'users/show.html',
        id=id
    )


# обработчик для вывода списка пользователей с возможностью фильтрации
@app.route('/users')
def all_users():
    users = ['mike', 'mishel', 'adel', 'keks', 'kamila']
    term = request.args.get('term')
    if term is None:
        return render_template(
            'users/index.html',
            users=users
        )
    else:
        filtered_users = filter(lambda x: term in x, users)
        return render_template(
            'users/index.html',
            users=filtered_users,
            search=term
        )


app.run(debug=True)
