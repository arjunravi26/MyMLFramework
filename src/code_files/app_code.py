def app_code(project_name):
    app_code = """from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    """
    with open(f"{project_name}/app.py", "w") as file:
        file.write(app_code)

