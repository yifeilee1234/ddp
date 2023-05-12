from flask import Flask, render_template, request, redirect, url_for
import uuid

app = Flask(__name__)

# A simple in-memory store for tasks
tasks = []


@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if task:
        tasks.append({"id": str(uuid.uuid4()), "task": task})
    return redirect(url_for("index"))


@app.route("/delete/<task_id>")
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
