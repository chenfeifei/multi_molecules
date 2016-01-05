import pylab, pickle, sys
from candidate_class import *
from experiment_setup import candidates, probe_arrange

def create_candidates(percentage, candidates, probe_arrange): 
    # generate target spectroscopy
    target_ir_x = []
    target_ir_z = []
    target_raman_xx = []
    target_raman_xy = []
    target_raman_xz = []
    target_raman_zz = []
    target_sfg_yyz = []
    target_sfg_yzy = []
    target_sfg_zzz = []

    for probe in probe_arrange:
      candidate_ir_x_list = [candidate.ir_x(probe) for candidate in candidates]
      candidate_ir_z_list = [candidate.ir_z(probe) for candidate in candidates]
      candidate_raman_xx_list = [candidate.raman_xx(probe) for candidate in candidates]
      candidate_raman_xy_list = [candidate.raman_xy(probe) for candidate in candidates]
      candidate_raman_xz_list = [candidate.raman_xz(probe) for candidate in candidates]
      candidate_raman_zz_list = [candidate.raman_zz(probe) for candidate in candidates]
      candidate_sfg_yyz_list = [candidate.sfg_yyz(probe) for candidate in candidates]
      candidate_sfg_yzy_list = [candidate.sfg_yzy(probe) for candidate in candidates]
      candidate_sfg_zzz_list = [candidate.sfg_zzz(probe) for candidate in candidates]
      
      target_ir_x.append(sum(x*y for x,y in zip(percentage,candidate_ir_x_list)))
      target_ir_z.append(sum(x*y for x,y in zip(percentage,candidate_ir_z_list)))
      target_raman_xx.append(sum(x*y for x,y in zip(percentage,candidate_raman_xx_list)))
      target_raman_xy.append(sum(x*y for x,y in zip(percentage,candidate_raman_xy_list)))
      target_raman_xz.append(sum(x*y for x,y in zip(percentage,candidate_raman_xz_list)))
      target_raman_zz.append(sum(x*y for x,y in zip(percentage,candidate_raman_zz_list)))
      target_sfg_yyz.append(sum(x*y for x,y in zip(percentage,candidate_sfg_yyz_list)))
      target_sfg_yzy.append(sum(x*y for x,y in zip(percentage,candidate_sfg_yzy_list)))
      target_sfg_zzz.append(sum(x*y for x,y in zip(percentage,candidate_sfg_zzz_list)))

    #different target for different experiment
    target1 = target_ir_x + target_ir_z
    target2 = target_raman_xx + target_raman_xy + target_raman_xz + target_raman_zz
    target3 = target_sfg_yyz + target_sfg_yzy + target_sfg_zzz
    target4 = target_ir_x + target_ir_z + target_raman_xx + target_raman_xy + target_raman_xz + target_raman_zz
    target5 = target_ir_x + target_ir_z + target_sfg_yyz + target_sfg_yzy + target_sfg_zzz
    target6 = target_raman_xx + target_raman_xy + target_raman_xz + target_raman_zz + target_sfg_yyz + target_sfg_yzy + target_sfg_zzz
    target7 = target_ir_x + target_ir_z + target_raman_xx + target_raman_xy + target_raman_xz + target_raman_zz + target_sfg_yyz + target_sfg_yzy + target_sfg_zzz

    #generate different candidates files

    #---------------------------------------------------------------------------
    #Experiment 1
    data_file = open('candidates1.txt','w')

    num_candi = str(len(percentage))
    num_point = str(len(probe_arrange)*2)
    data_file.write(num_candi + ' ' + num_point + '\n')

    # write target data to data file
    for t in target1:
      data_file.write(str(t) + ' ')
    data_file.write('\n')

    # write each candidate data to data file
    for candidate in candidates:
      data_file.write("candidate" + str(candidate.theta) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.ir_x(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.ir_z(probe)) + ' ')
      data_file.write('\n')
    data_file.close()

    #---------------------------------------------------------------------------
    #Experiment 2
    data_file = open('candidates2.txt','w')

    num_candi = str(len(percentage))
    num_point = str(len(probe_arrange)*4)
    data_file.write(num_candi + ' ' + num_point + '\n')

    # write target data to data file
    for t in target2:
      data_file.write(str(t) + ' ')
    data_file.write('\n')

    # write each candidate data to data file
    for candidate in candidates:
      data_file.write("candidate" + str(candidate.theta) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.raman_xx(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.raman_xy(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.raman_xz(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.raman_zz(probe)) + ' ')
      data_file.write('\n')
    data_file.close()

    #---------------------------------------------------------------------------
    #Experiment 3
    data_file = open('candidates3.txt','w')

    num_candi = str(len(percentage))
    num_point = str(len(probe_arrange)*3)
    data_file.write(num_candi + ' ' + num_point + '\n')

    # write target data to data file
    for t in target3:
      data_file.write(str(t) + ' ')
    data_file.write('\n')

    # write each candidate data to data file
    for candidate in candidates:
      data_file.write("candidate" + str(candidate.theta) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.sfg_yyz(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.sfg_yzy(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.sfg_zzz(probe)) + ' ')
      data_file.write('\n')
    data_file.close()

    #---------------------------------------------------------------------------
    #Experiment 4
    data_file = open('candidates4.txt','w')

    num_candi = str(len(percentage))
    num_point = str(len(probe_arrange)*6)
    data_file.write(num_candi + ' ' + num_point + '\n')

    # write target data to data file
    for t in target4:
      data_file.write(str(t) + ' ')
    data_file.write('\n')

    # write each candidate data to data file
    for candidate in candidates:
      data_file.write("candidate" + str(candidate.theta) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.ir_x(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.ir_z(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.raman_xx(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.raman_xy(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.raman_xz(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.raman_zz(probe)) + ' ')
      data_file.write('\n')
    data_file.close()

    #---------------------------------------------------------------------------
    #Experiment 5
    data_file = open('candidates5.txt','w')

    num_candi = str(len(percentage))
    num_point = str(len(probe_arrange)*5)
    data_file.write(num_candi + ' ' + num_point + '\n')

    # write target data to data file
    for t in target5:
      data_file.write(str(t) + ' ')
    data_file.write('\n')

    # write each candidate data to data file
    for candidate in candidates:
      data_file.write("candidate" + str(candidate.theta) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.ir_x(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.ir_z(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.sfg_yyz(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.sfg_yzy(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.sfg_zzz(probe)) + ' ')
      data_file.write('\n')
    data_file.close()

    #---------------------------------------------------------------------------
    #Experiment 6
    data_file = open('candidates6.txt','w')

    num_candi = str(len(percentage))
    num_point = str(len(probe_arrange)*7)
    data_file.write(num_candi + ' ' + num_point + '\n')

    # write target data to data file
    for t in target6:
      data_file.write(str(t) + ' ')
    data_file.write('\n')

    # write each candidate data to data file
    for candidate in candidates:
      data_file.write("candidate" + str(candidate.theta) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.raman_xx(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.raman_xy(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.raman_xz(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.raman_zz(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.sfg_yyz(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.sfg_yzy(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.sfg_zzz(probe)) + ' ')
      data_file.write('\n')
    data_file.close()


    #---------------------------------------------------------------------------
    #Experiment 7
    data_file = open('candidates7.txt','w')

    num_candi = str(len(percentage))
    num_point = str(len(probe_arrange)*9)
    data_file.write(num_candi + ' ' + num_point + '\n')

    # write target data to data file
    for t in target7:
      data_file.write(str(t) + ' ')
    data_file.write('\n')

    # write each candidate data to data file
    for candidate in candidates:
      data_file.write("candidate" + str(candidate.theta) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.ir_x(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.ir_z(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.raman_xx(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.raman_xy(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.raman_xz(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.raman_zz(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.sfg_yyz(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.sfg_yzy(probe)) + ' ')
      for probe in probe_arrange:
        data_file.write(str(candidate.sfg_zzz(probe)) + ' ')
      data_file.write('\n')
    data_file.close()
