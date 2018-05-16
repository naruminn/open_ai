#
#  # OpenAI Gym での学習に必要なユーティリティ
#

import gym
import numpy as np

# observationを一つの離散値に変換する
def digitize_state(env, observation, num_dizitized):
    def bins(clip_min, clip_max, num):
        return np.linspace(clip_min, clip_max, num + 1)[1:-1]
    env_low = env.observation_space.low
    env_high = env.observation_space.high
    digitized = []
    for index, value in enumerate(observation):
        digitized.append(np.digitize(value, bins=bins(env_low[index], env_high[index], num_dizitized)))
    return sum([x * (num_dizitized**i) for i, x in enumerate(digitized)])