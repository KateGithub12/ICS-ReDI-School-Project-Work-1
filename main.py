from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []  # Create an empty list to store tasks

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)  # Pass tasks to the template

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        task_name = request.form.get('task')
        task = {'name': task_name, 'done': False}
        tasks.append(task)  # Append the new task to the tasks list
        return redirect('/')
    return render_template('index.html', tasks=tasks)

@app.route('/update/<int:task_id>')
def update(task_id):
    if task_id < len(tasks):
        task = tasks[task_id]
        task['done'] = not task['done']
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if task_id < len(tasks):
        del tasks[task_id]
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)

