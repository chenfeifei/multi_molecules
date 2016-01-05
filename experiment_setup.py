import pylab, pickle, sys
from candidate_class import *

# for testing, base on the passing pickle file, create candidates with different theta
pickle_file1 = 'methionine.pkl'
pickle_file2 = 'Leu_dipproperty.pkl'

theta_list = [0, 10, 20, 30, 40, 50, 60, 70, 80]
percentages = [[0, 0, 0.8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.2, 0, 0, 0, 0 ],
	       [0, 0, 0.3, 0, 0, 0, 0.5, 0, 0, 0, 0, 0, 0, 0.2, 0, 0, 0, 0]]

probe_arrange = arange(1000,2000,5)

# candidates setting
candidates1 = [Candidate(pickle_file1, theta) for theta in theta_list]
candidates2 = [Candidate(pickle_file2, theta) for theta in theta_list]
candidates = candidates1 + candidates2


'''
#percentages that have tried:
[0, 0.8, 0, 0, 0, 0, 0, 0, 0.2]
[0, 0.8, 0, 0.2, 0, 0, 0, 0, 0]
[0, 0, 0, 0.5, 0, 0.5, 0, 0, 0]
[0, 0.2, 0, 0, 0.5, 0, 0, 0, 0.2]
[0, 0, 0, 0.2, 0.5, 0.2, 0, 0, 0]
[0.1, 0.5, 0.2, 0.2, 0, 0, 0, 0, 0]
[0.2, 0.2, 0.2, 0.2, 0.2, 0, 0, 0, 0]
'''
