#生成网站
import json

from flask import *
import pandas as pd

app = Flask(__name__)


def convertToHtml(result, title):
    d = {}
    index = 0
    for t in title:
        d[t] = result[index]
        index = index + 1
    df = pd.DataFrame(d)
    df = df[title]
    h = df.to_html(index=False)
    return h, result[0]


def getH():
    with open("data.json", 'r') as load_f:
        items = json.loads(load_f.read())
    arr = [[], []]
    for key, values in items.items():
        reposition = values["reposition"]
        result = [[], [], [], [], []]
        index = 0
        for reps in reposition:
            result[0].append(reps['name'])
            result[1].append(reps['url'])
            result[2].append(reps['star'])
            result[3].append(reps['fork'])
            result[4].append(reps['watch'])
            index += 1
            if index > 5:
                break
        title = [u'name', u'Repo', u'Star', u'Fork', u'Watch']
        h, title = convertToHtml(result, title)
        arr[0].append(h)
        arr[1].append(key)

    return arr


@app.route("/tables")
def show_tables():
    arr = getH()
    print(arr[1])
    return render_template("show.html", tables=arr[0],
                           titles=arr[1])


def start():
    app.run(debug=True)
