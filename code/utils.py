from datetime import datetime
import numpy as np
import pandas as pd
from tqdm import tqdm

# Receives a unix time format and returns a string in ISO format
def toDate(unix):
    return datetime.utcfromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S')

# Parameters: DataFrame of Matches, (Pandas DataFrame)
            # Valid Players to Count, (Numpy Array of Strings)
            # Limit Date, (Unix Format)
            # Use Date as Final Date? (Bool)
            
def countMatches(df, players, date, final = True):
    # Ordering players
    players  = np.sort(players)
    # Ordering matches
    # Vamos ordenar as partidas por data
    df       = df.sort_values("end_time", ascending = final)
    df       = df.reset_index(drop=True)
    nmatches = dict(zip(players, [0 for i in range(len(players))]))
    for i in tqdm(range(len(df))):
        white = df["white_username"][i]
        black = df["black_username"][i]
        # Limit by date
        if not final and df["end_time"][i] <  date: break
        if     final and df["end_time"][i] >= date: break
        # Binary Search
        if players.searchsorted(black) < len(players) and players[players.searchsorted(black)] == black:
            nmatches[black] += 1
        # Binary Search
        if players.searchsorted(white) < len(players) and players[players.searchsorted(white)] == white :
            nmatches[white] += 1
        
    return nmatches

# Receives an array and return a tuple with inferior and superior value of confidence interval
def confidenceInterval(array):
    import scipy.stats as ss
    from statistics import variance
    import math
    
    n      = len(array)
    mu     = np.mean(array)
    sigma  = math.sqrt(variance(array)) / np.sqrt(n)
    
    inferior = mu - 1.96*sigma
    superior = mu + 1.96*sigma
    
    return [inferior, superior]

# Parameters: Panda Series with the Values to Bootstrap, Number of Samples Required
# Returns an array with all the medians from the bootstrap process.

def makeBootstrap(df, n):
    values = np.zeros(n)
    for i in range(n):
        sample    = nme.sample(len(df), replace = True)
        values[i] = sample.mean()
    return values

# Receives an array and return its init and final percentage values
def percentile(bm_values, init, final):
#     bm_values = np.sort(bm_values)
#     per1      = int(len(bm_values) / 100 * init)
#     per2      = int(len(bm_values) / 100 * final)
#     inferior  = bm_values[per1]
#     superior  = bm_values[per2]
    inferior = np.percentile(bm_values, init)
    superior = np.percentile(bm_values, final)
    return [inferior, superior]