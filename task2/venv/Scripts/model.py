import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.ticker as ticker
import numpy as np
import time
from matplotlib import colors as mcolors
plt.rcParams['animation.ffmpeg_path'] = 'X:\Trash/ffmpeg-20200413-59e3a9a-win64-static/ffmpeg-20200413-59e3a9a-win64-static/bin/ffmpeg.exe'
plt.rcParams['animation.convert_path'] = 'C:\Program Files/ImageMagick-7.0.10-Q16/magick.exe'


def showModel(list):
    fig = plt.figure()
    ax = plt.axes(xlim=(0,1), ylim=(-1,2.35))
    annotationlA = ax.annotate(r'$a^2$', xy=(pow(list[0][0],2),0.05))
    annotationrA = ax.annotate(r'$\sqrt{a}$', xy=(pow(list[0][0],0.5),0.05))
    annotationB = ax.annotate('b', xy=(list[0][1]-0.03,-0.2))
    lA = ax.scatter(pow(list[0][0],2),0,c='b')
    rA = ax.scatter(pow(list[0][0],0.5),0,c='b')
    B = ax.scatter(pow(list[0][1],0.5),-0.08,c='r', zorder=3)
    line, = ax.plot([], [], lw=4, c='b')
    ax.text(0, 1,"Number of tests:\n\n\nFavorable number:", size = 13)
    numberOfTestText = ax.text(0.32, 1.55, list[0][3], fontsize=15, c='b')
    favoiableNumberText = ax.text(0.357, 0.97, list[0][2]/list[0][3], fontsize = 15, c='b')


    plt.gca().spines['bottom'].set_position(('axes', 0.3))
    plt.gca().spines['left'].set_position('center')
    ax.spines['bottom'].set_color('blue')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(labelleft=False)
    ax.tick_params(left=False)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))




    def init():
        line.set_data([], [])
        return line, annotationlA, annotationrA, lA, rA, B, annotationB, favoiableNumberText, numberOfTestText

    def animate(i):
        a = list[i][0]
        b = list[i][1]
        points = (np.linspace(a * a, pow(a, 0.5),1000), np.linspace(0,0,1000) )
        if ((b>=a*a) & (b<=pow(a, 0.5))):
            B.set_color('red')
        else:
            B.set_color('none')
            B.set_edgecolors('black')

        line.set_data(points)
        annotationlA.set_position((a*a,0.05))
        annotationrA.set_position((pow(a,0.5),0.05))
        annotationB.set_position((b-0.01,-0.2))
        lA.set_offsets((pow(a, 2), 0))
        rA.set_offsets((pow(a,0.5),0))
        B.set_offsets((b,0))
        favoiableNumberText.set_text(list[i][2])
        numberOfTestText.set_text(list[i][3])
        return line,annotationlA, annotationrA, lA, rA, B, annotationB, favoiableNumberText, numberOfTestText
    anim = FuncAnimation(fig, animate, init_func=init,
                         frames=30, interval=1000, blit=True)
    anim.save('model.gif', writer='imagemagick')
    plt.show()
