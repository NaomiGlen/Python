from flask import Flask, render_template,redirect,flash,request,session
from flask_app import app
from flask_app.models.post import Post

@app.route("/posts", methods=["POST"])
def create_post():
    print("Post has been created")
    print(request.form)
    Post.save(request.form)
    return redirect('/dashboard')

@app.route('/posts/delete/<post_id>')
def delete_post(post_id):
    print("Post has been deleted")
    Post.delete(post_id)
    return redirect('/dashboard')