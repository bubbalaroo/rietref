#! /usr/bin/env python
# rietveld.py

""" This module contains the functions to minimize the residual function
using the rietveld method 
"""

def residual ( W_i, I_exp, I_calc ):
	""" Residual function

	Args:
		W_i:
		I_exp  (float): 
		I_calc (float):

	Returns:
		WSS (float):


	"""
	return WSS;

def background ( N_b, a_n, twoTheta ):
	""" Background

	Args:
		N_b   	 (int): polynomial degree
		a_n   	 (int): polynomial coefficients
		twoTheta (int): degrees 2 theta

	Returns:
		bkg (int): background

	"""

	for i in range(N_b)


def scaleFactor ( S_f, f_j, V_j ):
	""" Scale Factor

	Page 13 In Presentation

	Args:
		S_f (float): beam intensity (depends on measurement)
		f_j (float): phase volume fraction
		V_j (float): phase cell volume (occsionally F factor)
	
	Returns:
		S_j (float): phase scale factor (overall Rietveld generic scale factor)


	"""
	return S_j;

