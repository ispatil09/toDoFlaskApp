# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 16:38:08 2022

@author: Ishwar
"""
#getbootstrap.com for web templates
#Use 'VS Code' IDE with 'Jinja2 template script..??' plugin installed

from flask import Flask
from flask import render_template, request #Direct page to .html file
from entity.AllEntity import ToDo, SaveData, LoadData


todo_list = LoadData().getAll()

app = Flask(__name__)


@app.route('/',methods=["GET","POST"])
def hello_world():
    if request.method=="POST":
        title = request.form["title"]
        desc = request.form["desc"]
        todo_list.append(ToDo(0, title, desc))
    return render_template('index.html',allToDo=todo_list) #File present in 'templates' folder

@app.route('/delete/<title>', methods=["GET"]) #call url - 'http://127.0.0.1:5000/products'
def delete(title):
    title=title[title.index('=')+1:]
    for todo in todo_list:
        if(todo.title==title):
            todo_list.remove(todo)
    print(todo_list)
    return render_template('index.html',allToDo=todo_list)

@app.route('/save', methods=["GET","POST","PUT"])
def save():
    SaveData(todo_list)
    return "Your ToDo Data is saved successfully.. You can exit()"
    

if __name__ == '__main__':
    app.run(debug=False, port=5000)