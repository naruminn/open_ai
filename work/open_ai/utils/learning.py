#
#  # OpenAI Gym での学習に必要なユーティリティ
#

import gym
import numpy as np

# observationを一つの離散値に変換する
def digitize_state(observation, low, high, num_dizitized):
    def bins(clip_min, clip_max, num):
        return np.linspace(clip_min, clip_max, num + 1)[1:-1]
    digitized = []
    for index, value in enumerate(observation):
        digitized.append(np.digitize(value, bins=bins(low[index], high[index], num_dizitized)))
    return sum([x * (num_dizitized**i) for i, x in enumerate(digitized)])