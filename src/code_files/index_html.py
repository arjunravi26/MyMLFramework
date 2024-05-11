def index_code(project_name):
    index_code ="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ML Project</title>
</head>
<body>
    <h1>Welcome to the ML Project</h1>
</body>
</html>
"""
    with open(f'{project_name}/templates/index.html', 'w') as file:
        file.write(index_code)
