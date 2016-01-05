#!/usr/bin/env python
from scipy import *
import sys, math

#All the inputs are in radians
'''
For chi2, when there is non-uniform tilt and twist angles and uniform phi angle, only 7 elements are non-zeros and only three of them are unique

yyz = xxz
yzy = xzx = zxx = zyy
zzz
'''
def yyzThetaPsi(theta,psi,a,b,c,aa,bb,cc,ab,ac,bc): #This method takes Theta and Psi values as input.This means no angle preference in Phi
	preintYyz = pi * (-sin(theta) * cos(psi) * aa * a + sin(theta) * sin(psi) * aa * b + cos(theta) * aa * c + sin(theta) * cos(psi) ** 3 * aa * a + cos(theta) ** 3 * aa * c * cos(psi) ** 2 - sin(theta) * cos(psi) ** 3 * bb * a + cos(theta) * bb * c * cos(psi) ** 2 + 0.2e1 * sin(theta) * ab * b * cos(psi) - sin(theta) * cos(psi) ** 3 * aa * a * cos(theta) ** 2 - 0.2e1 * bc * b * cos(theta) + cos(theta) * cc * c + 0.2e1 * bc * b * cos(theta) ** 3 - cos(theta) ** 3 * cc * c + cos(theta) ** 3 * bb * c + sin(theta) * sin(psi) * aa * b * cos(theta) ** 2 * cos(psi) ** 2 + 0.2e1 * sin(theta) * cos(psi) ** 2 * ab * a * cos(theta) ** 2 * sin(psi) - 0.2e1 * sin(theta) * cos(psi) ** 2 * ab * a * sin(psi) - 0.2e1 * cos(theta) ** 3 * ab * c * cos(psi) * sin(psi) + 0.2e1 * cos(theta) * ab * c * sin(psi) * cos(psi) + 0.2e1 * sin(theta) * cos(theta) ** 2 * ac * c * cos(psi) + sin(theta) * sin(psi) * bb * b * cos(psi) ** 2 - 0.2e1 * sin(theta) * cos(theta) ** 2 * bc * c * sin(psi) + 0.2e1 * sin(psi) * ac * b * cos(theta) * cos(psi) + 0.2e1 * cos(psi) * bc * a * cos(theta) * sin(psi) + sin(theta) * sin(psi) * bb * b * cos(theta) ** 2 - sin(theta) * cos(psi) * bb * a * cos(theta) ** 2 - 0.2e1 * sin(theta) * ab * b * cos(theta) ** 2 * cos(psi) - 0.2e1 * sin(psi) * ac * b * cos(theta) ** 3 * cos(psi) - 0.2e1 * cos(psi) * bc * a * cos(theta) ** 3 * sin(psi) + 0.2e1 * sin(theta) * ab * b * cos(theta) ** 2 * cos(psi) ** 3 + sin(theta) * cos(psi) ** 3 * bb * a * cos(theta) ** 2 + 0.2e1 * cos(psi) ** 2 * ac * a * cos(theta) ** 3 - 0.2e1 * sin(theta) * ab * b * cos(psi) ** 3 - 0.2e1 * cos(psi) ** 2 * ac * a * cos(theta) - cos(psi) * cc * a * sin(theta) + sin(psi) * cc * b * sin(theta) - aa * c * cos(theta) * cos(psi) ** 2 - cos(theta) ** 3 * bb * c * cos(psi) ** 2 + 0.2e1 * bc * b * cos(theta) * cos(psi) ** 2 - 0.2e1 * bc * b * cos(theta) ** 3 * cos(psi) ** 2 - sin(theta) * sin(psi) * aa * b * cos(psi) ** 2 - sin(psi) * cc * b * sin(theta) * cos(theta) ** 2 - sin(theta) * sin(psi) * bb * b * cos(theta) ** 2 * cos(psi) ** 2 + cos(psi) * cc * a * sin(theta) * cos(theta) ** 2)
        return preintYyz

def yzyThetaPsi(theta,psi,a,b,c,aa,bb,cc,ab,ac,bc): #This method takes Theta and Psi values as input.This means no angle preference in Phi
	preintYzy = pi * (-bb * c * cos(theta) - sin(theta) * cos(psi) * aa * a + sin(theta) * bb * a * cos(psi) - sin(theta) * cos(psi) * ac * c + sin(theta) * sin(psi) * bc * c + sin(theta) * ab * a * sin(psi) + sin(theta) * cos(psi) ** 3 * aa * a + cos(theta) ** 3 * aa * c * cos(psi) ** 2 - sin(theta) * cos(psi) ** 3 * bb * a + cos(theta) * bb * c * cos(psi) ** 2 + sin(theta) * ab * b * cos(psi) - sin(theta) * cos(psi) ** 3 * aa * a * cos(theta) ** 2 + ac * a * cos(theta) - bc * b * cos(theta) + cos(theta) * cc * c + 0.2e1 * bc * b * cos(theta) ** 3 - cos(theta) ** 3 * cc * c + cos(theta) ** 3 * bb * c + sin(theta) * sin(psi) * aa * b * cos(theta) ** 2 * cos(psi) ** 2 + 0.2e1 * sin(theta) * cos(psi) ** 2 * ab * a * cos(theta) ** 2 * sin(psi) - 0.2e1 * sin(theta) * cos(psi) ** 2 * ab * a * sin(psi) - 0.2e1 * cos(theta) ** 3 * ab * c * cos(psi) * sin(psi) + 0.2e1 * cos(theta) * ab * c * sin(psi) * cos(psi) + 0.2e1 * sin(theta) * cos(theta) ** 2 * ac * c * cos(psi) + sin(theta) * sin(psi) * bb * b * cos(psi) ** 2 - 0.2e1 * sin(theta) * cos(theta) ** 2 * bc * c * sin(psi) + 0.2e1 * sin(psi) * ac * b * cos(theta) * cos(psi) + 0.2e1 * cos(psi) * bc * a * cos(theta) * sin(psi) + sin(theta) * sin(psi) * bb * b * cos(theta) ** 2 - sin(theta) * cos(psi) * bb * a * cos(theta) ** 2 - 0.2e1 * sin(theta) * ab * b * cos(theta) ** 2 * cos(psi) - 0.2e1 * sin(psi) * ac * b * cos(theta) ** 3 * cos(psi) - 0.2e1 * cos(psi) * bc * a * cos(theta) ** 3 * sin(psi) + 0.2e1 * sin(theta) * ab * b * cos(theta) ** 2 * cos(psi) ** 3 + sin(theta) * cos(psi) ** 3 * bb * a * cos(theta) ** 2 + 0.2e1 * cos(psi) ** 2 * ac * a * cos(theta) ** 3 - 0.2e1 * sin(theta) * ab * b * cos(psi) ** 3 - 0.2e1 * cos(psi) ** 2 * ac * a * cos(theta) - aa * c * cos(theta) * cos(psi) ** 2 - cos(theta) ** 3 * bb * c * cos(psi) ** 2 + 0.2e1 * bc * b * cos(theta) * cos(psi) ** 2 - 0.2e1 * bc * b * cos(theta) ** 3 * cos(psi) ** 2 - sin(theta) * sin(psi) * aa * b * cos(psi) ** 2 - sin(psi) * cc * b * sin(theta) * cos(theta) ** 2 - sin(theta) * sin(psi) * bb * b * cos(theta) ** 2 * cos(psi) ** 2 + cos(psi) * cc * a * sin(theta) * cos(theta) ** 2)
	return preintYzy

def zzzThetaPsi(theta,psi,a,b,c,aa,bb,cc,ab,ac,bc): #This method takes Theta and Psi values as input.This means no angle preference in Phi
	preintZzz = -0.2e1 * pi * (-bb * c * cos(theta) + sin(theta) * bb * a * cos(psi) - sin(theta) * sin(psi) * bb * b + sin(theta) * cos(psi) ** 3 * aa * a + cos(theta) ** 3 * aa * c * cos(psi) ** 2 - sin(theta) * cos(psi) ** 3 * bb * a + cos(theta) * bb * c * cos(psi) ** 2 + 0.2e1 * sin(theta) * ab * b * cos(psi) - sin(theta) * cos(psi) ** 3 * aa * a * cos(theta) ** 2 - 0.2e1 * bc * b * cos(theta) + 0.2e1 * bc * b * cos(theta) ** 3 - cos(theta) ** 3 * cc * c + cos(theta) ** 3 * bb * c + sin(theta) * sin(psi) * aa * b * cos(theta) ** 2 * cos(psi) ** 2 + 0.2e1 * sin(theta) * cos(psi) ** 2 * ab * a * cos(theta) ** 2 * sin(psi) - 0.2e1 * sin(theta) * cos(psi) ** 2 * ab * a * sin(psi) - 0.2e1 * cos(theta) ** 3 * ab * c * cos(psi) * sin(psi) + 0.2e1 * cos(theta) * ab * c * sin(psi) * cos(psi) + 0.2e1 * sin(theta) * cos(theta) ** 2 * ac * c * cos(psi) + sin(theta) * sin(psi) * bb * b * cos(psi) ** 2 - 0.2e1 * sin(theta) * cos(theta) ** 2 * bc * c * sin(psi) + 0.2e1 * sin(psi) * ac * b * cos(theta) * cos(psi) + 0.2e1 * cos(psi) * bc * a * cos(theta) * sin(psi) + sin(theta) * sin(psi) * bb * b * cos(theta) ** 2 - sin(theta) * cos(psi) * bb * a * cos(theta) ** 2 - 0.2e1 * sin(theta) * ab * b * cos(theta) ** 2 * cos(psi) - 0.2e1 * sin(psi) * ac * b * cos(theta) ** 3 * cos(psi) - 0.2e1 * cos(psi) * bc * a * cos(theta) ** 3 * sin(psi) + 0.2e1 * sin(theta) * ab * b * cos(theta) ** 2 * cos(psi) ** 3 + sin(theta) * cos(psi) ** 3 * bb * a * cos(theta) ** 2 + 0.2e1 * cos(psi) ** 2 * ac * a * cos(theta) ** 3 - 0.2e1 * sin(theta) * ab * b * cos(psi) ** 3 - 0.2e1 * cos(psi) ** 2 * ac * a * cos(theta) - aa * c * cos(theta) * cos(psi) ** 2 - cos(theta) ** 3 * bb * c * cos(psi) ** 2 + 0.2e1 * bc * b * cos(theta) * cos(psi) ** 2 - 0.2e1 * bc * b * cos(theta) ** 3 * cos(psi) ** 2 - sin(theta) * sin(psi) * aa * b * cos(psi) ** 2 - sin(psi) * cc * b * sin(theta) * cos(theta) ** 2 - sin(theta) * sin(psi) * bb * b * cos(theta) ** 2 * cos(psi) ** 2 + cos(psi) * cc * a * sin(theta) * cos(theta) ** 2)
        return preintZzz


def yyzTheta(theta,a,b,c,aa,bb,cc,ab,ac,bc): #This method takes Theta as input.This means no angle preference in Phi and Psi
        preIntYyzOverPhiPsi = pi ** 2 * cos(theta) * (bb * c + aa * c + (2 * cc * c) + cos(theta) ** 2 * bb * c + cos(theta) ** 2 * aa * c - (2 * bc * b) - 0.2e1 * cos(theta) ** 2 * cc * c + 0.2e1 * bc * b * cos(theta) ** 2 + 0.2e1 * ac * a * cos(theta) ** 2 - 0.2e1 * ac * a)
        return preIntYyzOverPhiPsi

def yzyTheta(theta,a,b,c,aa,bb,cc,ab,ac,bc): #This method takes Theta as input.This means no angle preference in Phi and Psi
        preIntYzyOverPhiPsi = cos(theta) * pi ** 2 * (-bb * c - aa * c + (2 * cc * c) + cos(theta) ** 2 * bb * c + cos(theta) ** 2 * aa * c - 0.2e1 * cos(theta) ** 2 * cc * c + 0.2e1 * bc * b * cos(theta) ** 2 + 0.2e1 * ac * a * cos(theta) ** 2)
        return preIntYzyOverPhiPsi

def zzzTheta(theta,a,b,c,aa,bb,cc,ab,ac,bc): #This method takes Theta as input.This means no angle preference in Phi and Psi
        preIntZzzOverPhiPsi = -0.2e1 * cos(theta) * pi ** 2 * (-bb * c - aa * c + cos(theta) ** 2 * bb * c + cos(theta) ** 2 * aa * c - (2 * bc * b) - 0.2e1 * cos(theta) ** 2 * cc * c + 0.2e1 * bc * b * cos(theta) ** 2 + 0.2e1 * ac * a * cos(theta) ** 2 - 0.2e1 * ac * a)

        return preIntZzzOverPhiPsi

'''
For theta psi, all the elements are different

'''
def xxThetaPsi(theta,psi,aa,bb,cc,ab,ac,bc):
	preIntxx = pi * (0.24e2 * aa * cos(theta) ** 2 * cos(psi) ** 3 * ab * sin(psi) - 0.24e2 * ab * cos(theta) ** 2 * sin(psi) * cos(psi) ** 3 * bb + 0.24e2 * ab * cos(psi) ** 3 * cos(theta) * sin(theta) * bc + 0.12e2 * sin(theta) * ac * cos(theta) * cos(psi) ** 3 * bb + 0.12e2 * sin(theta) * bc * cos(theta) ** 3 * sin(psi) * cc + 0.12e2 * ab * cos(theta) ** 4 * sin(psi) * cos(psi) ** 3 * bb - 0.12e2 * sin(theta) * ac * cos(theta) ** 3 * cos(psi) * cc - 0.12e2 * ab ** 2 * cos(psi) ** 4 - 0.12e2 * aa * cos(theta) ** 4 * cos(psi) ** 3 * ab * sin(psi) + 0.12e2 * aa * cos(theta) ** 3 * cos(psi) ** 3 * sin(theta) * ac + 0.3e1 * bb ** 2 * cos(psi) ** 4 + 0.6e1 * bb * cos(theta) ** 2 * cc + 0.6e1 * bb ** 2 * cos(theta) ** 2 * cos(psi) ** 2 + 0.12e2 * ab ** 2 * cos(theta) ** 4 * cos(psi) ** 2 + 0.6e1 * aa * cos(theta) ** 4 * cos(psi) ** 2 * bb + 0.12e2 * aa * sin(psi) * ab * cos(psi) - 0.6e1 * aa * cos(theta) ** 4 * cos(psi) ** 4 * bb - 0.12e2 * aa * sin(psi) * ab * cos(psi) ** 3 + 0.12e2 * ab ** 2 * cos(psi) ** 2 + 0.3e1 * bb ** 2 * cos(theta) ** 4 + 0.4e1 * ab ** 2 * cos(theta) ** 2 + 0.4e1 * bc ** 2 * cos(psi) ** 2 - 0.12e2 * bc ** 2 * cos(theta) ** 4 + 0.6e1 * aa ** 2 * cos(theta) ** 2 * cos(psi) ** 2 + 0.4e1 * ab * cos(psi) * sin(psi) * cc + 0.8e1 * ac * sin(psi) * bc * cos(psi) + 0.12e2 * aa * cos(theta) ** 2 * cos(psi) ** 4 * bb + 0.12e2 * ab * cos(psi) ** 3 * sin(psi) * bb + 0.2e1 * aa * bb * cos(theta) ** 2 - 0.6e1 * bb ** 2 * cos(theta) ** 2 * cos(psi) ** 4 - 0.6e1 * aa ** 2 * cos(theta) ** 2 * cos(psi) ** 4 - 0.6e1 * bb * cos(theta) ** 4 * cc + 0.12e2 * bc ** 2 * cos(theta) ** 2 - 0.12e2 * aa * cos(theta) * cos(psi) ** 3 * sin(theta) * ac - 0.24e2 * ab * cos(theta) ** 3 * cos(psi) ** 3 * sin(theta) * bc - 0.12e2 * sin(theta) * ac * cos(theta) ** 3 * cos(psi) ** 3 * bb - 0.12e2 * sin(theta) * bc * cos(theta) * sin(psi) * cc - 0.12e2 * ab * cos(theta) ** 4 * sin(psi) * cos(psi) * bb - 0.8e1 * ab * cos(theta) * sin(psi) * sin(theta) * ac - 0.8e1 * sin(theta) * ac * bb * cos(theta) * cos(psi) + 0.12e2 * sin(theta) * ac * cos(theta) * cos(psi) * cc - 0.12e2 * aa * cos(theta) ** 2 * cos(psi) * sin(psi) * ab - 0.4e1 * aa * sin(psi) * sin(theta) * bc * cos(theta) + 0.12e2 * ab * cos(theta) ** 2 * sin(psi) * bb * cos(psi) + 0.3e1 * aa ** 2 + 0.3e1 * cc ** 2 + 0.4e1 * ac ** 2 + 0.2e1 * aa * cc - 0.6e1 * aa ** 2 * cos(psi) ** 2 + 0.3e1 * aa ** 2 * cos(psi) ** 4 - 0.4e1 * ac ** 2 * cos(psi) ** 2 - 0.4e1 * ac ** 2 * cos(theta) ** 2 - 0.6e1 * cc ** 2 * cos(theta) ** 2 + 0.3e1 * cc ** 2 * cos(theta) ** 4 + 0.12e2 * bb * cos(theta) ** 3 * sin(psi) * sin(theta) * bc * cos(psi) ** 2 + 0.3e1 * aa ** 2 * cos(theta) ** 4 * cos(psi) ** 4 + 0.24e2 * ab ** 2 * cos(psi) ** 4 * cos(theta) ** 2 - 0.8e1 * bb * cos(psi) ** 2 * cc * cos(theta) ** 2 - 0.12e2 * aa * bb * cos(theta) ** 2 * cos(psi) ** 2 + 0.8e1 * aa * cc * cos(theta) ** 2 * cos(psi) ** 2 - 0.6e1 * aa * cc * cos(theta) ** 4 * cos(psi) ** 2 + 0.6e1 * bb * cos(theta) ** 4 * cc * cos(psi) ** 2 - 0.24e2 * ab ** 2 * cos(theta) ** 2 * cos(psi) ** 2 + 0.16e2 * ac ** 2 * cos(theta) ** 2 * cos(psi) ** 2 - 0.16e2 * bc ** 2 * cos(psi) ** 2 * cos(theta) ** 2 - 0.6e1 * bb ** 2 * cos(theta) ** 4 * cos(psi) ** 2 + 0.3e1 * bb ** 2 * cos(theta) ** 4 * cos(psi) ** 4 - 0.2e1 * aa * cc * cos(psi) ** 2 - 0.2e1 * aa * cc * cos(theta) ** 2 - 0.12e2 * ac ** 2 * cos(theta) ** 4 * cos(psi) ** 2 + 0.12e2 * bc ** 2 * cos(theta) ** 4 * cos(psi) ** 2 + 0.12e2 * aa * cos(theta) * cos(psi) * sin(theta) * ac + 0.24e2 * ab * cos(theta) ** 3 * cos(psi) * sin(theta) * bc + 0.12e2 * sin(theta) * ac * cos(theta) ** 3 * cos(psi) * bb - 0.16e2 * ab * cos(theta) * sin(theta) * bc * cos(psi) + 0.12e2 * aa * cos(theta) * cos(psi) ** 2 * sin(psi) * sin(theta) * bc + 0.24e2 * ab * cos(psi) ** 2 * cos(theta) * sin(theta) * ac * sin(psi) - 0.12e2 * bb * cos(theta) * sin(psi) * cos(psi) ** 2 * sin(theta) * bc - 0.12e2 * aa * cos(theta) ** 3 * cos(psi) ** 2 * sin(theta) * bc * sin(psi) - 0.24e2 * ab * cos(theta) ** 3 * sin(psi) * cos(psi) ** 2 * sin(theta) * ac - 0.32e2 * ac * sin(psi) * bc * cos(psi) * cos(theta) ** 2 + 0.12e2 * ab * cos(psi) * sin(psi) * cc * cos(theta) ** 4 + 0.24e2 * ac * sin(psi) * bc * cos(psi) * cos(theta) ** 4 - 0.16e2 * ab * cos(psi) * sin(psi) * cc * cos(theta) ** 2 + 0.2e1 * bb * cos(psi) ** 2 * cc - 0.6e1 * aa * bb * cos(psi) ** 4 - 0.12e2 * ab ** 2 * cos(theta) ** 4 * cos(psi) ** 4 + 0.6e1 * aa * bb * cos(psi) ** 2 - 0.12e2 * bb * cos(theta) ** 3 * sin(psi) * sin(theta) * bc) / 0.4e1
	return preIntxx
def xyThetaPsi(theta,psi,aa,bb,cc,ab,ac,bc):
	preIntxy = pi * (0.8e1 * aa * cos(theta) ** 2 * cos(psi) ** 3 * ab * sin(psi) - 0.8e1 * ab * cos(theta) ** 2 * sin(psi) * cos(psi) ** 3 * bb + 0.8e1 * ab * cos(psi) ** 3 * cos(theta) * sin(theta) * bc + 0.4e1 * sin(theta) * ac * cos(theta) * cos(psi) ** 3 * bb + 0.4e1 * sin(theta) * bc * cos(theta) ** 3 * sin(psi) * cc + 0.4e1 * ab * cos(theta) ** 4 * sin(psi) * cos(psi) ** 3 * bb - 0.4e1 * sin(theta) * ac * cos(theta) ** 3 * cos(psi) * cc - 0.4e1 * ab ** 2 * cos(psi) ** 4 - 0.4e1 * aa * cos(theta) ** 4 * cos(psi) ** 3 * ab * sin(psi) + 0.4e1 * aa * cos(theta) ** 3 * cos(psi) ** 3 * sin(theta) * ac + bb ** 2 * cos(psi) ** 4 + 0.2e1 * bb * cos(theta) ** 2 * cc + 0.2e1 * bb ** 2 * cos(theta) ** 2 * cos(psi) ** 2 + 0.4e1 * ab ** 2 * cos(theta) ** 4 * cos(psi) ** 2 + 0.2e1 * aa * cos(theta) ** 4 * cos(psi) ** 2 * bb + 0.4e1 * aa * sin(psi) * ab * cos(psi) - 0.2e1 * aa * cos(theta) ** 4 * cos(psi) ** 4 * bb - 0.4e1 * aa * sin(psi) * ab * cos(psi) ** 3 + 0.4e1 * ab ** 2 * cos(psi) ** 2 + bb ** 2 * cos(theta) ** 4 + 0.4e1 * ab ** 2 * cos(theta) ** 2 + 0.4e1 * bc ** 2 * cos(psi) ** 2 - 0.4e1 * bc ** 2 * cos(theta) ** 4 + 0.2e1 * aa ** 2 * cos(theta) ** 2 * cos(psi) ** 2 - 0.4e1 * ab * cos(psi) * sin(psi) * cc + 0.8e1 * ac * sin(psi) * bc * cos(psi) + 0.4e1 * aa * cos(theta) ** 2 * cos(psi) ** 4 * bb + 0.4e1 * ab * cos(psi) ** 3 * sin(psi) * bb - 0.2e1 * aa * bb * cos(theta) ** 2 - 0.2e1 * bb ** 2 * cos(theta) ** 2 * cos(psi) ** 4 - 0.2e1 * aa ** 2 * cos(theta) ** 2 * cos(psi) ** 4 - 0.2e1 * bb * cos(theta) ** 4 * cc + 0.4e1 * bc ** 2 * cos(theta) ** 2 - 0.4e1 * aa * cos(theta) * cos(psi) ** 3 * sin(theta) * ac - 0.8e1 * ab * cos(theta) ** 3 * cos(psi) ** 3 * sin(theta) * bc - 0.4e1 * sin(theta) * ac * cos(theta) ** 3 * cos(psi) ** 3 * bb - 0.4e1 * sin(theta) * bc * cos(theta) * sin(psi) * cc - 0.4e1 * ab * cos(theta) ** 4 * sin(psi) * cos(psi) * bb - 0.8e1 * ab * cos(theta) * sin(psi) * sin(theta) * ac - 0.8e1 * sin(theta) * ac * bb * cos(theta) * cos(psi) + 0.4e1 * sin(theta) * ac * cos(theta) * cos(psi) * cc - 0.4e1 * aa * cos(theta) ** 2 * cos(psi) * sin(psi) * ab + 0.4e1 * aa * sin(psi) * sin(theta) * bc * cos(theta) + 0.4e1 * ab * cos(theta) ** 2 * sin(psi) * bb * cos(psi) + aa ** 2 + cc ** 2 + 0.4e1 * ac ** 2 - 0.2e1 * aa * cc - 0.2e1 * aa ** 2 * cos(psi) ** 2 + aa ** 2 * cos(psi) ** 4 - 0.4e1 * ac ** 2 * cos(psi) ** 2 - 0.4e1 * ac ** 2 * cos(theta) ** 2 - 0.2e1 * cc ** 2 * cos(theta) ** 2 + cc ** 2 * cos(theta) ** 4 + 0.4e1 * bb * cos(theta) ** 3 * sin(psi) * sin(theta) * bc * cos(psi) ** 2 + aa ** 2 * cos(theta) ** 4 * cos(psi) ** 4 + 0.8e1 * ab ** 2 * cos(psi) ** 4 * cos(theta) ** 2 - 0.4e1 * aa * bb * cos(theta) ** 2 * cos(psi) ** 2 - 0.2e1 * aa * cc * cos(theta) ** 4 * cos(psi) ** 2 + 0.2e1 * bb * cos(theta) ** 4 * cc * cos(psi) ** 2 - 0.8e1 * ab ** 2 * cos(theta) ** 2 * cos(psi) ** 2 + 0.8e1 * ac ** 2 * cos(theta) ** 2 * cos(psi) ** 2 - 0.8e1 * bc ** 2 * cos(psi) ** 2 * cos(theta) ** 2 - 0.2e1 * bb ** 2 * cos(theta) ** 4 * cos(psi) ** 2 + bb ** 2 * cos(theta) ** 4 * cos(psi) ** 4 + 0.2e1 * aa * cc * cos(psi) ** 2 + 0.2e1 * aa * cc * cos(theta) ** 2 - 0.4e1 * ac ** 2 * cos(theta) ** 4 * cos(psi) ** 2 + 0.4e1 * bc ** 2 * cos(theta) ** 4 * cos(psi) ** 2 + 0.4e1 * aa * cos(theta) * cos(psi) * sin(theta) * ac + 0.8e1 * ab * cos(theta) ** 3 * cos(psi) * sin(theta) * bc + 0.4e1 * sin(theta) * ac * cos(theta) ** 3 * cos(psi) * bb + 0.4e1 * aa * cos(theta) * cos(psi) ** 2 * sin(psi) * sin(theta) * bc + 0.8e1 * ab * cos(psi) ** 2 * cos(theta) * sin(theta) * ac * sin(psi) - 0.4e1 * bb * cos(theta) * sin(psi) * cos(psi) ** 2 * sin(theta) * bc - 0.4e1 * aa * cos(theta) ** 3 * cos(psi) ** 2 * sin(theta) * bc * sin(psi) - 0.8e1 * ab * cos(theta) ** 3 * sin(psi) * cos(psi) ** 2 * sin(theta) * ac - 0.16e2 * ac * sin(psi) * bc * cos(psi) * cos(theta) ** 2 + 0.4e1 * ab * cos(psi) * sin(psi) * cc * cos(theta) ** 4 + 0.8e1 * ac * sin(psi) * bc * cos(psi) * cos(theta) ** 4 - 0.2e1 * bb * cos(psi) ** 2 * cc - 0.2e1 * aa * bb * cos(psi) ** 4 - 0.4e1 * ab ** 2 * cos(theta) ** 4 * cos(psi) ** 4 + 0.2e1 * aa * bb * cos(psi) ** 2 - 0.4e1 * bb * cos(theta) ** 3 * sin(psi) * sin(theta) * bc) / 0.4e1
	return preIntxy
def xzThetaPsi(theta,psi,aa,bb,cc,ab,ac,bc):
	preIntxz = -pi * (0.8e1 * aa * cos(theta) ** 2 * cos(psi) ** 3 * ab * sin(psi) - 0.8e1 * ab * cos(theta) ** 2 * sin(psi) * cos(psi) ** 3 * bb + 0.8e1 * ab * cos(psi) ** 3 * cos(theta) * sin(theta) * bc + 0.4e1 * sin(theta) * ac * cos(theta) * cos(psi) ** 3 * bb + 0.4e1 * sin(theta) * bc * cos(theta) ** 3 * sin(psi) * cc + 0.4e1 * ab * cos(theta) ** 4 * sin(psi) * cos(psi) ** 3 * bb - 0.4e1 * sin(theta) * ac * cos(theta) ** 3 * cos(psi) * cc - 0.4e1 * ab ** 2 * cos(psi) ** 4 - 0.4e1 * aa * cos(theta) ** 4 * cos(psi) ** 3 * ab * sin(psi) + 0.4e1 * aa * cos(theta) ** 3 * cos(psi) ** 3 * sin(theta) * ac + bb ** 2 * cos(psi) ** 4 + 0.2e1 * bb * cos(theta) ** 2 * cc + 0.3e1 * bb ** 2 * cos(theta) ** 2 * cos(psi) ** 2 + 0.4e1 * ab ** 2 * cos(theta) ** 4 * cos(psi) ** 2 + 0.2e1 * aa * cos(theta) ** 4 * cos(psi) ** 2 * bb + 0.2e1 * aa * sin(psi) * ab * cos(psi) - 0.2e1 * aa * cos(theta) ** 4 * cos(psi) ** 4 * bb - 0.4e1 * aa * sin(psi) * ab * cos(psi) ** 3 + 0.4e1 * ab ** 2 * cos(psi) ** 2 + bb ** 2 * cos(theta) ** 4 + ab ** 2 * cos(theta) ** 2 + bc ** 2 * cos(psi) ** 2 - 0.4e1 * bc ** 2 * cos(theta) ** 4 + aa ** 2 * cos(theta) ** 2 * cos(psi) ** 2 + 0.2e1 * ac * sin(psi) * bc * cos(psi) + 0.4e1 * aa * cos(theta) ** 2 * cos(psi) ** 4 * bb + 0.4e1 * ab * cos(psi) ** 3 * sin(psi) * bb - 0.2e1 * bb ** 2 * cos(theta) ** 2 * cos(psi) ** 4 - 0.2e1 * aa ** 2 * cos(theta) ** 2 * cos(psi) ** 4 - 0.2e1 * bb * cos(theta) ** 4 * cc + 0.4e1 * bc ** 2 * cos(theta) ** 2 - 0.4e1 * aa * cos(theta) * cos(psi) ** 3 * sin(theta) * ac - 0.8e1 * ab * cos(theta) ** 3 * cos(psi) ** 3 * sin(theta) * bc - 0.4e1 * sin(theta) * ac * cos(theta) ** 3 * cos(psi) ** 3 * bb - 0.2e1 * sin(theta) * bc * cos(theta) * sin(psi) * cc - 0.4e1 * ab * cos(theta) ** 4 * sin(psi) * cos(psi) * bb - 0.2e1 * ab * cos(theta) * sin(psi) * sin(theta) * ac - 0.4e1 * sin(theta) * ac * bb * cos(theta) * cos(psi) + 0.2e1 * sin(theta) * ac * cos(theta) * cos(psi) * cc - 0.2e1 * aa * cos(theta) ** 2 * cos(psi) * sin(psi) * ab + 0.6e1 * ab * cos(theta) ** 2 * sin(psi) * bb * cos(psi) - bb ** 2 * cos(theta) ** 2 - bb ** 2 * cos(psi) ** 2 - ab ** 2 - bc ** 2 - aa ** 2 * cos(psi) ** 2 + aa ** 2 * cos(psi) ** 4 - ac ** 2 * cos(psi) ** 2 - ac ** 2 * cos(theta) ** 2 - cc ** 2 * cos(theta) ** 2 + cc ** 2 * cos(theta) ** 4 + 0.4e1 * bb * cos(theta) ** 3 * sin(psi) * sin(theta) * bc * cos(psi) ** 2 + aa ** 2 * cos(theta) ** 4 * cos(psi) ** 4 + 0.8e1 * ab ** 2 * cos(psi) ** 4 * cos(theta) ** 2 - 0.2e1 * bb * cos(psi) ** 2 * cc * cos(theta) ** 2 - 0.4e1 * aa * bb * cos(theta) ** 2 * cos(psi) ** 2 + 0.2e1 * aa * cc * cos(theta) ** 2 * cos(psi) ** 2 - 0.2e1 * aa * cc * cos(theta) ** 4 * cos(psi) ** 2 + 0.2e1 * bb * cos(theta) ** 4 * cc * cos(psi) ** 2 - 0.8e1 * ab ** 2 * cos(theta) ** 2 * cos(psi) ** 2 + 0.5e1 * ac ** 2 * cos(theta) ** 2 * cos(psi) ** 2 - 0.5e1 * bc ** 2 * cos(psi) ** 2 * cos(theta) ** 2 - 0.2e1 * bb ** 2 * cos(theta) ** 4 * cos(psi) ** 2 + bb ** 2 * cos(theta) ** 4 * cos(psi) ** 4 - 0.4e1 * ac ** 2 * cos(theta) ** 4 * cos(psi) ** 2 + 0.4e1 * bc ** 2 * cos(theta) ** 4 * cos(psi) ** 2 + 0.2e1 * aa * cos(theta) * cos(psi) * sin(theta) * ac + 0.8e1 * ab * cos(theta) ** 3 * cos(psi) * sin(theta) * bc + 0.4e1 * sin(theta) * ac * cos(theta) ** 3 * cos(psi) * bb - 0.6e1 * ab * cos(theta) * sin(theta) * bc * cos(psi) + 0.4e1 * aa * cos(theta) * cos(psi) ** 2 * sin(psi) * sin(theta) * bc + 0.8e1 * ab * cos(psi) ** 2 * cos(theta) * sin(theta) * ac * sin(psi) - 0.4e1 * bb * cos(theta) * sin(psi) * cos(psi) ** 2 * sin(theta) * bc - 0.4e1 * aa * cos(theta) ** 3 * cos(psi) ** 2 * sin(theta) * bc * sin(psi) - 0.8e1 * ab * cos(theta) ** 3 * sin(psi) * cos(psi) ** 2 * sin(theta) * ac - 0.10e2 * ac * sin(psi) * bc * cos(psi) * cos(theta) ** 2 + 0.4e1 * ab * cos(psi) * sin(psi) * cc * cos(theta) ** 4 + 0.8e1 * ac * sin(psi) * bc * cos(psi) * cos(theta) ** 4 - 0.4e1 * ab * cos(psi) * sin(psi) * cc * cos(theta) ** 2 - 0.2e1 * aa * bb * cos(psi) ** 4 - 0.4e1 * ab ** 2 * cos(theta) ** 4 * cos(psi) ** 4 + 0.2e1 * aa * bb * cos(psi) ** 2 + 0.2e1 * sin(theta) * sin(psi) * bb * cos(theta) * bc - 0.4e1 * bb * cos(theta) ** 3 * sin(psi) * sin(theta) * bc - 0.2e1 * sin(psi) * ab * bb * cos(psi))
	return preIntxz
def yyThetaPsi(theta,psi,aa,bb,cc,ab,ac,bc):
	preIntyy = pi * (0.24e2 * aa * cos(theta) ** 2 * cos(psi) ** 3 * ab * sin(psi) - 0.24e2 * ab * cos(theta) ** 2 * sin(psi) * cos(psi) ** 3 * bb + 0.24e2 * ab * cos(psi) ** 3 * cos(theta) * sin(theta) * bc + 0.12e2 * sin(theta) * ac * cos(theta) * cos(psi) ** 3 * bb + 0.12e2 * sin(theta) * bc * cos(theta) ** 3 * sin(psi) * cc + 0.12e2 * ab * cos(theta) ** 4 * sin(psi) * cos(psi) ** 3 * bb - 0.12e2 * sin(theta) * ac * cos(theta) ** 3 * cos(psi) * cc - 0.12e2 * ab ** 2 * cos(psi) ** 4 - 0.12e2 * aa * cos(theta) ** 4 * cos(psi) ** 3 * ab * sin(psi) + 0.12e2 * aa * cos(theta) ** 3 * cos(psi) ** 3 * sin(theta) * ac + 0.3e1 * bb ** 2 * cos(psi) ** 4 + 0.6e1 * bb * cos(theta) ** 2 * cc + 0.6e1 * bb ** 2 * cos(theta) ** 2 * cos(psi) ** 2 + 0.12e2 * ab ** 2 * cos(theta) ** 4 * cos(psi) ** 2 + 0.6e1 * aa * cos(theta) ** 4 * cos(psi) ** 2 * bb + 0.12e2 * aa * sin(psi) * ab * cos(psi) - 0.6e1 * aa * cos(theta) ** 4 * cos(psi) ** 4 * bb - 0.12e2 * aa * sin(psi) * ab * cos(psi) ** 3 + 0.12e2 * ab ** 2 * cos(psi) ** 2 + 0.3e1 * bb ** 2 * cos(theta) ** 4 + 0.4e1 * ab ** 2 * cos(theta) ** 2 + 0.4e1 * bc ** 2 * cos(psi) ** 2 - 0.12e2 * bc ** 2 * cos(theta) ** 4 + 0.6e1 * aa ** 2 * cos(theta) ** 2 * cos(psi) ** 2 + 0.4e1 * ab * cos(psi) * sin(psi) * cc + 0.8e1 * ac * sin(psi) * bc * cos(psi) + 0.12e2 * aa * cos(theta) ** 2 * cos(psi) ** 4 * bb + 0.12e2 * ab * cos(psi) ** 3 * sin(psi) * bb + 0.2e1 * aa * bb * cos(theta) ** 2 - 0.6e1 * bb ** 2 * cos(theta) ** 2 * cos(psi) ** 4 - 0.6e1 * aa ** 2 * cos(theta) ** 2 * cos(psi) ** 4 - 0.6e1 * bb * cos(theta) ** 4 * cc + 0.12e2 * bc ** 2 * cos(theta) ** 2 - 0.12e2 * aa * cos(theta) * cos(psi) ** 3 * sin(theta) * ac - 0.24e2 * ab * cos(theta) ** 3 * cos(psi) ** 3 * sin(theta) * bc - 0.12e2 * sin(theta) * ac * cos(theta) ** 3 * cos(psi) ** 3 * bb - 0.12e2 * sin(theta) * bc * cos(theta) * sin(psi) * cc - 0.12e2 * ab * cos(theta) ** 4 * sin(psi) * cos(psi) * bb - 0.8e1 * ab * cos(theta) * sin(psi) * sin(theta) * ac - 0.8e1 * sin(theta) * ac * bb * cos(theta) * cos(psi) + 0.12e2 * sin(theta) * ac * cos(theta) * cos(psi) * cc - 0.12e2 * aa * cos(theta) ** 2 * cos(psi) * sin(psi) * ab - 0.4e1 * aa * sin(psi) * sin(theta) * bc * cos(theta) + 0.12e2 * ab * cos(theta) ** 2 * sin(psi) * bb * cos(psi) + 0.3e1 * aa ** 2 + 0.3e1 * cc ** 2 + 0.4e1 * ac ** 2 + 0.2e1 * aa * cc - 0.6e1 * aa ** 2 * cos(psi) ** 2 + 0.3e1 * aa ** 2 * cos(psi) ** 4 - 0.4e1 * ac ** 2 * cos(psi) ** 2 - 0.4e1 * ac ** 2 * cos(theta) ** 2 - 0.6e1 * cc ** 2 * cos(theta) ** 2 + 0.3e1 * cc ** 2 * cos(theta) ** 4 + 0.12e2 * bb * cos(theta) ** 3 * sin(psi) * sin(theta) * bc * cos(psi) ** 2 + 0.3e1 * aa ** 2 * cos(theta) ** 4 * cos(psi) ** 4 + 0.24e2 * ab ** 2 * cos(psi) ** 4 * cos(theta) ** 2 - 0.8e1 * bb * cos(psi) ** 2 * cc * cos(theta) ** 2 - 0.12e2 * aa * bb * cos(theta) ** 2 * cos(psi) ** 2 + 0.8e1 * aa * cc * cos(theta) ** 2 * cos(psi) ** 2 - 0.6e1 * aa * cc * cos(theta) ** 4 * cos(psi) ** 2 + 0.6e1 * bb * cos(theta) ** 4 * cc * cos(psi) ** 2 - 0.24e2 * ab ** 2 * cos(theta) ** 2 * cos(psi) ** 2 + 0.16e2 * ac ** 2 * cos(theta) ** 2 * cos(psi) ** 2 - 0.16e2 * bc ** 2 * cos(psi) ** 2 * cos(theta) ** 2 - 0.6e1 * bb ** 2 * cos(theta) ** 4 * cos(psi) ** 2 + 0.3e1 * bb ** 2 * cos(theta) ** 4 * cos(psi) ** 4 - 0.2e1 * aa * cc * cos(psi) ** 2 - 0.2e1 * aa * cc * cos(theta) ** 2 - 0.12e2 * ac ** 2 * cos(theta) ** 4 * cos(psi) ** 2 + 0.12e2 * bc ** 2 * cos(theta) ** 4 * cos(psi) ** 2 + 0.12e2 * aa * cos(theta) * cos(psi) * sin(theta) * ac + 0.24e2 * ab * cos(theta) ** 3 * cos(psi) * sin(theta) * bc + 0.12e2 * sin(theta) * ac * cos(theta) ** 3 * cos(psi) * bb - 0.16e2 * ab * cos(theta) * sin(theta) * bc * cos(psi) + 0.12e2 * aa * cos(theta) * cos(psi) ** 2 * sin(psi) * sin(theta) * bc + 0.24e2 * ab * cos(psi) ** 2 * cos(theta) * sin(theta) * ac * sin(psi) - 0.12e2 * bb * cos(theta) * sin(psi) * cos(psi) ** 2 * sin(theta) * bc - 0.12e2 * aa * cos(theta) ** 3 * cos(psi) ** 2 * sin(theta) * bc * sin(psi) - 0.24e2 * ab * cos(theta) ** 3 * sin(psi) * cos(psi) ** 2 * sin(theta) * ac - 0.32e2 * ac * sin(psi) * bc * cos(psi) * cos(theta) ** 2 + 0.12e2 * ab * cos(psi) * sin(psi) * cc * cos(theta) ** 4 + 0.24e2 * ac * sin(psi) * bc * cos(psi) * cos(theta) ** 4 - 0.16e2 * ab * cos(psi) * sin(psi) * cc * cos(theta) ** 2 + 0.2e1 * bb * cos(psi) ** 2 * cc - 0.6e1 * aa * bb * cos(psi) ** 4 - 0.12e2 * ab ** 2 * cos(theta) ** 4 * cos(psi) ** 4 + 0.6e1 * aa * bb * cos(psi) ** 2 - 0.12e2 * bb * cos(theta) ** 3 * sin(psi) * sin(theta) * bc) / 0.4e1
	return preIntyy
def yzThetaPsi(theta,psi,aa,bb,cc,ab,ac,bc):
	preIntyz = -pi * (0.8e1 * aa * cos(theta) ** 2 * cos(psi) ** 3 * ab * sin(psi) - 0.8e1 * ab * cos(theta) ** 2 * sin(psi) * cos(psi) ** 3 * bb + 0.8e1 * ab * cos(psi) ** 3 * cos(theta) * sin(theta) * bc + 0.4e1 * sin(theta) * ac * cos(theta) * cos(psi) ** 3 * bb + 0.4e1 * sin(theta) * bc * cos(theta) ** 3 * sin(psi) * cc + 0.4e1 * ab * cos(theta) ** 4 * sin(psi) * cos(psi) ** 3 * bb - 0.4e1 * sin(theta) * ac * cos(theta) ** 3 * cos(psi) * cc - 0.4e1 * ab ** 2 * cos(psi) ** 4 - 0.4e1 * aa * cos(theta) ** 4 * cos(psi) ** 3 * ab * sin(psi) + 0.4e1 * aa * cos(theta) ** 3 * cos(psi) ** 3 * sin(theta) * ac + bb ** 2 * cos(psi) ** 4 + 0.2e1 * bb * cos(theta) ** 2 * cc + 0.3e1 * bb ** 2 * cos(theta) ** 2 * cos(psi) ** 2 + 0.4e1 * ab ** 2 * cos(theta) ** 4 * cos(psi) ** 2 + 0.2e1 * aa * cos(theta) ** 4 * cos(psi) ** 2 * bb + 0.2e1 * aa * sin(psi) * ab * cos(psi) - 0.2e1 * aa * cos(theta) ** 4 * cos(psi) ** 4 * bb - 0.4e1 * aa * sin(psi) * ab * cos(psi) ** 3 + 0.4e1 * ab ** 2 * cos(psi) ** 2 + bb ** 2 * cos(theta) ** 4 + ab ** 2 * cos(theta) ** 2 + bc ** 2 * cos(psi) ** 2 - 0.4e1 * bc ** 2 * cos(theta) ** 4 + aa ** 2 * cos(theta) ** 2 * cos(psi) ** 2 + 0.2e1 * ac * sin(psi) * bc * cos(psi) + 0.4e1 * aa * cos(theta) ** 2 * cos(psi) ** 4 * bb + 0.4e1 * ab * cos(psi) ** 3 * sin(psi) * bb - 0.2e1 * bb ** 2 * cos(theta) ** 2 * cos(psi) ** 4 - 0.2e1 * aa ** 2 * cos(theta) ** 2 * cos(psi) ** 4 - 0.2e1 * bb * cos(theta) ** 4 * cc + 0.4e1 * bc ** 2 * cos(theta) ** 2 - 0.4e1 * aa * cos(theta) * cos(psi) ** 3 * sin(theta) * ac - 0.8e1 * ab * cos(theta) ** 3 * cos(psi) ** 3 * sin(theta) * bc - 0.4e1 * sin(theta) * ac * cos(theta) ** 3 * cos(psi) ** 3 * bb - 0.2e1 * sin(theta) * bc * cos(theta) * sin(psi) * cc - 0.4e1 * ab * cos(theta) ** 4 * sin(psi) * cos(psi) * bb - 0.2e1 * ab * cos(theta) * sin(psi) * sin(theta) * ac - 0.4e1 * sin(theta) * ac * bb * cos(theta) * cos(psi) + 0.2e1 * sin(theta) * ac * cos(theta) * cos(psi) * cc - 0.2e1 * aa * cos(theta) ** 2 * cos(psi) * sin(psi) * ab + 0.6e1 * ab * cos(theta) ** 2 * sin(psi) * bb * cos(psi) - bb ** 2 * cos(theta) ** 2 - bb ** 2 * cos(psi) ** 2 - ab ** 2 - bc ** 2 - aa ** 2 * cos(psi) ** 2 + aa ** 2 * cos(psi) ** 4 - ac ** 2 * cos(psi) ** 2 - ac ** 2 * cos(theta) ** 2 - cc ** 2 * cos(theta) ** 2 + cc ** 2 * cos(theta) ** 4 + 0.4e1 * bb * cos(theta) ** 3 * sin(psi) * sin(theta) * bc * cos(psi) ** 2 + aa ** 2 * cos(theta) ** 4 * cos(psi) ** 4 + 0.8e1 * ab ** 2 * cos(psi) ** 4 * cos(theta) ** 2 - 0.2e1 * bb * cos(psi) ** 2 * cc * cos(theta) ** 2 - 0.4e1 * aa * bb * cos(theta) ** 2 * cos(psi) ** 2 + 0.2e1 * aa * cc * cos(theta) ** 2 * cos(psi) ** 2 - 0.2e1 * aa * cc * cos(theta) ** 4 * cos(psi) ** 2 + 0.2e1 * bb * cos(theta) ** 4 * cc * cos(psi) ** 2 - 0.8e1 * ab ** 2 * cos(theta) ** 2 * cos(psi) ** 2 + 0.5e1 * ac ** 2 * cos(theta) ** 2 * cos(psi) ** 2 - 0.5e1 * bc ** 2 * cos(psi) ** 2 * cos(theta) ** 2 - 0.2e1 * bb ** 2 * cos(theta) ** 4 * cos(psi) ** 2 + bb ** 2 * cos(theta) ** 4 * cos(psi) ** 4 - 0.4e1 * ac ** 2 * cos(theta) ** 4 * cos(psi) ** 2 + 0.4e1 * bc ** 2 * cos(theta) ** 4 * cos(psi) ** 2 + 0.2e1 * aa * cos(theta) * cos(psi) * sin(theta) * ac + 0.8e1 * ab * cos(theta) ** 3 * cos(psi) * sin(theta) * bc + 0.4e1 * sin(theta) * ac * cos(theta) ** 3 * cos(psi) * bb - 0.6e1 * ab * cos(theta) * sin(theta) * bc * cos(psi) + 0.4e1 * aa * cos(theta) * cos(psi) ** 2 * sin(psi) * sin(theta) * bc + 0.8e1 * ab * cos(psi) ** 2 * cos(theta) * sin(theta) * ac * sin(psi) - 0.4e1 * bb * cos(theta) * sin(psi) * cos(psi) ** 2 * sin(theta) * bc - 0.4e1 * aa * cos(theta) ** 3 * cos(psi) ** 2 * sin(theta) * bc * sin(psi) - 0.8e1 * ab * cos(theta) ** 3 * sin(psi) * cos(psi) ** 2 * sin(theta) * ac - 0.10e2 * ac * sin(psi) * bc * cos(psi) * cos(theta) ** 2 + 0.4e1 * ab * cos(psi) * sin(psi) * cc * cos(theta) ** 4 + 0.8e1 * ac * sin(psi) * bc * cos(psi) * cos(theta) ** 4 - 0.4e1 * ab * cos(psi) * sin(psi) * cc * cos(theta) ** 2 - 0.2e1 * aa * bb * cos(psi) ** 4 - 0.4e1 * ab ** 2 * cos(theta) ** 4 * cos(psi) ** 4 + 0.2e1 * aa * bb * cos(psi) ** 2 + 0.2e1 * sin(theta) * sin(psi) * bb * cos(theta) * bc - 0.4e1 * bb * cos(theta) ** 3 * sin(psi) * sin(theta) * bc - 0.2e1 * sin(psi) * ab * bb * cos(psi))
	return preIntyz
def zzThetaPsi(theta,psi,aa,bb,cc,ab,ac,bc):
	preIntzz = 0.2e1 * pi * (sin(theta) ** 2 * cos(psi) ** 2 * aa - 0.2e1 * sin(theta) ** 2 * cos(psi) * sin(psi) * ab - 0.2e1 * sin(theta) * cos(psi) * cos(theta) * ac + sin(theta) ** 2 * sin(psi) ** 2 * bb + 0.2e1 * sin(theta) * sin(psi) * cos(theta) * bc + cos(theta) ** 2 * cc) ** 2
	return preIntzz
'''
For theta only 
xx = yy
xz = yz

'''	
def xxTheta(theta,aa,bb,cc,ab,ac,bc): #This method takes Theta as input.This means no angle preference in Phi and Psi
	alphaxxSquare = pi ** 2 * (0.9e1 * aa ** 2 * cos(theta) ** 4 + 0.16e2 * bb * cos(theta) ** 2 * cc + 0.9e1 * bb ** 2 * cos(theta) ** 4 + 0.8e1 * ab ** 2 * cos(theta) ** 2 - 0.48e2 * bc ** 2 * cos(theta) ** 4 + 0.6e1 * aa * cos(theta) ** 4 * bb + 0.4e1 * aa * bb * cos(theta) ** 2 - 0.24e2 * bb * cos(theta) ** 4 * cc + 0.32e2 * bc ** 2 * cos(theta) ** 2 + 0.6e1 * aa ** 2 * cos(theta) ** 2 + 0.6e1 * bb ** 2 * cos(theta) ** 2 + 0.12e2 * ab ** 2 * cos(theta) ** 4 + 0.9e1 * aa ** 2 + 0.9e1 * bb ** 2 + 0.24e2 * cc ** 2 + 0.12e2 * ab ** 2 + (16 * ac ** 2) + 0.16e2 * bc ** 2 + 0.6e1 * aa * bb + 0.8e1 * aa * cc + 0.32e2 * (ac ** 2) * cos(theta) ** 2 - 0.48e2 * cc ** 2 * cos(theta) ** 2 + 0.24e2 * cc ** 2 * cos(theta) ** 4 + 0.16e2 * aa * cc * cos(theta) ** 2 + 0.8e1 * bb * cc - 0.24e2 * aa * cc * cos(theta) ** 4 - 0.48e2 * (ac ** 2) * cos(theta) ** 4) / 0.16e2
        return alphaxxSquare

def xyTheta(theta,aa,bb,cc,ab,ac,bc): #This method takes Theta as input.This means no angle preference in Phi and Psi
	alphaxySquare = pi ** 2 * (0.3e1 * aa ** 2 * cos(theta) ** 4 + 0.16e2 * bb * cos(theta) ** 2 * cc + 0.3e1 * bb ** 2 * cos(theta) ** 4 + 0.24e2 * ab ** 2 * cos(theta) ** 2 - 0.16e2 * bc ** 2 * cos(theta) ** 4 + 0.2e1 * aa * cos(theta) ** 4 * bb - 0.20e2 * aa * bb * cos(theta) ** 2 - 0.8e1 * bb * cos(theta) ** 4 * cc + 0.2e1 * aa ** 2 * cos(theta) ** 2 + 0.2e1 * bb ** 2 * cos(theta) ** 2 + 0.4e1 * ab ** 2 * cos(theta) ** 4 + 0.3e1 * aa ** 2 + 0.3e1 * bb ** 2 + 0.8e1 * cc ** 2 + 0.4e1 * ab ** 2 + (16 * ac ** 2) + 0.16e2 * bc ** 2 + 0.2e1 * aa * bb - 0.8e1 * aa * cc - 0.16e2 * cc ** 2 * cos(theta) ** 2 + 0.8e1 * cc ** 2 * cos(theta) ** 4 + 0.16e2 * aa * cc * cos(theta) ** 2 - 0.8e1 * bb * cc - 0.8e1 * aa * cc * cos(theta) ** 4 - 0.16e2 * (ac ** 2) * cos(theta) ** 4) / 0.16e2
        return alphaxySquare
def xzTheta(theta,aa,bb,cc,ab,ac,bc): #This method takes Theta as input.This means no angle preference in Phi and Psi
	alphaxzSquare = -pi ** 2 * (-(4 * bc ** 2) - (4 * ac ** 2) - bb ** 2 - aa ** 2 - (4 * ab ** 2) + 0.12e2 * (bc ** 2) * cos(theta) ** 2 + 0.3e1 * bb ** 2 * cos(theta) ** 4 + 0.12e2 * (ac ** 2) * cos(theta) ** 2 - 0.2e1 * bb ** 2 * cos(theta) ** 2 + 0.4e1 * (ab ** 2) * cos(theta) ** 4 + 0.8e1 * cc ** 2 * cos(theta) ** 4 + 0.3e1 * aa ** 2 * cos(theta) ** 4 - 0.2e1 * aa ** 2 * cos(theta) ** 2 + 0.2e1 * aa * bb - 0.16e2 * (ac ** 2) * cos(theta) ** 4 - 0.16e2 * (bc ** 2) * cos(theta) ** 4 - 0.8e1 * cc ** 2 * cos(theta) ** 2 - 0.4e1 * aa * bb * cos(theta) ** 2 + 0.8e1 * bb * cos(theta) ** 2 * cc + 0.8e1 * aa * cc * cos(theta) ** 2 + 0.2e1 * aa * cos(theta) ** 4 * bb - 0.8e1 * aa * cc * cos(theta) ** 4 - 0.8e1 * bb * cos(theta) ** 4 * cc) / 0.4e1
        return alphaxzSquare
def yyTheta(theta,aa,bb,cc,ab,ac,bc): #This method takes Theta as input.This means no angle preference in Phi and Psi
	alphayySquare = pi ** 2 * (0.9e1 * aa ** 2 * cos(theta) ** 4 + 0.16e2 * bb * cos(theta) ** 2 * cc + 0.9e1 * bb ** 2 * cos(theta) ** 4 + 0.8e1 * ab ** 2 * cos(theta) ** 2 - 0.48e2 * bc ** 2 * cos(theta) ** 4 + 0.6e1 * aa * cos(theta) ** 4 * bb + 0.4e1 * aa * bb * cos(theta) ** 2 - 0.24e2 * bb * cos(theta) ** 4 * cc + 0.32e2 * bc ** 2 * cos(theta) ** 2 + 0.6e1 * aa ** 2 * cos(theta) ** 2 + 0.6e1 * bb ** 2 * cos(theta) ** 2 + 0.12e2 * ab ** 2 * cos(theta) ** 4 + 0.9e1 * aa ** 2 + 0.9e1 * bb ** 2 + 0.24e2 * cc ** 2 + 0.12e2 * ab ** 2 + (16 * ac ** 2) + 0.16e2 * bc ** 2 + 0.6e1 * aa * bb + 0.8e1 * aa * cc + 0.32e2 * (ac ** 2) * cos(theta) ** 2 - 0.48e2 * cc ** 2 * cos(theta) ** 2 + 0.24e2 * cc ** 2 * cos(theta) ** 4 + 0.16e2 * aa * cc * cos(theta) ** 2 + 0.8e1 * bb * cc - 0.24e2 * aa * cc * cos(theta) ** 4 - 0.48e2 * (ac ** 2) * cos(theta) ** 4) / 0.16e2
        return alphayySquare
def yzTheta(theta,aa,bb,cc,ab,ac,bc): #This method takes Theta as input.This means no angle preference in Phi and Psi
	alphayzSquare = -pi ** 2 * (-(4 * bc ** 2) - (4 * ac ** 2) - bb ** 2 - aa ** 2 - (4 * ab ** 2) + 0.12e2 * (bc ** 2) * cos(theta) ** 2 + 0.3e1 * bb ** 2 * cos(theta) ** 4 + 0.12e2 * (ac ** 2) * cos(theta) ** 2 - 0.2e1 * bb ** 2 * cos(theta) ** 2 + 0.4e1 * (ab ** 2) * cos(theta) ** 4 + 0.8e1 * cc ** 2 * cos(theta) ** 4 + 0.3e1 * aa ** 2 * cos(theta) ** 4 - 0.2e1 * aa ** 2 * cos(theta) ** 2 + 0.2e1 * aa * bb - 0.16e2 * (ac ** 2) * cos(theta) ** 4 - 0.16e2 * (bc ** 2) * cos(theta) ** 4 - 0.8e1 * cc ** 2 * cos(theta) ** 2 - 0.4e1 * aa * bb * cos(theta) ** 2 + 0.8e1 * bb * cos(theta) ** 2 * cc + 0.8e1 * aa * cc * cos(theta) ** 2 + 0.2e1 * aa * cos(theta) ** 4 * bb - 0.8e1 * aa * cc * cos(theta) ** 4 - 0.8e1 * bb * cos(theta) ** 4 * cc) / 0.4e1
        return alphayzSquare
def zzTheta(theta,aa,bb,cc,ab,ac,bc): #This method takes Theta as input.This means no angle preference in Phi and Psi
	alphazzSquare = pi ** 2 * ((3 * bb ** 2) + (3 * aa ** 2) + (4 * ab ** 2) - 0.8e1 * (ab ** 2) * cos(theta) ** 2 + 0.16e2 * bc ** 2 * cos(theta) ** 2 + 0.3e1 * (bb ** 2) * cos(theta) ** 4 + 0.16e2 * ac ** 2 * cos(theta) ** 2 - 0.6e1 * (bb ** 2) * cos(theta) ** 2 + 0.4e1 * (ab ** 2) * cos(theta) ** 4 + 0.8e1 * cc ** 2 * cos(theta) ** 4 + 0.3e1 * (aa ** 2) * cos(theta) ** 4 - 0.6e1 * (aa ** 2) * cos(theta) ** 2 + (2 * aa * bb) - 0.16e2 * ac ** 2 * cos(theta) ** 4 - 0.16e2 * bc ** 2 * cos(theta) ** 4 - 0.4e1 * aa * bb * cos(theta) ** 2 + 0.8e1 * bb * cos(theta) ** 2 * cc + 0.8e1 * aa * cc * cos(theta) ** 2 + 0.2e1 * aa * cos(theta) ** 4 * bb - 0.8e1 * aa * cc * cos(theta) ** 4 - 0.8e1 * bb * cos(theta) ** 4 * cc) / 0.2e1
        return alphazzSquare

def xThetaPsi(theta,psi,a,b,c):
	mxThetaPsiSquare = pi * (0.2e1 * a * cos(theta) * cos(psi) * sin(theta) * c - b ** 2 * cos(theta) ** 2 * cos(psi) ** 2 + c ** 2 - c ** 2 * cos(theta) ** 2 + a ** 2 * cos(theta) ** 2 * cos(psi) ** 2 - a ** 2 * cos(psi) ** 2 + b ** 2 * cos(psi) ** 2 - 0.2e1 * a * cos(theta) ** 2 * cos(psi) * b * sin(psi) + b ** 2 * cos(theta) ** 2 + 0.2e1 * a * sin(psi) * b * cos(psi) + a ** 2 - 0.2e1 * b * cos(theta) * sin(psi) * sin(theta) * c)
        return mxThetaPsiSquare
def yThetaPsi(theta,psi,a,b,c):
	myThetaPsiSquare = pi * (0.2e1 * a * cos(theta) * cos(psi) * sin(theta) * c - b ** 2 * cos(theta) ** 2 * cos(psi) ** 2 + c ** 2 - c ** 2 * cos(theta) ** 2 + a ** 2 * cos(theta) ** 2 * cos(psi) ** 2 - a ** 2 * cos(psi) ** 2 + b ** 2 * cos(psi) ** 2 - 0.2e1 * a * cos(theta) ** 2 * cos(psi) * b * sin(psi) + b ** 2 * cos(theta) ** 2 + 0.2e1 * a * sin(psi) * b * cos(psi) + a ** 2 - 0.2e1 * b * cos(theta) * sin(psi) * sin(theta) * c)
        return myThetaPsiSquare
def zThetaPsi(theta,psi,a,b,c):
        mzThetaPsiSquare = 0.2e1 * (-sin(theta) * cos(psi) * a + sin(theta) * sin(psi) * b + cos(theta) * c) ** 2 * pi
        return mzThetaPsiSquare
def xTheta(theta,a,b,c):
        mxThetaSquare = pi ** 2 * (-0.2e1 * c ** 2 * cos(theta) ** 2 + 0.2e1 * c ** 2 + b ** 2 * cos(theta) ** 2 + b ** 2 + a ** 2 * cos(theta) ** 2 + a ** 2)
        return mxThetaSquare
def yTheta(theta,a,b,c):
        myThetaSquare = pi ** 2 * (-0.2e1 * c ** 2 * cos(theta) ** 2 + 0.2e1 * c ** 2 + b ** 2 * cos(theta) ** 2 + b ** 2 + a ** 2 * cos(theta) ** 2 + a ** 2)
        return myThetaSquare
def zTheta(theta,a,b,c):
        mzThetaSquare = -0.2e1 * pi ** 2 * (-a ** 2 + a ** 2 * cos(theta) ** 2 - b ** 2 + b ** 2 * cos(theta) ** 2 - 0.2e1 * c ** 2 * cos(theta) ** 2)
        return mzThetaSquare



