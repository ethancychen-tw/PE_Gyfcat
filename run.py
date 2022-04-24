#!/usr/bin/env python3

# Searching by text
# Viewing trending GIFs

import os

from app import create_app, gfycat_caller

from flask import request, render_template, url_for, redirect

import json

app = create_app(os.environ.get("FLASK_ENV"))

@app.route("/")
@app.route("/trending")
def trending():
    cursor = request.args.get("cursor")
    print(cursor)
    imgs, cursor = gfycat_caller.get_trending(cursor=cursor)
    return render_template("scatter_plot.html", title="Trending", imgs=json.dumps(imgs), cursor=cursor)


@app.route("/search")
def search():
    cursor = request.args.get("cursor")
    search_text = request.args.get("search_text")
    if not search_text:
        return redirect(url_for('trending'))
    imgs, cursor = gfycat_caller.get_search(search_text, cursor=cursor)

    return render_template("scatter_plot.html", title="Search Result", imgs=json.dumps(imgs), cursor=cursor)


if __name__ == "__main__":
    app.run()
