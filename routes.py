from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from app.posts import posts
from app import db
from app.models import Post


@posts.route("/create", methods=["GET", "POST"])
@login_required
def create_post():

    if request.method == "POST":

        title = request.form["title"]
        content = request.form["content"]

        if not title or not content:
            flash("Title and content are required.", "danger")
            return redirect(url_for("posts.create_post"))

        post = Post(
            title=title,
            content=content,
            user_id=current_user.id
        )

        db.session.add(post)
        db.session.commit()

        flash("Post created successfully!", "success")

        return redirect(url_for("main.home"))

    return render_template("posts/create.html")


@posts.route("/<int:post_id>")
def view_post(post_id):

    post = Post.query.get_or_404(post_id)

    return render_template(
        "posts/view.html",
        post=post
    )


@posts.route("/<int:post_id>/edit", methods=["GET", "POST"])
@login_required
def edit_post(post_id):

    post = Post.query.get_or_404(post_id)

    if post.user_id != current_user.id:

        flash(
            "You can only edit your own posts.",
            "danger"
        )

        return redirect(url_for("main.home"))

    if request.method == "POST":

        title = request.form["title"]
        content = request.form["content"]

        if not title or not content:

            flash(
                "Title and content are required.",
                "danger"
            )

            return redirect(
                url_for(
                    "posts.edit_post",
                    post_id=post.id
                )
            )

        post.title = title
        post.content = content

        db.session.commit()

        flash(
            "Post updated successfully!",
            "success"
        )

        return redirect(
            url_for(
                "posts.view_post",
                post_id=post.id
            )
        )

    return render_template(
        "posts/edit.html",
        post=post
    )


@posts.route(
    "/<int:post_id>/delete",
    methods=["POST"]
)
def delete_post(post_id):

    post = Post.query.get_or_404(post_id)

    if not current_user.is_authenticated:

        flash(
            "Please login to delete this post.",
            "danger"
        )

        return redirect(url_for("auth.login"))

    if post.user_id != current_user.id:

        flash(
            "You can only delete your own posts.",
            "danger"
        )

        return redirect(url_for("main.home"))

    db.session.delete(post)

    db.session.commit()

    flash(
        "Post deleted successfully!",
        "success"
    )

    return redirect(url_for("main.home"))