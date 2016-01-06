import pylab, pickle, sys
from candidate_class import *
import random
from subprocess import call
from read_output_files import dipoleProperty
import realProblemSolver
import create_candidates
import obtain_lpoutput_result

# for testing, base on the passing pickle file, create candidates with different theta
#pickle_file1 = 'methionine.pkl'
#pickle_file2 = 'Leu_dipproperty.pkl'

theta_list = [0, 10, 20, 30, 40, 50, 60, 70, 80]
#percentages = [[0, 0, 0.8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.2, 0, 0, 0, 0 ],
#	       [0, 0, 0.3, 0, 0, 0, 0.5, 0, 0, 0, 0, 0, 0, 0.2, 0, 0, 0, 0]]
probe_arrange = arange(1000,2000,5)

# candidates setting
#candidates1 = [Candidate(pickle_file1, theta) for theta in theta_list]
#candidates2 = [Candidate(pickle_file2, theta) for theta in theta_list]
#candidates = candidates1 + candidates2
pickle_files = ['methionine.pkl','Leu_dipproperty.pkl','Ile_dipproperty.pkl']
candidates = [Candidate(pickle_file, theta) for pickle_file in pickle_files for theta in theta_list]

percentages = []
def experiment_setup(percentages):
  size = len(theta_list)
  percentage = [0]*size
  
  for i in range(len(pickle_files)-1):
    index = random.randint(0,size-1)
    print index
    percentage[index] = round(random.uniform(0, 1- sum(percentages)),5)
    percentages += percentage
    percentage = [0]*size
    
  percentage = [0]*size
  index = random.randint(0,size-1)
  print index
  percentage[index] = round((1- sum(percentages)),5)
  percentages += percentage
  print percentages, len(percentages)


def experiment_setup1():
  size = len(pickle_files)
  pickle_files_copy = list(pickle_files)
  
  while size:
    size = size - 1
    index1 = random.randint(0,size)
    pickle_file = pickle_files_copy[index1]
    pickle_files_copy[index1] = pickle_files_copy[-1]
    del pickle_files_copy[-1]
    print pickle_file
    index2 = random.randint(0, len(theta_list)-1)
    theta = theta_list[index2]
    print theta
    #candidates.append(Candidate(pickle_file, theta))
  

  for i in range(len(candidates)-1):
    percentage = round(random.uniform(0, 1- sum(percentages)),5)
    percentages.append(percentage)
  percentages.append(round((1- sum(percentages)),5)) 
  size = len(pickle_files)
  print percentages

def run_experiment():
  #open('score.txt','w').close()

  create_candidates.create_candidates(percentages, candidates, probe_arrange)
  # run 7 experiments in the set
  for i in range(7):
    i = i + 1
    realProblemSolver.solver("candidates%s.txt"%(i), "lp_input%s.txt"%(i))
    call(["glpsol", "-o", "lp_output%s.txt"%(i), "--lp", "lp_input%s.txt"%(i)])
    call(["rm", "candidates%s.txt"%(i)])
    call(["rm", "lp_input%s.txt"%(i)])
      
  #result_file = 'result%s.txt'%(j)
  #result_file = 'result.txt'
  #score_file = 'score.txt'
  #obtain_lpoutput_result.obtain_result(percentages, result_file, score_file)

if __name__ == "__main__":
  open('score.txt','w').close()
  for j in range(10):
    experiment_setup(percentages)
    
    run_experiment()
    result_file = 'result%s.txt'%(j)
    score_file = 'score.txt'
    obtain_lpoutput_result.obtain_result(percentages, result_file, score_file)
    percentages = []
    
    
    