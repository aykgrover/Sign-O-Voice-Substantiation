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
from tkinter import *


accounts = {}
means = None
invstds = None

def printf(string):
    root = tk.Tk()
    w = tk.Label(root, text=string)
    w.pack()
    root.mainloop()
    
def normalize(means, invstds, data):
    return (data - means) * invstds

def filter_sig(fs, signal):
    vad_ob = vad.VAD()
    (fs_noise, signal_noise) = wav.read("noise.wav")
    vad_ob.init_noise(fs_noise, signal_noise)
    ret, intervals = vad_ob.afilter(fs, signal)
    orig_len = len(signal)
    
    if len(ret) > orig_len/3:
        wav.write('vaded.wav', fs, ret)
        return ret
    return np.array([0])
    #wav.write('vaded.wav', fs, ret)
    #return ret

def main(username):
    global accounts
    global means
    global invstds
    if means == None and os.path.isfile("allfeatures.txt"):
        means, invstds = ca.recalculate_norm()
    try:
        accounts = pickle.loads(open("accounts.txt", 'rb+').read(),encoding='latin1')
        #os.remove("accounts.txt")
    except IOError:
        print("IO Error")
        pass
    
    wa.record_noise()
    wa.write_temp_audio(username)

    wavpath = "temp.wav"
    (rate,sig) = wav.read(wavpath)
    new_sig = filter_sig(rate, sig)
    mfcc_feat = mfcc(new_sig, rate)
    mfcc_feat = np.array(mfcc_feat)

    best_label = ""
    best_ll = -9e99

    for label, account in accounts.items():
        features = normalize(means, invstds, mfcc_feat)
        ll = account.gmm.score_samples(features)[0]
        ll = np.sum(ll)
        print (label, ll)
        if ll > best_ll:
            best_ll = ll
            best_label = label
    print (best_ll)
    print (best_label)
    if username != best_label:
        return False
    else:
        return True

#try:
#    main()
#except KeyboardInterrupt:
#    print ('Interrupted')
#    pickle.dump(accounts, open("accounts.txt", 'wb+'))
#    sys.exit(0)
#except Exception as e:    
   #print (e)
   #print ('Problem with Speech Recognition -- please run in debug mode')
   #pickle.dump(accounts, open("accounts.txt", 'wb+'))
   #sys.exit(0)