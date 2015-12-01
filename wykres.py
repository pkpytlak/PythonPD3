#!/opt/anaconda34/bin/python3
# -*- coding: utf-8 -*-

def wykres(katalog):
    import numpy as np
    import os
    import scipy.io.wavfile as siw
    import json
    import scipy.fftpack as sf
    import matplotlib.pylab as plt
    os.chdir(katalog)
    song = open('song.txt', 'r')
    songlist = list()
    defs = json.load(open('defs.txt', 'r'))
    beat = defs["bpm"]
    nframes = 60/beat*44100
    for songline in song:
        track = open('track'+songline.strip('\n')+'.txt', 'r')
        tracklist = list()
        for trackline in track:
            y = np.zeros([nframes, 2])
            for i in range(len(trackline.split())):
                y = y + siw.read('sample'+''.join(trackline.split()[i])+'.wav')[1][0:nframes]
            y = np.mean(y,axis=1)
            y /= 32767
            tracklist = np.r_[tracklist, y]
        songlist = np.r_[songlist, tracklist]
    yf = sf.fft(songlist)
    n = yf.size
    xf = np.linspace(0, 44100/2, n/2)
    plt.plot(xf, 2*(yf[1:int(n/2)+1])/n)
    plt.xscale('log')
    plt.show()

if __name__=='__main__':
    import sys
    import os
    argumenty = sys.argv
    utworX = argumenty[1][:-1]
    biezacy = os.getcwd()
    katalogX = biezacy+'\\'+utworX
    wykres(katalogX)