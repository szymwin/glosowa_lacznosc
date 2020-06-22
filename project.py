# importing all the dependencies
import pandas as pd # data frame
import numpy as np # matrix math
from glob import glob # file handling
import librosa # audio manipulation
from sklearn.utils import shuffle # shuffling of data
import os # interation with the OS
from random import sample # random selection
from tqdm import tqdm
from scipy import signal # audio processing
from scipy.io import wavfile # reading the wavfile

# fixed param
PATH = '/Users/wiktoriatyper/Desktop/Komendy/LABELS_MN'


def load_files(path):
    # write the complete file loading function here, this will return
    # a dataframe having files and labels
    # loading the files
    train_labels = os.listdir(PATH)
    train_labels.remove('_background_noise_')

    labels_to_keep = ['OTWORZ', 'OKNO', 'DRZWI', 'GARAZ', 'ZAMKNIJ', '_background_noise_']

    train_file_labels = dict()
    for label in train_labels:
        files = os.listdir(PATH + '/' + label)
        for f in files:
            train_file_labels[label + '/' + f] = label

    train = pd.DataFrame.from_dict(train_file_labels, orient='index')
    train = train.reset_index(drop=False)
    train = train.rename(columns={'index': 'file', 0: 'folder'})
    train = train[['folder', 'file']]
    train = train.sort_values('file')
    train = train.reset_index(drop=True)

    def remove_label_from_file(label, fname):
        return path + label + '/' + fname[len(label) + 1:]

    train['file'] = train.apply(lambda x: remove_label_from_file(*x), axis=1)
    train['label'] = train['folder'].apply(lambda x: x if x in labels_to_keep else 'unknown')

    labels_to_keep.append('unknown')

    return train, labels_to_keep
    train, labels_to_keep = load_files(PATH)

    # making word2id dict
    word2id = dict((c,i) for i,c in enumerate(sorted(labels_to_keep)))

    # get some files which will be labeled as unknown
    unk_files = train.loc[train['label'] == 'unknown']['file'].values
    unk_files = sample(list(unk_files), 1000)