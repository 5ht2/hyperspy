# Copyright 2007-2016 The HyperSpy developers
#
# This file is part of  HyperSpy.
#
#  HyperSpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
#  HyperSpy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with  HyperSpy.  If not, see <http://www.gnu.org/licenses/>.

import sys

import numpy as np

import nose
import nose.tools as nt

import hyperspy.api as hs


# def test_reconstruct_phase():
#     nt.assert_true(True)
# TODO: Vadim, this is where your tests belong!


if __name__ == '__main__':
    nose.run(argv=[sys.argv[0], sys.modules[__name__].__file__, '-v'])
