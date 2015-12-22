# Online_Book_Store-Database
<h4>Database project in SUTD, Singapore</h4>
Thanks to Prof Meihui Zhang's kind guidance.
  
#Django + Python Based
* This project was created in Ubuntu 14.04
* We use a low version of Django--0.96.5. 
* The root path is /Sutd/Database/OnlineBookStore, where the Django environment is created. Under the root file, there are 3 files contained, one for the app `bookstore`, one for the Django environment `env`, and the last one `part1`, using python to create the database `try_01` and insert different kinds of books into it.
* In the web app `bookstore`, the `basic html` stores the fundamental html files only with a style.css connected to it . The file `templates` has the htmls we would like to use in the server.
* Developing server is running at `localhost:8000/`
  
#Running Instruction
* ```$cd Sutd/Database/OnlineBookStore```<br>
  ```$source env/bin/activate```<br>
  ```$cd bookstore```<br>
  ```$python manage.py runserver```<br>
* Open the Firefox browser, input `localhost:8000/`
