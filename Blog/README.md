# Mentored Project Week 3 Homework - Backend Intro

## Instructions

### Installing the Homework Code

1. Clone this repository to your computer and cd into the directory created.

2. Set up a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) with the command `python3 -m venv env`
   (Linux and Mac) or `virtualenv env` if you're on Windows.

3. Activate your virtual environment with `source env/bin/activate` (Linux and Mac) or `env\scripts\activate` (Windows). Your
   terminal's command prompt should now have a little `(env)` in front of it, so it goes from
   ```
   user@MY-COMPUTER:~$
   ```
   to
   ```
   (env) user@MY-COMPUTER:~$
   ```
   Note that from here on out we'll assume that you've activated your virtual environment - if you need to deactivate your virtual
   environment (for example, if you need to work on another project that uses Python) just type in the command `deactivate` (works on
   both Linux/Mac and Windows). You can always activate it again when you work on this code.

4. Once you've activated your virtual environment, install all of the project dependencies with the command
   ```
   pip install -r requirements.txt
   ```

### Running the Server

You'll need to run the server to see the website in action and check if your code works.

1. CD into the Django project directory with `cd bloggo`, then do `python manage.py runserver`.
2. View your website by opening up a web browser and going to `localhost:8000`.

### Submitting the Homework

Your submissions will be done through git. We'll automatically run tests against each git commit - you can see the results
of the tests by clicking on the checkmarks in your GitHub commit list. To commit and push your work to GitHub, do
```
git commit -am "<YOUR COMMIT MESSAGE HERE>"
```
and then
```
git push
```

If you don't want to wait for the autograder to see if your code works, you can run the tests manually with `python manage.py test`.

## Homework Questions

For this homework, we'll be building a blogging engine called "bloggo". The basic parts of the blog engine are already made
(you can view the blog as is by running the server and going to `localhost:8000/posts`),
but our client wants us to add some more features.

#### Reading

* [Django templates](https://tutorial.djangogirls.org/en/django_templates/) (Tutorial)
* [Template Extending](https://tutorial.djangogirls.org/en/template_extending/) (Tutorial)

### Question 1 - Static Pages and Templates

The first thing our client wants is an about page for their blog. Specifically, they want to be able to go to the URL
 `localhost:8000/posts/about` and view an about page, which should contain the following text:

> Bloggo is the best blog engine ever and it's gonna make me fifty trillion dollars!

The first thing you'll need to do is add the URL to the list of URLs in `bloggo/posts/urls.py`, because it doesn't exist yet.
Recall that a Django URL object looks like this:
```python
url(r'^the_url_for_the_view$', views.the_view_function, name="the_view_name")
```

The view functions are defined as regular functions right in `bloggo/posts/views.py`. For instance, for a function defined as `index`
 in views.py, you would put `views.index` as the view function in the URL object. Our client's code already has a (incomplete)
 view function for the about page, so you should use that.

The client also wants the about page to look nice, so use the existing template for it in `bloggo/posts/templates/posts/about.html`.
Right now the template is incomplete - you should make it extend the base template and add in the text from above that the client wants
the about page to show.

To see if your page works, run the server and go to the above URL. You should see the above text and also a page header linking to the main page.

You should now commit and push your code to GitHub. If you want to test your code for this question, do

```
python manage.py test posts.tests.AboutPage
```

#### Reading

* [Models in Django](https://tutorial.djangogirls.org/en/django_models/) (Tutorial) _Note: don't worry about "Creating an Application" because we have set that up for you already._
* [Introduction to Models in Django](https://docs.djangoproject.com/en/1.11/topics/db/models/) (Official Tutorial and Docs)
* [Querying Models in Django](https://tutorial.djangogirls.org/en/django_orm/) (Tutorial)
* [Dynamic Data in Templates](https://tutorial.djangogirls.org/en/dynamic_data_in_templates/) (Tutorial)

### Question 2 - Dynamic Views and Routes

The next thing the client wants is a unique URL to link to the details of every individual post in the blog.
Specifically, they want to be able to go to localhost:8000/posts/details/1 and see the title and text of the post with primary key 1,
localhost:8000/posts/details/4 and see the post with primary key 4, and so on.

#### The Post object

At this point you might be a little bit confused as to where all this post stuff came from. If you run the server and go to
localhost:8000/posts you'll see that the blog already has some posts in it! That is, our blog engine already comes with some
data included and a model for posts - the **Post** object in `bloggo/posts/models.py`. If you look in models.py, the Post object is
defined so that it has 3 fields - title (a character field), body (a text field), and pub_date (a date and time field). Django
makes it so that all models automatically get a hidden primary key (pk) field as well.

We can view all the existing Post objects by using the Django shell. In your terminal, run `python manage.py shell`.
In the interactive shell that comes up, run the following code:

```python
>>> from posts.models import Post
>>> all_posts = Posts.objects.all()
>>> print(all_posts)
```

This should output a list of all the posts so far (basically all the text in the main page of the blog right now).
You can view the single post with primary key 1 with the code

```python
>>> Post.objects.get(pk=1)
```

This should also do the same thing:

```python
>>> all_posts[0]
```

Note that this is all code you can use in your views too! All the code you type in the shell is code you can use in your
view functions as well. If you look in views.py, you'll see how the main page queries all the posts as well. It's helpful
to read through the view for that URL and the template to see how the main page gets all posts and displays them.

Add the right URL object in urls.py and edit the view so that it gets the Post object corresponding to the input `pk` and
renders a template with the post details (you'll need to create the template file yourself - name it whatever you want).

Once you finish, push your code to GitHub. You can manually test your code for this question with

```
python manage.py test posts.tests.PostDetailsPage
```
