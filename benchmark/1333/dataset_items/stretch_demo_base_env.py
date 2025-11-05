import os
import gym

class StretchDemoBaseEnv(gym.Env):
    def _recursive_listdir(self, directory):
        # From: https://stackoverflow.com/questions/19309667/recursive-os-listdir
        return [os.path.join(dp, f) for dp, dn, fn in os.walk(directory) for f in fn]
