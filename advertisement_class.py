# Define class for Bayesian ML algorithm (Thompson sampling)

from scipy.stats import beta
import numpy as np

class Ad():
    """
    A class used to represent an online advertisement.
    The term used in Bayesian theory is "bandit",
    where the typical example of a bandit is a casino slot machine.
    A casino slot machine returns (probable) coin rewards,
    whereas our Ad class returns probabilities of it being shown (to gain new customer).

    ...

    Attributes
    ----------
    name : str
        The name of the ad
    views : int
        The number of views of the ad
    clicks : int
        The number of clicks of the ad

    Methods
    -------
    add_view()
        Increments number of views by 1
    add_click()
        Increments number of clicks by 1
    show_ad()
        Returns probability to show the ad,
        depending on how often the ad was already viewed and clicked.
    """

    def __init__(self, name: str):
        self.name = name
        self.views = 0
        self.clicks = 0

    def add_view(self):
        self.views += 1

    def add_click(self):
        self.clicks += 1

    # here is where is Bayesian statistics happens!
    def show_ad(self):
        a = 1 + self.clicks
        b = 1 + self.views - self.clicks
        return np.random.beta(a, b)

        """
        Returns probability to show (i.e. view) the ad
        depending on how often the ad was already viewed and clicked,
        i.e. number of views and number of clicks.
        See "Thompson sampling" in Bayesian theory.

        The showing-probability is initialized to be uniformly distributed,
        which is equivalent to Beta(1,1) (start with no views nor clicks).
        See "prior distribution" in Bayesian theory.

        The showing-probability is modelled by the Beta distributions
        with updated parameters (updated number of views and clicks).
        See "posterior distribution" in Bayesian theory.

        Bayesian theory shows that Beta distribution is the correct choice
        when modelling Bernoulli distributed data (here: click data).
        See "conjugate pairs" in Bayesian theory.
        """
