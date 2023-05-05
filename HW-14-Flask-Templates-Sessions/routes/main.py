import hashlib
from app import app, db
from flask import render_template, request, redirect, session, abort
from models import User, Post

@app.route("/")
def hello_world():
    if session.get("user"):
        posts = Post.query.filter_by(user_id=session.get("user").get("id")) or [None]
        print("POST: =========================", posts)
    else:
        posts = Post.query.all()
    return render_template("index.html", posts=posts, User=User)

@app.route("/sign-up")
def sign_up():
    return render_template("sign-up.html")

@app.route("/save-user", methods=["POST"])
def register():
    data = request.form
    password_hash = hashlib.sha256(data.get("password").encode("utf-8"))
    user = User(
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        email=data.get("email"),
        password=password_hash.hexdigest(),
    )
    db.session.add(user)
    db.session.commit()
    session["user"] = user.serialize
    return redirect("/")

@app.route("/sign-in")
def sign_in():
    return render_template("sign-in.html")

@app.route("/authorize", methods=["POST"])
def authorize():
    data = request.form
    user = User.query.filter(User.email == data.get("email")).first()
    if user:
        if hashlib.sha256(data.get("password").encode("utf-8")).hexdigest() == user.password:
            session["user"] = user.serialize
    return redirect("/")

@app.route("/logout")
def logout():
    del session["user"]
    return redirect("/")

@app.route("/create-post")
def create_post():
    if session.get("user"):
        return render_template("create-post.html")
    else:
        return abort(401)

@app.route("/save-post", methods=["POST"])
def save_post():
    data = request.form
    user = User.query.filter_by(id=session.get("user").get("id")).first()
    if user:
        post = Post(
            user_id=user.id,
            title=data.get('title'),
            content=data.get('content')
        )
        db.session.add(post)
        db.session.commit()
        return redirect("/")
    else:
        return abort(401)

@app.route("/post/<int:id>")
def view_post(id):
    id = int(id)
    post = Post.query.get(id)
    if post:
        return render_template("post.html", post=post)
    else:
        return abort(404)

@app.route("/post/<int:id>/edit")
def edit_post(id):
    id = int(id)
    post = Post.query.get(id)
    if session.get("user") and post.user_id == session.get("user").get("id"):
        return render_template("edit-post.html", post=post)
    else:
        return abort(401)

@app.route("/post/<int:id>/update", methods=["POST"])
def update_post(id):
    id = int(id)
    data = request.form
    post = Post.query.get(id)
    if session.get("user") and post.user_id == session.get("user").get("id"):
        post.title = data.get("title")
        post.content = data.get("content")
        db.session.commit()
    return redirect("/")

@app.route("/post/<int:id>/delete")
def delete_post(id):
    id = int(id)
    post = Post.query.get(id)
    if session.get("user") and post.user_id == session.get("user").get("id"):
        db.session.delete(post)
        db.session.commit()
    return redirect("/")
