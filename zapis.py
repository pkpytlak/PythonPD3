#!/opt/anaconda34/bin/python3
# -*- coding: utf-8 -*-

def zapis(katalog):
    import numpy as np
    import os
    import scipy.io.wavfile as siw
    os.chdir(katalog)
    utwor = katalog[-6:]
    songlist = np.loadtxt(utwor+'.txt')
    siw.write(''.join(utwor)+'_zapis.wav', 44100, np.int16(songlist/max(np.abs(songlist))*32767))

if __name__=='__main__':
    import sys
    import os
    argumenty = sys.argv
    utworX = argumenty[1][:-1]
    biezacy = os.getcwd()
    katalogX = biezacy+'\\'+utworX
    zapis(katalogX)