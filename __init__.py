#!/usr/bin/env python
# This file is part of the party_birthday module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
pass
from trytond.pool import Pool
from .party import *


def register():
    Pool.register(
        Party,
        module='party_birthday', type_='model')
