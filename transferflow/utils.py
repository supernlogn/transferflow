
import os
import json
import numpy as np
import cv2
from tensorflow.python.framework import graph_util
from tensorflow.python.platform import gfile
import tensorflow as tf
import shutil
import time
from distutils.version import LooseVersion

import logging
logger = logging.getLogger("transferflow.utils")

TENSORFLOW_VERSION = LooseVersion(tf.__version__)

def tf_concat(axis, values, **kwargs):
    if TENSORFLOW_VERSION >= LooseVersion('1.0'):
        return tf.concat(values, axis, **kwargs)
    else:
        return tf.concat(axis, values, **kwargs)

def load_meta(path):
    with open(path + '/index.json', 'r') as f:
        return json.load(f)

def load_labels(path):
    f = open(path + '/labels.jsons')
    index = {}
    for line in f:
        label = json.loads(line)
        index[label['id']] = label
    return index

def draw_rectangles(orig_image, rects, min_confidence=0.1, color=(0, 0, 255)):
    image = np.copy(orig_image)
    for rect in rects:
        if rect.confidence > min_confidence:
            cv2.rectangle(image,
                (rect.cx-int(rect.width/2), rect.cy-int(rect.height/2)),
                (rect.cx+int(rect.width/2), rect.cy+int(rect.height/2)),
                color,
                2)
    return image

def get_tensors(sess):
    layers = []
    for op in sess.graph.get_operations():
        layers.append(op.name)
    return layers

def get_tensor_namespaces(sess):
    namespaces = []
    for op in sess.graph.get_operations():
        path = op.name.split('/')
        if len(path) > 1 and path[0] not in namespaces:
            namespaces.append(path[0])
    return namespaces
