from subprocess import call
from read_output_files import dipoleProperty
import realProblemSolver
import create_candidates
from experiment_setup import percentages, candidates, probe_arrange
import obtain_lpoutput_result

open('score.txt','w').close()

j = 1
for percentage in percentages:
    create_candidates.create_candidates(percentage, candidates, probe_arrange)
    # run 7 experiments in the set
    for i in range(7):
      i = i + 1
      realProblemSolver.solver("candidates%s.txt"%(i), "lp_input%s.txt"%(i))
      call(["glpsol", "-o", "lp_output%s.txt"%(i), "--lp", "lp_input%s.txt"%(i)])
      call(["rm", "candidates%s.txt"%(i)])
      call(["rm", "lp_input%s.txt"%(i)])
    
    result_file = 'result%s.txt'%(j)
    score_file = 'score.txt'


    obtain_lpoutput_result.obtain_result(percentage, result_file, score_file)
    j = j + 1
