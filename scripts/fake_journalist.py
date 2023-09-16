from faker import Faker
import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutorialproject.settings')

import django
django.setup()
import requests
from news.api.serializers import JournalistSerializer

def fake_journalist(content):
    fake=Faker('en_US')
    url='https://openlibrary.org/search.json?'
    payload={'q':content}    
    response=requests.get(url,params=payload)
    jsn=response.json()
    books=jsn.get('docs')
    for book in books:
        author=book.get('author_name')[0]
        last_name=fake.last_name()
        bio=fake.paragraph(nb_sentences=1)
        data=dict(
            first_name=author,
            last_name=last_name,
            biography=bio,
        )

        serializer=JournalistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            raise(serializer.errors)