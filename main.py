from flask import Flask, render_template, request, redirect, url_for
import models.sqlOperator as sqlOperator

app = Flask(__name__)


@app.route("/")
def index():
    all_message = sqlOperator.get_all_message()
    messageNum = len(all_message)
    return render_template('index.html', messageNum=messageNum, messageList=all_message)


@app.route("/addMessage", methods=['GET'])
def addMessage():
    sqlOperator.add_message(request.values.get('message'))
    return redirect(url_for('index'))


@app.route("/editMessage", methods=['GET'])
def editMessage():
    editOp = str(request.values.get('editOp'))

    id = int(request.values.get('id'))
    if editOp == 'true':
        sqlOperator.update_message(id, 1)
    elif editOp == 'false':
        sqlOperator.update_message(id, 2)
    elif editOp == 'delete':
        sqlOperator.delete_one_message(id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
