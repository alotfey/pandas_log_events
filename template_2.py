from jinja2 import Environment, FileSystemLoader
import pandas as pd

# Create DataFrame
data = {
    'Name': ['John Doe', 'Jane Smith', 'Bob Johnson', 'Alice Williams'],
    'Age': [45, 55, 30, 60],
    'Position': ['Manager', 'CEO', 'Clerk', 'CTO'],
    'Salary': [5000, 8000, 3000, 7000]
}
df = pd.DataFrame(data)

# Load Jinja2 template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('mytemplate.html')

# Render template with data
output = template.render(df=df)

# Write to file
with open('output.html', 'w') as f:
    f.write(output)
