
from asyncore import loop
import asyncio
import nest_asyncio 
import cv2
import numpy as np

import globalValue
import MPautomation0616
#import MPautomation0617_PHG

nest_asyncio.apply()

def read_spa(filepath): # https://github.com/lerkoah/spa-on-python/blob/master/LoadSpectrum.py
    '''
    Input
    Read a file (string) *.spa
    ----------
    Output
    Return spectra, wavelenght (nm), titles
    '''
    tm = cv2.TickMeter()
    tm.start()

    with open(filepath, 'rb') as f:
        f.seek(564)
        Spectrum_Pts = np.fromfile(f, np.int32, 1)[0]
        f.seek(30)
        SpectraTitles = np.fromfile(f, np.uint8, 255)
        SpectraTitles = ''.join([chr(x) for x in SpectraTitles if x != 0])

        f.seek(576)
        Max_Wavenum = np.fromfile(f, np.single, 1)[0]
        Min_Wavenum = np.fromfile(f, np.single, 1)[0]
        # print(Min_Wavenum, Max_Wavenum, Spectrum_Pts)
        Wavenumbers = np.flip(np.linspace(Min_Wavenum, Max_Wavenum, Spectrum_Pts))

        f.seek(288);

        Flag = 0
        while Flag != 3:
            Flag = np.fromfile(f, np.uint16, 1)

        DataPosition = np.fromfile(f, np.uint16, 1)
        f.seek(DataPosition[0])

        Spectra = np.fromfile(f, np.single, Spectrum_Pts)

    tm.stop()
    print(f'File:[{f}] read Spa Time: {tm.getTimeMilli()} (ms)')
    
    return Spectra, Wavenumbers, SpectraTitles


async def get_info_from_spa(filepath):
    spec, wn, tit =  await globalValue.loop.run_in_executor(None, read_spa, filepath)
    
    # global MPautomation0617_PHG.proDlg
    globalValue.proDlg.SetIncreate()

    return spec, wn, tit

async def get_spec(input_list):
    info = [asyncio.ensure_future(get_info_from_spa(i)) for i in input_list]
    r = await asyncio.gather(*info)
    globalValue.results = r 
    return globalValue.results