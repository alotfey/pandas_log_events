import os
import pandas as pd
from django.template.loader import render_to_string
from django.conf import settings

# Set Django settings module environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'my_project.settings'  # replace with your project's settings

# Init Django
settings.configure()

# Create DataFrame
data = {
    'Title': ['Book1', 'Book2', 'Book3'],
    'Author': ['Author1', 'Author2', 'Author3'],
    'Genre': ['Genre1', 'Genre2', 'Genre3'],
    'Rating': [4.2, 3.7, 4.8]
}
df = pd.DataFrame(data)

# Render table and cards templates with data
table_html = render_to_string('table.html', {'df': df})
cards_html = render_to_string('cards.html', {'df': df})

# Render main page template with table and cards HTML
main_page_html = render_to_string('main_page.html', {'table': table_html, 'cards': cards_html})

# Write to file
with open('output.html', 'w') as f:
    f.write(main_page_html)
