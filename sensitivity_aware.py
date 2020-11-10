import numpy as np
import tensorflow as tf

from tqdm.notebook import tqdm

from carlini_wagner_l2 import CarliniWagnerL2

class SensitivityAware(CarliniWagnerL2):
    def __init__(self,
                             model_fn,
                             y=None,
                             batch_size=128,
                             clip_min=0.,
                             clip_max=1.,
                             binary_search_steps=5,
                             max_iterations=1_000,
                             abort_early=True,
                             confidence=0.,
                             initial_const=1e-2,
                             learning_rate=5e-3):
        super().__init__(model_fn, y, batch_size, clip_min, clip_max, binary_search_steps, max_iterations, abort_early, confidence, initial_const, learning_rate)
        self.sensitivity_map = None
    
    def loss_fn(self, x, x_new, y_true, y_pred, const):
        other = self.clip_tanh(x)
        l2_dist = tf.reduce_sum(
                tf.square(x_new - other)*self.sensitivity_map, list(range(1, len(x.shape))))

        real = tf.reduce_sum(y_true * y_pred, 1)
        other = tf.reduce_max(
                (1. - y_true) * y_pred - y_true * 10_000, 1)

        if self.targeted:
            # if targeted, optimize for making the other class most likely
            loss_1 = tf.maximum(0., other - real + self.confidence)
        else:
            # if untargeted, optimize for making this class least likely.
            loss_1 = tf.maximum(0., real - other + self.confidence)

        # sum up losses
        loss_2 = tf.reduce_sum(l2_dist)
        loss_1 = tf.reduce_sum(const * loss_1)
        loss = loss_1 + loss_2
        return loss, l2_dist