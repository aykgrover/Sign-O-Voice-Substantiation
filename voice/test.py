import account as ac
import create_account as ca
import write_audio as wa
import scipy.io.wavfile as wav
import sys
from python_speech_features import mfcc
import numpy as np
import pickle
import os
import ltsd
import vad
import verify as verify

def filter_sig(fs, signal):
    vad_ob = vad.VAD()
    (fs_noise, signal_noise) = wav.read("noise.wav")
    vad_ob.init_noise(fs_noise, signal_noise)
    #ret, intervals = vad_ob.filter(fs, signal)
    #orig_len = len(signal)
    
    #if len(ret) > orig_len/3:
        #wav.write('vaded.wav', fs, ret)
        #return ret
    #return np.array([0])

wavpath = "temp.wav"
(rate,sig) = wav.read(wavpath)
filter_sig(rate, sig)
#mfcc_feat = mfcc(new_sig, rate)
