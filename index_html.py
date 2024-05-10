def index_code(project_name):
    index_code ="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ML Project</title>
</head>
<body>
    <h1>Welcome to the Ml Project</h1>
</body>
</html>
"""
    file_path = f'{project_name}/templates/index.html'
    with open(file_path,'w') as file:
        file.write(index_code)