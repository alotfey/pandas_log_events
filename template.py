from jinja2 import Environment, FileSystemLoader
import pandas as pd

# Load data
df = pd.read_csv('mydata.csv')

# Load Jinja2 template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('mytemplate.html')

# Render template with data
output = template.render(df=df)

# Write to file
with open('output.html', 'w') as f:
    f.write(output)
