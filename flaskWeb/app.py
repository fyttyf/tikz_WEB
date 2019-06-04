'''
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run('0.0.0.0',port=8000)

'''
import json
from flask import Flask, render_template

app = Flask(__name__)



@app.route("/index/")
def index():
    url = []
    with open('./static/file/exampleName.json', 'r') as f:
        data = json.load(f)
        names = data['names']
        for i in range(len(names)):
            names[i] = names[i].split('.')[0]
            url.append('images/' + names[i] + '.png')

    return render_template("index.html", allNames = names, allUrl = url, length = len(url))


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/find/")
def find():
    return render_template("find.html")


@app.route("/tag/")
def tags():
    with open('./static/file/allTag.json', 'r') as f:
        data_tag = json.load(f)
        total_tags = data_tag['tags']
        total_tags.sort()
    return render_template("tag.html", allTag = total_tags)


@app.route('/<category>')
def individual_tag(category):
    url = []
    with open('./static/file/texCatelog.json', 'r') as f:
        texCatelog = json.load(f)
        names = texCatelog[category]
        for i in range(len(names)):
            names[i] = names[i].split('.')[0]
            #url.append('images/' + names[i] + '.png')
        names = list(set(names))
        names.sort()
        for i in range(len(names)):
            url.append('images/' + names[i] + '.png')
    return render_template("index.html",allNames = names, allUrl = url, length = len(url) )


if __name__ == "__main__":
    app.run('0.0.0.0',port=8000,debug=True)
