import pylab, pickle, sys
from candidate_class import *

# for testing, base on the passing pickle file, create candidates with different theta 
pickle_file = sys.argv[1]
theta_list = [0, 10, 20, 30]
percentage = [0.1, 0.5, 0.2, 0.2]
probe_arrange = arange(1000,2000,5)

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
candidates = [Candidate(pickle_file, theta) for theta in theta_list]

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

fig = pylab.figure()
ax = fig.add_subplot(111)
x = probe_arrange
'''
ax.plot(x, target_ir_x, label="target_ir_x")
ax.plot(x, target_ir_z, label="target_ir_z")
ax.plot(x, target_raman_xx, label="target_raman_xx")
ax.plot(x, target_raman_xy, label="target_raman_xy")
ax.plot(x, target_raman_xz, label="target_raman_xz")
ax.plot(x, target_raman_zz, label="target_raman_zz")
ax.plot(x, target_sfg_yyz, label="target_sfg_yyz")
ax.plot(x, target_sfg_yzy, label="target_sfg_yzy")
ax.plot(x, target_sfg_zzz, label="target_sfg_zzz")
'''

# generate candidate spectroscopy
for candidate in candidates:
  candidate_ir_x = []
  candidate_ir_z = []
  candidate_raman_xx = []
  candidate_raman_xy = []
  candidate_raman_xz = []
  candidate_raman_zz = []
  candidate_sfg_yyz = []
  candidate_sfg_yzy = []
  candidate_sfg_zzz = []
  for probe in probe_arrange:
    candidate_ir_x.append(candidate.ir_x(probe))
  for probe in probe_arrange:
    candidate_ir_z.append(candidate.ir_z(probe))
  for probe in probe_arrange:
    candidate_raman_xx.append(candidate.raman_xx(probe))
  for probe in probe_arrange:
    candidate_raman_xy.append(candidate.raman_xy(probe))
  for probe in probe_arrange:
    candidate_raman_xz.append(candidate.raman_xz(probe))
  for probe in probe_arrange:
    candidate_raman_zz.append(candidate.raman_zz(probe))
  for probe in probe_arrange:
    candidate_sfg_yyz.append(candidate.sfg_yyz(probe))
  for probe in probe_arrange:
    candidate_sfg_yzy.append(candidate.sfg_yzy(probe))
  for probe in probe_arrange:
    candidate_sfg_zzz.append(candidate.sfg_zzz(probe))
    
  #ax.plot(x, candidate_ir_x, label="candidate" + str(candidate.theta))
  #ax.plot(x, candidate_ir_z, label="candidate" + str(candidate.theta))
  #ax.plot(x, candidate_raman_xx, label="candidate_raman_xx_" + str(candidate.theta))
  #ax.plot(x, candidate_raman_xy, label="candidate_raman_xy_" + str(candidate.theta))
  #ax.plot(x, candidate_raman_xz, label="candidate_raman_xz_" + str(candidate.theta))
  ax.plot(x, candidate_raman_zz, label="candidate_raman_zz_" + str(candidate.theta))
  #ax.plot(x, candidate_sfg_yyz, label="candidate_sfg_yyz_" + str(candidate.theta))
  #ax.plot(x, candidate_sfg_yzy, label="candidate_sfg_yzy_" + str(candidate.theta))
  #ax.plot(x, candidate_sfg_zzz, label="candidate_sfg_zzz_" + str(candidate.theta))

pylab.legend(loc=0, fontsize=8)
pylab.savefig('Ala_candidates_plotting_ramanzz.png', dpi=150)

