# coding: utf-8

from __future__ import unicode_literals, division, print_function

"""
Script process the GW output generated by GWsetup using VASP or ABINIT.
"""

__author__ = "Michiel van Setten"
__copyright__ = " "
__version__ = "0.9"
__maintainer__ = "Michiel van Setten"
__email__ = "mjvansetten@gmail.com"
__date__ = "May 2014"

import os
import os.path

from pymatgen.io.gwwrapper.datastructures import get_spec

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    if os.path.isfile('plots'):
        os.remove('plots')
    spec = get_spec('GW')
    spec.read_from_file('spec.in')
    print('Found setup for ', spec.get_code())
    spec.loop_structures('o')
