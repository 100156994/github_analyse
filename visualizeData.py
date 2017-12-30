#可视化
#生成可视化图片
#!/usr/bin/python  
# coding: UTF-8
import numpy as np
import matplotlib.pyplot as plt
import json


def start():
    with open("data.json", 'r') as load_f:
        items = json.loads(load_f.read())
    index = np.arange(3)
    fig, ax = plt.subplots()

    width = 0.05  # the width of the bars

    i = 0
    for key, values in items.items():
        ax.bar(index + width * i, (values["total_star"], values["total_fork"],
                                   values["total_watch"]), width, label=key)

        i += 1
    ax.set_xlabel('languages')
    ax.set_ylabel('numbers')
    ax.set_title('top 10 language star fork and watch')
    ax.set_xticklabels(("star count", "fork count", "watch count"))
    ax.set_xticks(index + width / 0.3)
    ax.legend()

    fig.tight_layout()
    plt.savefig('./static/popular.png')

start()
