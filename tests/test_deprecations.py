"""
Test deprecations. For each deprecation two things must be tested:
1. Is a proper warning raised. This is done using
   with pytest.warns(PyfarDeprecationWarning, match="some text"):
       call_of_function()
2. Was the function properly deprecated. This is done using:
   if version.parse(pf.__version__) >= version.parse('0.5.0'):
        with pytest.raises(AttributeError):
            # remove get_nearest_k() from pyfar 0.5.0!
            coords.get_nearest_k(1, 0, 0)

"""
import numpy as np
from packaging import version
import pathlib
import re

import pytest
from unittest.mock import patch

import pyfar as pf
import pyfar.dsp.filter as pfilt
from pyfar.classes.warnings import PyfarDeprecationWarning

# This defines the plot size and the backend
from pyfar.testing.plot_utils import create_figure


# deprecate in 0.5.0 ----------------------------------------------------------
def test_get_nearest_deprecations():
    """Coordinates get_nearest* methods"""
    coords = pf.Coordinates(np.arange(6), 0, 0)

    if version.parse(pf.__version__) >= version.parse('0.5.0'):
        with pytest.raises(AttributeError):
            # remove get_nearest_k() from pyfar 0.5.0!
            coords.get_nearest_k(1, 0, 0)

    if version.parse(pf.__version__) >= version.parse('0.5.0'):
        with pytest.raises(AttributeError):
            # remove get_nearest_k() from pyfar 0.5.0!
            coords.get_nearest_cart(2.5, 0, 0, 1.5)

    if version.parse(pf.__version__) >= version.parse('0.5.0'):
        with pytest.raises(AttributeError):
            # remove get_nearest_k() from pyfar 0.5.0!
            coords.get_nearest_sph(0, 0, 1, 1)

    if version.parse(pf.__version__) >= version.parse('0.5.0'):
        with pytest.raises(AttributeError):
            # remove get_slice() from pyfar 0.5.0!
            coords.get_slice('x', 'met', 0, 1)


def test_filter_deprecations():
    """Deprecate filter functions with non-verbose names"""

    # butter
    if version.parse(pf.__version__) >= version.parse('0.5.0'):
        with pytest.raises(AttributeError):
            # remove butter() from pyfar 0.5.0!
            pfilt.butter(None, 2, 1000, 'lowpass', 44100)

    # cheby1
    if version.parse(pf.__version__) >= version.parse('0.5.0'):
        with pytest.raises(AttributeError):
            # remove cheby1() from pyfar 0.5.0!
            pfilt.cheby1(None, 2, 1, 1000, 'lowpass', 44100)

    # cheby2
    if version.parse(pf.__version__) >= version.parse('0.5.0'):
        with pytest.raises(AttributeError):
            # remove cheby2() from pyfar 0.5.0!
            pfilt.cheby2(None, 2, 40, 1000, 'lowpass', 44100)

    # elipp
    if version.parse(pf.__version__) >= version.parse('0.5.0'):
        with pytest.raises(AttributeError):
            # remove ellip() from pyfar 0.5.0!
            pfilt.ellip(None, 2, 1, 40, 1000, 'lowpass', 44100)

    # bell
    if version.parse(pf.__version__) >= version.parse('0.5.0'):
        with pytest.raises(AttributeError):
            # remove peq() from pyfar 0.5.0!
            pfilt.peq(None, 1000, 10, 2, sampling_rate=44100)


@patch('soundfile.read', return_value=(np.array([1., 2., 3.]), 1000))
def test_read_wav_deprecation(tmpdir):
    """Deprecate pf.io.read_wav"""
    filename = 'test.wav'
    if version.parse(pf.__version__) >= version.parse('0.5.0'):
        with pytest.raises(AttributeError):
            # remove read_wav from pyfar 0.5.0!
            pf.io.read_wav(filename)


@patch('soundfile.write')
def test_write_wav_deprecation(write_mock, noise, tmpdir):
    """Deprecate pf.io.write_wav"""
    filename = pathlib.Path(tmpdir, 'test_wav')
    if version.parse(pf.__version__) >= version.parse('0.5.0'):
        with pytest.raises(AttributeError):
            # remove write_wav from pyfar 0.5.0!
            pf.io.write_wav(noise, filename)


def test_linear_sweep_deprecation():
    """Deprecate pf.signals.linear_sweep"""
    if version.parse(pf.__version__) >= version.parse('0.5.0'):
        with pytest.raises(AttributeError):
            # remove linear_sweep() from pyfar 0.5.0!
            pf.signals.linear_sweep(2**10, [1e3, 20e3])


def test_exponential_sweep_deprecation():
    """Deprecate pf.signals.exponential_sweep"""
    if version.parse(pf.__version__) >= version.parse('0.5.0'):
        with pytest.raises(AttributeError):
            # remove exponential_sweep() from pyfar 0.5.0!
            pf.signals.exponential_sweep(2**10, [1e3, 20e3])


# deprecate in 0.6.0 ----------------------------------------------------------
@pytest.mark.parametrize('function', [
    (pf.plot.freq), (pf.plot.phase), (pf.plot.group_delay),
    (pf.plot.time_freq), (pf.plot.freq_phase), (pf.plot.freq_group_delay)])
def test_xscale_deprecation(function, handsome_signal):
    """Deprecate xscale parameter in plot functions"""

    with pytest.warns(PyfarDeprecationWarning,
                      match="The xscale parameter will be removed"):
        create_figure()
        function(handsome_signal, xscale='linear')

    if version.parse(pf.__version__) >= version.parse('0.6.0'):
        with pytest.raises(AttributeError):
            # remove xscale from pyfar 0.6.0!
            create_figure()
            function(handsome_signal)


def test_spectrogram_yscale_deprecation(sine):
    """Deprecate yscale parameter in plot functions"""

    with pytest.warns(PyfarDeprecationWarning,
                      match="The yscale parameter will be removed"):
        create_figure()
        pf.plot.spectrogram(sine, yscale='linear')

    if version.parse(pf.__version__) >= version.parse('0.6.0'):
        with pytest.raises(AttributeError):
            # remove xscale from pyfar 0.6.0!
            create_figure()
            pf.plot.spectrogram(sine)


def test__check_time_unit():
    """Deprecate unit=None in plots showing the time or group delay"""

    with pytest.warns(PyfarDeprecationWarning,
                      match="unit=None will be deprecated"):
        create_figure()
        pf.plot._utils._check_time_unit(None)

    if version.parse(pf.__version__) >= version.parse('0.6.0'):
        with pytest.raises(ValueError):
            # remove xscale from pyfar 0.6.0!
            create_figure()
            pf.plot._utils._check_time_unit(None)


# deprecate in 0.8.0 ----------------------------------------------------------
def test_pad_zero_modi():
    with pytest.warns(PyfarDeprecationWarning,
                      match='Mode "before" and "after" will be renamed into'):
        pf.dsp.pad_zeros(pf.Signal([1], 44100), 5, 'before')

    if version.parse(pf.__version__) >= version.parse('0.8.0'):
        with pytest.raises(ValueError):
            # remove mode 'before' and 'after' from pyfar 0.8.0!
            pf.dsp.pad_zeros(pf.Signal([1], 44100), 5, mode='before')


# deprecate in 0.8.0 ----------------------------------------------------------
@pytest.mark.parametrize(
    'statement', [
        ('coords.get_cart()'),
        ('coords.sh_order'),
        ('coords.set_cart(1,1,1)'),
        ('coords.get_cyl()'),
        ('coords.set_cyl(1,1,1)'),
        ('coords.get_sph()'),
        ('coords.set_sph(1,1,1)'),
        ('coords.systems()'),
        ('pf.Coordinates(0, 0, 0, sh_order=1)'),
        ("pf.Coordinates(0, 0, 0, domain='sph')"),
        ("pf.Coordinates(0, 0, 0, domain='sph', unit='deg')"),
        ("pf.Coordinates(0, 0, 0, domain='sph', convention='top_colat')"),
    ])
def test_deprecations_0_8_0(statement):
    coords = pf.Coordinates.from_spherical_colatitude(np.arange(6), 0, 0)
    coords.y = 1

    # PyfarDeprecationWarning for
    with pytest.warns(PyfarDeprecationWarning,
                      match="This function will be"):
        eval(statement)

    # PyfarDeprecationWarning check version
    with pytest.warns(PyfarDeprecationWarning,
                      match="0.8.0"):
        eval(statement)

    # remove statement from pyfar 0.8.0!
    if version.parse(pf.__version__) >= version.parse('0.8.0'):
        with pytest.raises(AttributeError):
            eval(statement)


def test_deprecations_0_8_0_set_sh_order():
    coords = pf.Coordinates(np.arange(6), 0, 0)
    # sh_order setter
    with pytest.warns(PyfarDeprecationWarning,
                      match="This function will be deprecated"):
        coords.sh_order = 1

    # sh_order setter
    with pytest.warns(PyfarDeprecationWarning,
                      match="0.8.0"):
        coords.sh_order = 1

    # remove statement from pyfar 0.8.0!
    if version.parse(pf.__version__) >= version.parse('0.8.0'):
        with pytest.raises(AttributeError):
            coords.sh_order = 1


def test_signal_len():
    with pytest.warns(PyfarDeprecationWarning,
                      match=re.escape("len(Signal) will be deprecated")):
        len(pf.Signal([1, 2, 3], 44100))

    if version.parse(pf.__version__) >= version.parse('0.8.0'):
        with pytest.raises(TypeError, match=re.escape("had no len()")):
            # remove Signal.__len__ from pyfar 0.8.0!
            len(pf.Signal([1, 2, 3], 44100))


def test_deprecations_find_nearest_k():
    coords = pf.Coordinates(np.arange(6), 0, 0)

    with pytest.warns(
            PyfarDeprecationWarning,
            match="This function will be deprecated in pyfar 0.8.0 in favor"):
        coords.find_nearest_k(1, 0, 0)


def test_deprecations_find_slice():
    coords = pf.samplings.sph_lebedev(sh_order=10)

    with pytest.warns(
            PyfarDeprecationWarning,
            match="This function will be deprecated in pyfar 0.8.0. Use "):
        coords.find_slice('elevation', 'deg', 0, 5)
