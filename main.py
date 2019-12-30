import os

from collections import Counter

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from matplotlib import image as mpimg

import statistics


# 2194


def getColors(img):
    pixels = img.reshape((72*72, 4))  .tolist()

    # filter pixels for all with A > .9 (almost nontransparent)
    pixels = list(filter(lambda x: x[3] >= .9, pixels))

    # turn in [R, G, B, A]
    img_reshaped = np.array(pixels).T

    mean = list(map(lambda x: np.mean(x), img_reshaped))
    median = list(map(lambda x: np.median(x), img_reshaped))
    mode = list(map(lambda x: (Counter(x).most_common(1))[0][0], img_reshaped))
    print('hi')
    print(mode)

    # tupleify image to remove duplicates
    pixels = [tuple(i) for i in pixels]
    count = [[x, pixels.count(x)] for x in set(pixels)]

    def getFrequency(val):
        return val[1]

    count.sort(key=getFrequency, reverse=True)
    most = list((count[0])[0])

    fortyforty = img[40, 40]

    dings = [mean, median, mode, most, fortyforty]

    return dings


def plotWithColors(img, colors):
    fig, ax = plt.subplots()

    ax.imshow(img)

    for d in range(len(colors)):
        print(colors[d])
        rect = Rectangle((d * 20.0, 80.0), 20, 20,
                         alpha=1, facecolor=colors[d])
        ax.add_patch(rect)

    plt.xlim((0, 120))
    plt.ylim((100, 0))

    plt.show()


pngs = os.listdir("assets/72x72/")

# pngs = ["1f1e6-1f1ea.png"]


for png in pngs:
    print(png)

    img = mpimg.imread(str('assets/72x72/' + png))

    colors = getColors(img)

    plotWithColors(img, colors)
