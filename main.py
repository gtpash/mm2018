#going to try a basic tf model using keras

#localpath
import os
path = 'C:\\Users\\graha\\Dropbox\\Graham\\documents\\GitHub\\mm2018'
os.chdir(path)

import math
import numpy as np
import pandas as pd
import tensorflow as tf
import keras

data_dir = 'C:\\Users\\graha\\Dropbox\\Graham\\documents\\SportsAnalytics\\mm_data\\DataFiles\\'

#read in seeds and results
df_seeds = pd.read_csv(data_dir + 'NCAATourneySeeds.csv')
df_tour = pd.read_csv(data_dir + 'NCAATourneyCompactResults.csv')

#df_seeds.head()
#df_tour.head()

def seed_to_int(seed):
    #Get just the digits from the seeding. Return as int
    s_int = int(seed[1:3])
    return s_int
df_seeds['seed_int'] = df_seeds.Seed.apply(seed_to_int)
df_seeds.drop(labels=['Seed'], inplace=True, axis=1) # This is the string label
#df_seeds.head()

