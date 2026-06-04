#!/usr/bin/env python3
"""
bar chart with fruits
"""
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """How much fruit do Fs consume"""
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))

    # your code here
    ppl = (
        "Farrah",
        "Fred",
        "Felicia"
    )

    fruits = {
        "apples": (fruit[0], "red"),
        "bananas": (fruit[1], "yellow"),
        "oranges": (fruit[2], "#ff8000"),
        "peaches": (fruit[3], "#ffe5b4")
    }

    ax = plt.gca()
    bottom = np.zeros(3)

    for name, (quantity, colors) in fruits.items():
        p = ax.bar(ppl, quantity, color=colors, width=0.5,
                   bottom=bottom, label=name)
        bottom += quantity

    ax.set_title("Number of Fruit per Person")
    ax.legend(loc="upper right")

    plt.ylabel('Quantity of Fruit')

    plt.ylim(0, 80)
    plt.yticks(range(0, 81, 10))

    plt.show()
