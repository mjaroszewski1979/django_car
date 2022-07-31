## MJ Cars
### This is a Django application powered by HTMX to assist in building rich client-side experience. It will allow users to register and authenticate with google account. Once logged in you can create your own list of favorite cars and upload an image. Thanks to implementing drag-and-drop reordering there is also a possibility of dynamically changing order of elements which is automatically reflected in database.

--------------------------------------------------

### Features:
* Working with template inheritance mechanism to build a base “skeleton” template that contains all the common elements and defines blocks that child templates can override
* Applying LoginRequiredMixin to ensure that the requesting user is authenticated
* Taking full advantage of HTMX - dependency-free library to access modern browser features directly from HTML, rather than using javascript
* Configuring Django to load and serve up user uploaded media files via an Amazon S3 bucket
* Managing user authentication using the django-allauth package, which allows login and registration using Social Accounts, like Google
* Breaking logic into smaller parts by adding various new Django applications to an existing project 
* Implementing Django's built-in features like cross-site request forgery protection to ensure safe data transfer in web forms to a database
* Storing app’s secure credentials in environment variables
* Writing as much functionality as possible in models or utility files instead of views
* Setting-up sphinx-apidoc to automatically build a nice module index with links to documentation generated from the docstrings
* Utilizing setUp method to handle especially expensive setup operations for all of the tests within a module
* Performing extensive selenium tests using 'page object pattern' instead of making raw WebDriver calls to have cleaner code:
  * Utilizing DRY (Don’t repeat yourself) principle to minimize code duplication by having all ID-locators in one place
  * Setting an interface between web page’s elements and tests
  * Avoiding usage of WebDriver APIs in test methods
  * Encapsulating the services of web pages, not only exposing their elements

--------------------------------------------------

### Code Coverage:


<img src="https://github.com/mjaroszewski1979/django_car/blob/main/cov_report.png">


--------------------------------------------------

![caption](https://github.com/mjaroszewski1979/django_car/blob/main/mjcars_mockup.png)
  
  Live | Code | Docs | Docker | Technologies
  ---- | ---- | ---- | ------ | ------------
  [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/heroku_g.png">](https://django-mjcars.herokuapp.com/) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/github_g.png">](https://github.com/mjaroszewski1979/django_car) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/sphinx.png">](https://djangocarsdocs.netlify.app/) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/docker_compose.png">](https://github.com/mjaroszewski1979/django_car/blob/main/docker-compose.yml) | <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/python_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/django_g.png">  &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/amazon_s3.png">  &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/htmx.png">  &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/html_g.png"> <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/css_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/htmlup.png"> &nbsp; &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/js1.png"> 
