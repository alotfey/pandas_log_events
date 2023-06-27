from jinja2 import Environment, FileSystemLoader
import pandas as pd

# Create DataFrame
data = {
    'Title': ['Book1', 'Book2', 'Book3'],
    'Author': ['Author1', 'Author2', 'Author3'],
    'Genre': ['Genre1', 'Genre2', 'Genre3'],
    'Rating': [4.2, 3.7, 4.8]
}
df = pd.DataFrame(data)

# Load Jinja2 template
env = Environment(loader=FileSystemLoader('.'))
table_template = env.get_template('table.html')
cards_template = env.get_template('cards.html')
main_page_template = env.get_template('main_page.html')

# Render table and cards templates with data
table_html = table_template.render(df=df)
cards_html = cards_template.render(df=df)

# Render main page template with table and cards HTML
output = main_page_template.render(table=table_html, cards=cards_html)

# Write to file
with open('output.html', 'w') as f:
    f.write(output)
