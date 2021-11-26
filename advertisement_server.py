# Create Flask app which shows clients online advertisements
# and simulate clients' clicks (as given in data file) on these ads.

# From the course: Bayesin Machine Learning in Python: A/B Testing
# https://deeplearningcourses.com/c/bayesian-machine-learning-in-python-ab-testing
# https://www.udemy.com/bayesian-machine-learning-in-python-ab-testing

from flask import Flask, jsonify, request
from advertisement_class import Ad # predefined class

# create Flask app
app = Flask(__name__)

# initialize online advertisements (Bayesian theory: bandit slot machines)
adA = Ad('A')
adB = Ad('B')

@app.route('/get_ad')
# determine which ad should be shown to client
def get_ad():
    if adA.show_ad() > adB.show_ad():
        ad = 'A'
        adA.add_view()
    else:
        ad = 'B'
        adB.add_view()
    return jsonify({'advertisement_id': ad})

@app.route('/click_ad', methods=['POST'])
# click ad according to data file
def click_ad():
    result = 'OK'
    if request.form['advertisement_id'] == 'A':
        adA.add_click()
        pass
    elif request.form['advertisement_id'] == 'B':
        adB.add_click()
        pass
    else:
        result = 'Invalid Input.'
    # nothing to return really
    return jsonify({'result': result})

# run app on local host
if __name__ == '__main__':
  app.run(host='127.0.0.1', port='8888')
