# -*- coding: utf-8 -*-
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
import numpy.testing as nt

import nose

import hyperspy.api as hs


real_ref = np.arange(9).reshape((3, 3))
imag_ref = np.arange(9).reshape((3, 3)) + 9
comp_ref = real_ref + 1j * imag_ref
phase_ref = np.angle(comp_ref)
amplitude_ref = np.abs(comp_ref)


class TestProperties:

    def setUp(self):
        test = np.arange(9).reshape((3, 3)) + 1j * (9 + np.arange(9).reshape((3, 3)))
        self.s = hs.signals.WaveImage(test)

    def test_get_real(self):
        nt.assert_almost_equal(self.s.real, real_ref)

    def test_set_real(self):
        test = np.random.random((3, 3))
        self.s.real = test
        nt.assert_almost_equal(self.s.real, test)

    def test_get_imag(self):
        nt.assert_almost_equal(self.s.imag, imag_ref)

    def test_set_imag(self):
        test = np.random.random((3, 3))
        self.s.imag = test
        nt.assert_almost_equal(self.s.imag, test)

    def test_get_phase(self):
        nt.assert_almost_equal(self.s.phase, phase_ref)

    def test_set_phase(self):
        test = np.random.random((3, 3))
        self.s.phase = test
        nt.assert_almost_equal(self.s.phase, test)

    def test_get_amplitude(self):
        nt.assert_almost_equal(self.s.amplitude, amplitude_ref)

    def test_set_amplitude(self):
        test = np.random.random((3, 3))
        self.s.amplitude = test
        nt.assert_almost_equal(self.s.amplitude, test)

    def test_get_unwrapped_phase(self):
        phase_ref = np.arange(9).reshape((3, 3))
        self.s.phase = phase_ref
        phase = self.s.get_unwrapped_phase()
        assert isinstance(phase, hs.signals.Image)
        nt.assert_almost_equal(phase.data, phase_ref)

    def test_normalize(self):
        normalization = np.mean(comp_ref)
        self.s.normalize(self.s.data)
        nt.assert_almost_equal(self.s.amplitude, amplitude_ref / np.abs(normalization))
        nt.assert_almost_equal(self.s.phase, phase_ref - np.angle(normalization))

    def test_subtract_reference(self):
        self.s.subtract_reference(self.s)
        nt.assert_almost_equal(self.s.amplitude, 1)
        nt.assert_almost_equal(self.s.phase, 0)

    def test_add_phase_ramp(self):
        self.s.phase = np.indices((3,3)).sum(axis=0) + 4
        self.s.add_phase_ramp(-1, -1, -4)
        nt.assert_almost_equal(self.s.phase, 0)


# TODO: After image stacks can be handled, test for them here!


if __name__ == '__main__':
    nose.run(argv=[sys.argv[0], sys.modules[__name__].__file__, '-v'])
