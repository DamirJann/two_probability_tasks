from matplotlib.animation import FuncAnimation
import numpy as np
import probability as prb
import matplotlib.pyplot as plt
import time
import showPlot
import matplotlib.ticker as ticker
plt.rcParams['animation.ffmpeg_path'] = 'X:\Trash/ffmpeg-20200413-59e3a9a-win64-static/ffmpeg-20200413-59e3a9a-win64-static/bin/ffmpeg.exe'
plt.rcParams['animation.convert_path'] = 'C:\Program Files/ImageMagick-7.0.10-Q16/magick.exe'

def showPlot(list):
    fig = plt.figure()
    ax = plt.axes(xlim=(0, 1000), ylim=(0, 1))
    plt.title('')
    plt.legend(loc=4)
    line, = ax.plot([], [], lw=3, label = 'experimental probability')
    ax.xaxis.set_major_locator(ticker.MultipleLocator(70))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(35))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(0.05))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.025))
    plt.xlabel("Number of tests")
    plt.ylabel("Probability")
    plt.title("P(Ivanov shoots first | Ivanov wins)")

    x0 = [i for i in range(1000)]
    y0 = [0.85 for i in range(1000)]

    ax.plot(x0,y0, linestyle = '--', linewidth = 1, label = 'theoretical probability')

    xdata, ydata = [], []
    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        print(i)
        xdata.append(10*i);
        ydata.append(list[10*i])
        line.set_data(xdata, ydata)
        return line,

    anim = FuncAnimation(fig, animate, init_func=init,
                         frames=100, interval=250, blit=True)
    anim.save('plot.gif', writer='imagemagick')
    plt.show()