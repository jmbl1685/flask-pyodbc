from server import app, render_template, request, jsonify
from config.db import cursor

@app.route('/page', methods=['GET'])
def Index():

    info = {
        'title': 'My Title',
        'message': 'OK'
    }

    html = render_template('index.html',
                           info=info)
    return html


@app.route('/', methods=['POST'])
def Post():
    body = request.json
    print(body['candidateName'])
    return jsonify(body)


@app.route('/user')
@app.route('/user/<user_id>')
def Get(user_id=None):

    cursor.execute(
        'SELECT Id,FullName, UserName, Email, Password, Avatar FROM [TechnologyApp].[Users]')
    row = cursor.fetchone()

    users = []

    while row:
        user = {
            'Id': row[0],
            'FullName': row[1],
            'UserName': row[2],
            'Email': row[3],
            'Password': row[4],
            'Avatar': row[5]
        }
        users.append(user)
        row = cursor.fetchone()

    # print(f'Value: {user_id}')
    # print(request.args.get('username'))
    return jsonify(users)
