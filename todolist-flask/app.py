from flask import Flask,request,url_for,redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:tryhackme8@localhost:5432/todolist"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Tasks(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String)
    def __repr__(self):
        return '%s' % self.task

with app.app_context():
    db.create_all()


@app.route('/')
def hello_world():  # put application's code here
    return render_template('home.html')


@app.route('/todolist', methods=('GET', 'POST'))
def todo_list():
    if request.method == 'POST':
        tk = request.form["task"]
        new_task = Tasks(task = tk)
        db.session.add(new_task)
        db.session.commit()
        tasks = Tasks.query.all()
        return render_template('todolist.html', task = tasks)
    return render_template('todolist.html', task = Tasks.query.all())
    

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Tasks.query.get_or_404(id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect('/'+'todolist')


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Tasks.query.get_or_404(id)
    if request.method == 'POST':
        task.task = request.form['update']
        db.session.commit()
        return redirect('/'+'todolist')
    else:
        return render_template('update.html', task = task)


if __name__ == '__main__':
    app.run(debug=True)
