from flask import Flask, render_template, request, redirect, url_for
from database import db_session, init_db
from models import Bug
import datetime

app = Flask(__name__)



@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def index():
    bugs = db_session.query(Bug).all()
    return render_template('index.html', bugs=bugs)

@app.route('/create', methods=['GET', 'POST'])
def create_bug():
    if request.method == 'POST':
        title = request.form['title']
        new_bug = Bug(title=title)
        db_session.add(new_bug)
        db_session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/edit/<int:bug_id>', methods=['GET', 'POST'])
def edit_bug(bug_id):
    bug = db_session.get(Bug, bug_id)
    if request.method == 'POST':
        bug.title = request.form['title']
        bug.status = request.form['status']
        if bug.status == 'Done' and bug.completion_date is None:
            bug.completion_date = datetime.datetime.now(datetime.UTC)
        elif bug.status != 'Done':
            bug.completion_date = None
        db_session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', bug=bug)

@app.route('/update_status/<int:bug_id>', methods=['POST'])
def update_status(bug_id):
    bug = db_session.get(Bug, bug_id)
    if bug:
        bug.status = request.form['status']
        if bug.status == 'Done' and bug.completion_date is None:
            bug.completion_date = datetime.datetime.now(datetime.UTC)
        elif bug.status != 'Done':
            bug.completion_date = None
        db_session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:bug_id>', methods=['POST'])
def delete_bug(bug_id):
    bug = db_session.get(Bug, bug_id)
    db_session.delete(bug)
    db_session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5001)