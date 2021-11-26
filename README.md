# Bayesian Machine Learning: A/B Testing
This project is based on the final project of the online course https://www.udemy.com/course/bayesian-machine-learning-in-python-ab-testing/

# Introduction
Given are two online advertisements with different, competing designs.

Our aim is to determine which ad has a more compelling design.

Both ads are put online and shown to possible clients.

Data is collected: how often each ad is viewed and clicked. Showing ads (collecting data) costs money but also brings in money (converts clients to users). Therefore, while collecting data for our algorithm, we would already like to be showing the better ad (which converts more clients).

This is where Bayesian statistics comes in handy! We show ads depending on how often the ad was previously clicked (and showed). Mathematically, we show ads depending on a probability distribution (whose parameters learn).

Summarizing, we save opportunity costs from showing the suboptimal ad. We show the optimal ad as soon as we compute which ad is better.

# Bayesian ML application fields
Classical A/B testing is done when comparing options (here: two ad designs) and choosing the best option based on statistics and data.

Bayesian ML is generally suitable for online learning. When data is collected real-time (online), Bayesian statistics is useful. With every data point, it is not necessary to run the whole model again. Instead, the model is adapted (it learns) continously; and that in only constant O(1) time!

Bayesian ML therefore reduces computation time as well as data collection costs.

# Files
advertisement_clicks.csv ... data file

advertisement_class.py ... class for ads (views, clicks, showing probability)

advertisement_server.py ... shows advertisements, receives clicks on ads

customer_client.py ... simulates clients' views and clicks (as given in data file)

CTRs.png ... result: shows changing click-through-rates of both ads

requirements.txt ... list of all required modules and their versions

runtime.txt ... version of python used

# Usage
First run the server, then the client, i.e. run the files in this order:

python advertisement_class.py

python customer_client.py

# Results
CTRs.png shows how the changing click-through-rates of both ads, as we show more ads. We see that ad A has a higher CTR than ad B. This means that ad A has a more compelling design than ad B, i.e. show ad A to clients (not ad B).

Sanity check: the horizontal lines are the means of all clicks for each ad (if we had all data from the beginning, there would not need Bayesian ML). We can see that the changing CTRs converge towards these means, as expected.

Note that only for roughly the first 200 ads, the suboptimal ad was also shown. Later on, only the optimal ad is shown (since we calculated that its CTR is higher). Bayesian ML therefore helps to saves costs spent on showing suboptimal ads.

# Adaptation to other data sources
In this project, our data file consists of binary data click data (0 for not clicking, 1 for clicking). Therefore we chose a Bernoulli distribution as prior distribution and a Beta distribution as posterior distribution (see Bayesian theory).

For other data sources, we need to adapt prior and posterior distribution. For example, if our data is Normal distributed (prior distribution), the posterior distribution may be Normal, Gamma or Normal-Gamma distributed. These distributions have more than one parameter. Depending on which and how many parameters are modelled to learn, Bayesian theory tells us which prior and posterior distribution should be modelled together (form a conjugate pair).
