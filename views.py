from django.shortcuts import render
import pandas as pd

def book_view(request):
    # Create DataFrame
    data = {
        'Title': ['Book1', 'Book2', 'Book3'],
        'Author': ['Author1', 'Author2', 'Author3'],
        'Genre': ['Genre1', 'Genre2', 'Genre3'],
        'Rating': [4.2, 3.7, 4.8]
    }
    df = pd.DataFrame(data)

    context = {'df': df}

    return render(request, 'main_page.html', context)
