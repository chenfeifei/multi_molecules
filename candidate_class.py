#!/usr/bin/env python
from scipy import *
import pylab, pickle, sys
from read_output_files import dipoleProperty
from math import cos, pi
from preIntegratedExpressions import *

# setup
f = 0.936
w = 6

class Candidate:
  def __init__(self, pickle_file, theta0):
    self.pickle_file = pickle_file
    self.theta = theta0
    self.theta0 = float(theta0)/180.*pi
    hndl = open(self.pickle_file, 'rt')
    self.data = pickle.load(hndl)
    hndl.close()
    
  def ir_x(self,probe):
    ir_spectrum_x = 0.0
    for m in range(len(self.data)):
      info = self.data[m]
      mua, mub, muc = info.mus
      prefactor = 1./(2.*info.reducedmass*f*info.freq)
      #muxSquared = 0.5*muc*muc*(1 - cos(self.theta0)**2)
      muxSquared = xTheta(self.theta0,mua,mub,muc)
      ir_spectrum_x += prefactor*(muxSquared)*w*w/((probe - f*info.freq)**2. + w*w)
    return ir_spectrum_x
  
  def ir_y(self,probe):
    ir_spectrum_y = 0.0
    for m in range(len(self.data)):
      info = self.data[m]
      mua, mub, muc = info.mus
      prefactor = 1./(2.*info.reducedmass*f*info.freq)
      #muxSquared = 0.5*muc*muc*(1 - cos(self.theta0)**2)
      muySquared = yTheta(self.theta0,mua,mub,muc)
      ir_spectrum_y += prefactor*(muySquared)*w*w/((probe - f*info.freq)**2. + w*w)
    return ir_spectrum_y

  def ir_z(self,probe):
    ir_spectrum_z = 0.0 
    for m in range(len(self.data)):
      info = self.data[m]
      mua, mub, muc = info.mus
      prefactor = 1./(2.*info.reducedmass*f*info.freq)
      #muzSquared = muc*muc*cos(self.theta0)**2
      muzSquared = zTheta(self.theta0,mua,mub,muc)
      ir_spectrum_z += prefactor*(muzSquared)*w*w/((probe - f*info.freq)**2. + w*w)
    return ir_spectrum_z
  
  def raman_xx(self,probe):
    raman_spectrum_xx = 0.0
    for m in range(len(self.data)):
      info = self.data[m]
      aa, bb, cc, ab, ac, bc, ba, ca, cb = info.alphas
      prefactor = 1./(2.*info.reducedmass*f*info.freq)
      xxSquared = xxTheta(self.theta0,aa,bb,cc,ab,ac,bc)
      raman_spectrum_xx += prefactor*(xxSquared)*w*w/((probe - f*info.freq)**2. + w*w)
    return raman_spectrum_xx

  def raman_xy(self,probe):
    raman_spectrum_xy = 0.0
    for m in range(len(self.data)):
      info = self.data[m]
      aa, bb, cc, ab, ac, bc, ba, ca, cb = info.alphas
      prefactor = 1./(2.*info.reducedmass*f*info.freq)
      xySquared = xyTheta(self.theta0,aa,bb,cc,ab,ac,bc)
      raman_spectrum_xy += prefactor*(xySquared)*w*w/((probe - f*info.freq)**2. + w*w)
    return raman_spectrum_xy
  
  def raman_xz(self,probe):
    raman_spectrum_xz = 0.0
    for m in range(len(self.data)):
      info = self.data[m]
      aa, bb, cc, ab, ac, bc, ba, ca, cb = info.alphas
      prefactor = 1./(2.*info.reducedmass*f*info.freq)
      xzSquared = xzTheta(self.theta0,aa,bb,cc,ab,ac,bc)
      raman_spectrum_xz += prefactor*(xzSquared)*w*w/((probe - f*info.freq)**2. + w*w)
    return raman_spectrum_xz  
  
  def raman_zz(self,probe):
    raman_spectrum_zz = 0.0
    for m in range(len(self.data)):
      info = self.data[m]
      aa, bb, cc, ab, ac, bc, ba, ca, cb = info.alphas
      prefactor = 1./(2.*info.reducedmass*f*info.freq)
      zzSquared = zzTheta(self.theta0,aa,bb,cc,ab,ac,bc)
      raman_spectrum_zz += prefactor*(zzSquared)*w*w/((probe - f*info.freq)**2. + w*w)
    return raman_spectrum_zz
  
  # for SFG, xxz = yyz; xzx = yzy = zxx = zyy; and zzz itself
  def sfg_yyz(self, probe):
    sfg_spectrum_yyz = 0.0
    for m in range(len(self.data)):
      info = self.data[m]
      a, b, c = info.mus
      aa, bb, cc, ab, ac, bc, ba, ca, cb = info.alphas
      prefactor = 1./(2.*info.reducedmass*f*info.freq)
      yyz = yyzTheta(self.theta0,a,b,c,aa,bb,cc,ab,ac,bc)
      sfg_spectrum_yyz += prefactor*yyz*w/(f*info.freq - probe -(0.0+1.0j)*w)
    return sfg_spectrum_yyz.imag

  def sfg_yzy(self, probe):
    sfg_spectrum_yzy = 0.0
    for m in range(len(self.data)):
      info = self.data[m]
      a, b, c = info.mus
      aa, bb, cc, ab, ac, bc, ba, ca, cb = info.alphas
      prefactor = 1./(2.*info.reducedmass*f*info.freq)
      yzy = yzyTheta(self.theta0,a,b,c,aa,bb,cc,ab,ac,bc)
      sfg_spectrum_yzy += prefactor*yzy*w/(f*info.freq - probe -(0.0+1.0j)*w)
    return sfg_spectrum_yzy.imag 

  def sfg_zzz(self, probe):
    sfg_spectrum_zzz = 0.0
    for m in range(len(self.data)):
      info = self.data[m]
      a, b, c = info.mus
      aa, bb, cc, ab, ac, bc, ba, ca, cb = info.alphas
      prefactor = 1./(2.*info.reducedmass*f*info.freq)
      zzz = zzzTheta(self.theta0,a,b,c,aa,bb,cc,ab,ac,bc)
      sfg_spectrum_zzz += prefactor*zzz*w/(f*info.freq - probe -(0.0+1.0j)*w)
    return sfg_spectrum_zzz.imag
