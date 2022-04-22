#!/usr/bin/env python3

# Searching by text
# Viewing trending GIFs

import os

from app import create_app, gfycat_caller

from flask import request, render_template, url_for, redirect

import json

app = create_app(os.environ.get("FLASK_ENV"))


@app.route("/trending")
def trending():
    imgs = gfycat_caller.get_trending()
    return render_template("scatter_plot.html", imgs=json.dumps(imgs))


@app.route("/search")
def search():
    search_text = request.args.get("search_text")
    if not search_text:
        return redirect(url_for('trending'))
    imgs = gfycat_caller.get_search(search_text)

    return render_template("scatter_plot.html", imgs=json.dumps(imgs))


if __name__ == "__main__":
    app.run()
