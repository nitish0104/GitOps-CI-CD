from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock todo list for demonstration
todo_list = [
    {"id": 1, "task": "Buy groceries"},
    {"id": 2, "task": "Finish coding"},
    {"id": 3, "task": "Go for a run"},
]

@app.route('/')
def index():
    return render_template('index.html', todo_list=todo_list)

@app.route('/add', methods=['POST'])
def add():
    new_task = request.form.get('task')
    if new_task:
        todo_list.append({"id": len(todo_list) + 1, "task": new_task})
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    global todo_list
    todo_list = [task for task in todo_list if task['id'] != task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
