from flask import Flask, render_template

app = Flask(__name__)


@app.route('/list_prof/<list_>')
def list_prof(list_):
    profs = ['пилот',
             'инженер',
             'врач',
             'учитель',
             'климатолог',
             'штурман',
             'пилот дронов',
             'киберинженер',
             'программист',
             'администратор']
    return render_template('base.html', lst=list_, profs=profs)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
