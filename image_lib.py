import io

import matplotlib.pyplot as plt
from PIL import Image


async def get_ecg_image(graph_x, graph_y):
    graph_x = list(map(int, graph_x.split(', ')))
    graph_y = list(map(int, graph_y.split(', ')))

    plt.plot(graph_x, graph_y, color='red', linewidth=3.0)
    plt.xlabel('Time', color='black')
    plt.ylabel('Amplitude', color='black')
    plt.xticks(color='black')
    plt.yticks(color='black')
    plt.title('ECG', color='black')
    plt.grid(False)

    ax = plt.gca()
    ax.spines['top'].set_color('black')
    ax.spines['bottom'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')

    buf = io.BytesIO()
    fig = plt.gcf()
    fig.savefig(buf, format='png')
    buf.seek(0)
    img = buf.read()

    return img


