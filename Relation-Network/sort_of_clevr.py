from __future__ import absolute_import
from __future__ import division

from keras.preprocessing.image import load_img
import os.path
import numpy as np
import h5py

from util import log

rs = np.random.RandomState(123)


class Dataset(object):

    def __init__(self, ids, path, name='default',
                 max_examples=None, is_train=True):
        self._ids = list(ids)
        self.name = name
        self.is_train = is_train

        if max_examples is not None:
            self._ids = self._ids[:max_examples]

        filename = 'data.hy'

        file = os.path.join(path, filename)
        log.info("Reading %s ...", file)

        try:
            self.data = h5py.File(file, 'r')
        except:
            raise IOError('Dataset not found. Please make sure the dataset was downloaded.')
        log.info("Reading Done: %s", file)
        # load data info
        mean_std = np.load('../DatasetCreation/VG/mean_std.npz')
        self.img_mean = mean_std['img_mean']
        self.img_std = mean_std['img_std']
        self.coords_mean = mean_std['coords_mean']
        self.coords_std = mean_std['coords_std']

    def get_data(self, id):
        # preprocessing and data augmentation
        img_name = self.data[id]['image'].value
        # load image
        img = np.array(load_img('../DatasetCreation/images/'+img_name)).astype(np.float64)
        # normalize images
        img -= self.img_mean
        img /= self.img_std
        q = self.data[id]['question'].value.astype(np.float32)
        a = self.data[id]['answer'].value.astype(np.float32)
        l = self.data[id]['location'].value.astype(np.float32)

        # normalize coordinates
        l -= self.coords_mean
        l /= self.coords_std

        return img, q, a, l

    @property
    def ids(self):
        return self._ids

    def __len__(self):
        return len(self.ids)

    def __repr__(self):
        return 'Dataset (%s, %d examples)' % (
            self.name,
            len(self)
        )


def get_data_info():
    # img height, img width, channels, questions, answer
    return np.array([300, 300, 3, 38, 17])


def get_conv_info():
    # changed from -> np.array([24, 24, 24, 24])
    return np.array([64, 128, 256, 256, 128])


def create_default_splits(path, is_train=True):
    ids = all_ids(path)
    n = len(ids)

    num_trains = int(n*0.8)

    dataset_train = Dataset(ids[:num_trains], path, name='train', is_train=False)
    dataset_test = Dataset(ids[num_trains:], path, name='test', is_train=False)
    return dataset_train, dataset_test


def all_ids(path):
    id_filename = 'id.txt'

    id_txt = os.path.join(path, id_filename)
    try:
        with open(id_txt, 'r') as fp:
            _ids = [s.strip() for s in fp.readlines() if s]
    except:
        raise IOError('Dataset not found. Please make sure the dataset was generated.')
    rs.shuffle(_ids)
    return _ids
