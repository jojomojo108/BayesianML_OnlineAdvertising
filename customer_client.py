# Client sends customer click data to advertisement server
# as given in data file advertisement_clicks.csv

# From the course: Bayesin Machine Learning in Python: A/B Testing
# https://deeplearningcourses.com/c/bayesian-machine-learning-in-python-ab-testing
# https://www.udemy.com/bayesian-machine-learning-in-python-ab-testing

import requests # to send data to server (here: local host)
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# load data
df = pd.read_csv('advertisement_clicks.csv')
actions_A = df[df['advertisement_id'] == 'A']
actions_B = df[df['advertisement_id'] == 'B']
actions_A = actions_A['action'].values
actions_B = actions_B['action'].values

# save CTRs (click-through-rates)
ctrs = pd.DataFrame(columns=['CTR_A', 'CTR_B'])
# CTRs are 0 when no ads are seen yet
ctrs.at[0,'CTR_A'] = 0
ctrs.at[0,'CTR_B'] = 0

# ------------------------------------------------------------------------------
# one-by-one, pass data to server ...
i = 0
j = 0
ads_seen = 0 # total number of seen ads
clicks_A = 0 # clicks on ad A
clicks_B = 0 # clicks on ad B

# ... until no data left for either ad
while i < len(actions_A) and j < len(actions_B):
    r = requests.get('http://localhost:8888/get_ad').json()
    if r['advertisement_id'] == 'A':
        action = actions_A[i]
        i += 1
    else:
        action = actions_B[j]
        j += 1

    # click ad if dataset says so
    if action == 1:
        requests.post(
        'http://localhost:8888/click_ad',
        data={'advertisement_id': r['advertisement_id']})

        # count which ad was clicked on
        if r['advertisement_id'] == 'A':
            clicks_A += 1
        else:
            clicks_B += 1
    # to compare CTRs
    #ctrr[ads_seen] = i / j
    ads_seen += 1
    if i > 0 and j > 0:
        ctrs.at[ads_seen, 'CTR_A'] = clicks_A / i
        ctrs.at[ads_seen, 'CTR_B'] = clicks_B / j

    # log some stats
    #ads_seen += 1
    #if ads_seen % 50 == 0:
    #    print("Seen %s ads, A: %s, B: %s" % (ads_seen, i, j))

# ------------------------------------------------------------------------------
# plot results
fig, ax = plt.subplots()

# plot dynamically changing CTRs
ax.plot(ctrs['CTR_A'], color='green', label='CTR A')
ax.plot(ctrs['CTR_B'], color='red', label='CTR B')

# plot means of whole data set
ax.axhline(actions_A.mean(), color='green')
ax.axhline(actions_B.mean(), color='red')

# legend and labels
ax.legend(loc='upper right')
ax.set_xlabel('Ads seen')
ax.set_ylabel('CTRs')

# save and view plot
plt.savefig('CTRs.png')
plt.show()

"""
Results
-------
The ad with higher CTR has a more compelling design, i.e. ad AB.

Sanity check
------------
CTRs should converge to respective data means.
If all data is available from start,
the means can be compared immediately.
These means are the final CTRs!
Therefore Bayesian ML algorithm is not necessary
since no online learning (no continously incoming data).

"""
# check means = CTRs of all data in advance
#print("actions_A.mean:", actions_A.mean())
#print("actions_B.mean:", actions_B.mean())
