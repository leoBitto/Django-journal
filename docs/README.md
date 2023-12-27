# Journal


Journal is a Django app used to keep a journal.
it uses Quill `https://quilljs.com/` and Django 5.0 . 
-----------

## Quick start
0. git submodule add https://github.com/leoBitto/journal.git
00. pip install django_quill

1. Add "journal" to your setting.py like this:

    ```
    INSTALLED_APPS - [
        ...
        'django_quill',
        'journal',
    ]
    ```


2. Include the journal URLconf in your project urls.py like this:

    > path('journal/', include(('journal.urls', 'journal'), namespace="journal")),

3. Run ``python manage.py migrate journal`` to create the journal models.

-----------

# journal docs                       
if you want to use the article links outside the app you need to use the namespace.
it is always a good idea when having many apps inside a Django project to use the namespace.
for example:

    > <a href="{% url 'journal:article' slug=article.slug  %}"</a>

