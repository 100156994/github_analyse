#!/usr/bin/python  
# coding: UTF-8
import numpy as np
import matplotlib.pyplot as plt
import json


# "total_star": 0,
# "total_fork": 0,
# "total_watch": 0,
# "total_sum": 0,
# 'count': 0

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                '%d' % int(height),
                ha='center', va='bottom')


with open("data.json", 'r') as load_f:
    items = json.loads(load_f.read())
    index = np.arange(3)
    fig, ax = plt.subplots()
    std = (2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
    width = 0.05  # the width of the bars

    i = 0
    for key, values in items.items():
        rect = ax.bar(index + width * i, (values["total_star"], values["total_fork"],
                                          values["total_watch"]), width, label=key)
        # autolabel(rect)
        i += 1
    ax.set_xlabel('languages')
    ax.set_ylabel('numbers')
    ax.set_title('top 10 language star fork and watch')
    ax.set_xticklabels(("star", "fork", "watch"))
    ax.set_xticks(index + width / 0.3)
    ax.legend()

    fig.tight_layout()
    plt.show()
