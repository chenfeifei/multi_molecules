from scipy import *
import pylab, sys
from candidate_class import *

pickle_file = sys.argv[1]
theta_list = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
percentage = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
probe_arrange = arange(1000,2000,5)
result_percentage = [0.25924, 0, 0, 0, 0.344387, 0, 0.154664, 0, 0, 0]
candidates = [Candidate(pickle_file, theta) for theta in theta_list]

target_ir_x = []
target_ir_z = []
target_raman_xx = []
target_raman_xy = []
target_raman_xz = []
target_raman_zz = []
target_sfg_yyz = []
target_sfg_yzy = []
target_sfg_zzz = []


result_ir_x = []
result_ir_z = []
result_raman_xx = []
result_raman_xy = []
result_raman_xz = []
result_raman_zz = []
result_sfg_yyz = []
result_sfg_yzy = []
result_sfg_zzz = []


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
  
  target_ir_x.append(1000*sum(x*y for x,y in zip(percentage,candidate_ir_x_list)))
  target_ir_z.append(1000*sum(x*y for x,y in zip(percentage,candidate_ir_z_list)))
  target_raman_xx.append(sum(x*y for x,y in zip(percentage,candidate_raman_xx_list)))
  target_raman_xy.append(sum(x*y for x,y in zip(percentage,candidate_raman_xy_list)))
  target_raman_xz.append(sum(x*y for x,y in zip(percentage,candidate_raman_xz_list)))
  target_raman_zz.append(sum(x*y for x,y in zip(percentage,candidate_raman_zz_list)))
  target_sfg_yyz.append(sum(x*y for x,y in zip(percentage,candidate_sfg_yyz_list)))
  target_sfg_yzy.append(sum(x*y for x,y in zip(percentage,candidate_sfg_yzy_list)))
  target_sfg_zzz.append(sum(x*y for x,y in zip(percentage,candidate_sfg_zzz_list)))
  
  result_ir_x.append(sum(x*y for x,y in zip(result_percentage,candidate_ir_x_list)))
  result_ir_z.append(sum(x*y for x,y in zip(result_percentage,candidate_ir_z_list)))
  result_raman_xx.append(sum(x*y for x,y in zip(result_percentage,candidate_raman_xx_list)))
  result_raman_xy.append(sum(x*y for x,y in zip(result_percentage,candidate_raman_xy_list)))
  result_raman_xz.append(sum(x*y for x,y in zip(result_percentage,candidate_raman_xz_list)))
  result_raman_zz.append(sum(x*y for x,y in zip(result_percentage,candidate_raman_zz_list)))
  result_sfg_yyz.append(sum(x*y for x,y in zip(result_percentage,candidate_sfg_yyz_list)))
  result_sfg_yzy.append(sum(x*y for x,y in zip(result_percentage,candidate_sfg_yzy_list)))
  result_sfg_zzz.append(sum(x*y for x,y in zip(result_percentage,candidate_sfg_zzz_list)))


fig = pylab.figure()
ax = fig.add_subplot(111)
x = probe_arrange
'''
ax.plot(x, target_ir_x, label="target_ir_x")
ax.plot(x, result_ir_x, label="result_ir_x")
ax.plot(x, target_ir_z, label="target_ir_z")
ax.plot(x, result_ir_z, label="result_ir_z")
'''
ax.plot(x, target_raman_xx, label="target_raman_xx")
ax.plot(x, result_raman_xx, label="result_raman_xx")
ax.plot(x, target_raman_xy, label="target_raman_xy")
ax.plot(x, result_raman_xy, label="result_raman_xy")
ax.plot(x, target_raman_xz, label="target_raman_xz")
ax.plot(x, result_raman_xz, label="result_raman_xz")
ax.plot(x, target_raman_zz, label="target_raman_zz")
ax.plot(x, result_raman_zz, label="result_raman_zz")
'''
ax.plot(x, target_sfg_yyz, label="target_sfg_yyz")
ax.plot(x, result_sfg_yyz, label="result_sfg_yyz")
ax.plot(x, target_sfg_yzy, label="target_sfg_yzy")
ax.plot(x, result_sfg_yzy, label="result_sfg_yzy")
ax.plot(x, target_sfg_zzz, label="target_sfg_zzz")
ax.plot(x, result_sfg_zzz, label="result_sfg_zzz")
'''
pylab.legend(loc=0, fontsize=8)
pylab.savefig('result_target_plotting.png', dpi=150)