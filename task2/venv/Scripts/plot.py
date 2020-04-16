from matplotlib.animation import FuncAnimation
import numpy as np
import probability as prb
import matplotlib.pyplot as plt
import time
import matplotlib.ticker as ticker
plt.rcParams['animation.ffmpeg_path'] = 'X:\Trash/ffmpeg-20200413-59e3a9a-win64-static/ffmpeg-20200413-59e3a9a-win64-static/bin/ffmpeg.exe'
plt.rcParams['animation.convert_path'] = 'C:\Program Files/ImageMagick-7.0.10-Q16/magick.exe'

def showPlot(list):
    fig = plt.figure()
    ax = plt.axes(xlim=(0, 30), ylim=(0, 1))
    plt.title('')
    line, = ax.plot([], [], lw=3, label = 'experimental probability')
    ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(2))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(0.05))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.025))
    plt.xlabel("Number of tests")
    plt.ylabel("Probability")
    plt.title("P(B lies between $a^2$ and $\sqrt{a}$)")

    x0 = [i for i in range(1000)]
    y0 = [1./3 for i in range(1000)]

    ax.plot(x0,y0, linestyle = '--', linewidth = 1, label = 'theoretical probability')
    plt.legend(loc=4)

    xdata, ydata = [], []
    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        print(i)
        xdata.append(list[i][3]);
        ydata.append(list[i][2]/list[i][3])
        line.set_data(xdata, ydata)
        return line,

    anim = FuncAnimation(fig, animate, init_func=init,
                         frames=30, interval=1000, blit=True)
    anim.save('plot.gif', writer='imagemagick')
    plt.show()