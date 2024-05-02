from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return render_template("index.html", tasks=tasks)

@app.route('/add_task', methods=['POST'])
def create_task():
    task = request.form.get("task")
    if task:
        tasks.append(task)
    return redirect(url_for("home"))

@app.route('/delete/<int:index>')
def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
    return redirect(url_for('home'))

@app.route('/update/<int:index>', methods=['GET', 'POST'])
def update_task(index):
    if request.method == 'POST':
        new_task = request.form.get("task")
        if new_task:
            tasks[index] = new_task
        return redirect(url_for('home'))
    return render_template("update.html", index=index, task=tasks[index])

if __name__ == "__main__":
    app.run(debug=True)
