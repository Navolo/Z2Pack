#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

import pytest
import z2pack
import tbmodels

@pytest.fixture
def tb_model():
    t1, t2 = (0.2, 0.3)

    model = tbmodels.Model(
        on_site=(1, 1, -1, -1),
        pos=[
            [0., 0., 0.],
            [0., 0., 0.],
            [0.5, 0.5, 0.],
            [0.5, 0.5, 0.]
        ],
        occ=2
    )

    for p, R in zip([1, 1j, -1j, -1], itertools.product([0, -1], [0, -1], [0])):
        model.add_hop(overlap=p * t1, orbital_1=0, orbital_2=2, R=R)
        model.add_hop(overlap=p.conjugate() * t1, orbital_1=1, orbital_2=3, R=R)

    for R in ((r[0], r[1], 0) for r in itertools.permutations([0, 1])):
        model.add_hop(t2, 0, 0, R)
        model.add_hop(t2, 1, 1, R)
        model.add_hop(-t2, 2, 2, R)
        model.add_hop(-t2, 3, 3, R)
    return model

@pytest.fixture
def tb_system(tb_model):
    return z2pack.tb.System(tb_model)

@pytest.fixture
def tb_surface():
    return lambda s, t: [s, t, 0]

@pytest.fixture
def tb_line():
    return lambda t: [0.3, t, 0]
