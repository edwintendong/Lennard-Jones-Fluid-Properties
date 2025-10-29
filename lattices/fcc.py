import numpy as np

"""
This module creates an input configuration of monoatomic fcc atoms for LJ Liquid
in XYZ file format, readable by vmd
"""

def creat_fcc_box(u,v,w):
	L = []
	for i in range(u):
		for j in range(v):
			for k in range(w):
				a = (1*i,1*j,1*k)
				b = (a[0]+0.5,a[1]+0.5,a[2])
				c = (a[0]+0.5,a[1],a[2]+0.5)
				d = (a[0],a[1]+0.5,a[2]+0.5)
				L.append(a)
				L.append(b)
				L.append(c)
				L.append(d)
	return(L)

def write_xyz(L):
	f1 = open("lj_fluid.xyz","w")
	print(len(L),file = f1)
	print("LJ", file=f1)
	for i in range(len(L)):
		print("%3s%8.3f%8.3f%8.3f"%("Ar",L[i][0],L[i][1],L[i][2]), file = f1)
	f1.close()


L = creat_fcc_box(5,5,5)
write_xyz(L)
