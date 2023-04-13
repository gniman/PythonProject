from flask import Flask, render_template, request
app =Flask("ToDoApp")
@app.route('/')
def home():
    return render_template('index.html')
def landing1():
    return render_template('landing2.html')
@app.route('/history')
def history():
    return render_template('past-works.html')

