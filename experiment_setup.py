import pylab, pickle, sys
from ast import literal_eval
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from candidate_class import *
import random
from subprocess import call
from read_output_files import dipoleProperty
import realProblemSolver
import create_candidates
import obtain_lpoutput_result


theta_list = [0, 10, 20, 30, 40, 50, 60, 70, 80]
probe_arrange = arange(1000,2000,5)
pickle_files = ['methionine.pkl','Leu_dipproperty.pkl','Ile_dipproperty.pkl','Ala_dipproperty.pkl']
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


def experiment_setup_notInUse():
  size = len(pickle_files)
  pickle_files_copy = list(pickle_files)
  
  while size:
    size = size - 1
    index1 = random.randint(0,size)
    pickle_file = pickle_files_copy[index1]
    pickle_files_copy[index1] = pickle_files_copy[-1]
    del pickle_files_copy[-1]
    index2 = random.randint(0, len(theta_list)-1)
    theta = theta_list[index2]

  for i in range(len(candidates)-1):
    percentage = round(random.uniform(0, 1- sum(percentages)),5)
    percentages.append(percentage)
  percentages.append(round((1- sum(percentages)),5)) 
  size = len(pickle_files)
  print percentages

def run_experiment():
  create_candidates.create_candidates(percentages, candidates, probe_arrange)
  # run 7 experiments in the set
  for i in range(7):
    i = i + 1
    realProblemSolver.solver("candidates%s.txt"%(i), "lp_input%s.txt"%(i))
    call(["glpsol", "-o", "lp_output%s.txt"%(i), "--lp", "lp_input%s.txt"%(i)])
    call(["rm", "candidates%s.txt"%(i)])
    call(["rm", "lp_input%s.txt"%(i)])

def generate_histogram(L, pic_name):
  labels, values = zip(*Counter(L).items())
  indexes = np.arange(len(labels))
  width =1
  plt.ylabel('Frequency')
  bar = plt.bar(indexes, values, width)
  plt.xticks(indexes+width, ['Experiment%s'%i for i in labels])

  for i in bar:
    height = i.get_height()
    plt.text(i.get_x() + i.get_width()/2., 1.05*height, '%d' % int(height), ha='center', va='bottom')

  plt.savefig('%s.png'%pic_name,dpi=100)
  plt.close()

def analyze_result():
  L0, L1, L2, L3, L4, L5, L6 = [], [], [], [], [], [], []
  lines = []
  input = open('score.txt','r')
  line = input.readline()
  while line:
    line = line.strip()
    line = literal_eval(line)
    lines.append(line)
    line = input.readline() 
  for i in lines:
    L0.append(i[0])
    L1.append(i[1])
    L2.append(i[2])
    L3.append(i[3])
    L4.append(i[4])
    L5.append(i[5])
    L6.append(i[6])
  generate_histogram(L0,'L0')
  generate_histogram(L1,'L1')
  generate_histogram(L2,'L2')
  generate_histogram(L3,'L3')
  generate_histogram(L4,'L4')
  generate_histogram(L5,'L5')
  generate_histogram(L6,'L6')
  input.close()


if __name__ == "__main__":
  open('score.txt','w').close()
  for j in range(100):
    experiment_setup(percentages)
    
    run_experiment()
    result_file = 'result%s.txt'%(j)
    score_file = 'score.txt'
    obtain_lpoutput_result.obtain_result(percentages, result_file, score_file)
    percentages = []
  analyze_result()
    
    