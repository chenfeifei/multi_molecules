import os
from re import match
#import pylab, pickle, sys
#from candidate_class import *
#from experiment_setup import candidates, probe_arrange

def obtain_result(percentage, result_file, score_file):
    score_file = open(score_file, 'a')
    data_file = open(result_file,'w')

    #iterate 7 experiment result that returned by lp_solver
    score_list = []
    score = 0.0

    for i in range(7):
      i = i + 1
      result = []
      with open('lp_output%s.txt'%(i)) as input:
        line = input.readline()
        while line:
          line = line.split()
          if len(line) >= 5:
            if match('x\d+',line[1]):
              result.append(float(line[3]))
          line = input.readline()
      result = result[:-1]
      score = sum((x-y)**2 for x,y in zip(percentage,result))
      score_list.append(score)
      data_file.write(str(i) + ' &' + str(result) + ' &' + str(score)+ '\n')

    data_file.write(str(score_list) + '\n')
    score_sorted = sorted(range(len(score_list)), key = lambda k: score_list[k])
    score_sorted = [ x+1 for x in score_sorted]
    score_file.write(str(score_sorted) + '\n')
    score_file.close()
    data_file.write(str(score_sorted)+ '\n')
    data_file.close()





