#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@ethz.ch>
# Date:    27.09.2014 15:39:41 CEST
# File:    BiSe_plot.py

import sys
sys.path.append("../../../")
import z2pack
import matplotlib.pyplot as plt

import os

"""
Bismuth Selenide example
"""

if not os.path.exists('./results'):
    os.makedirs('./results')


# creating the z2pack.abinit object
BiSe = z2pack.fp.System(["BiSe_nscf.files", "BiSe_nscf.in", "wannier90.win" ],
                        z2pack.fp.kpts.abinit,
                        "BiSe_nscf.in",
                        "build",
                        "mpirun -np 7 abinit < BiSe_nscf.files >& log")


# creating the z2pack.plane object
plane_0 = BiSe.plane(2, 0, 0, pickle_file = './results/res_0.txt')
plane_1 = BiSe.plane(2, 0, 0.5, pickle_file = './results/res_1.txt')


plane_0.load()
plane_1.load()
fig, ax = plt.subplots(2, sharex=True, figsize = (9,5))
plane_0.plot(show = False, axis=ax[0], shift=0.5)
plane_1.plot(show = False, axis=ax[1], shift=0.5)
plt.savefig('./results/BiSe.pdf', bbox_inches = 'tight')

print('Z2 topological invariant: {0}'.format(plane_0.invariant()))
print('Z2 topological invariant: {0}'.format(plane_1.invariant()))

