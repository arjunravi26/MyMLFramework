def app_code(project_name):
    app_code = """from flask import Flask, render_template

app = Flask(__name__)


# Creating route for index page
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
        """
    app_file_path = f"{project_name}/app.py"
    with open(app_file_path, "w") as file:
        file.write(app_code)
