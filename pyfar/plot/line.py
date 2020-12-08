import matplotlib.pyplot as plt
import matplotlib as mpl
from pyfar.plot.utils import plotstyle
from .. import Signal
from . import _line
from ._interaction import Interaction


def time(signal, ax=None, style='light', **kwargs):
    """Plot the time data of a signal.

    Parameters
    ----------
    signal : Signal
        pyfar Signal object.
    ax : matplotlib.pyplot.axes object
        Axes to plot on. The default is None, which uses the current figure
        ore creates a new one if no figure exists.
    style : str
        'light' or 'dark' to use the pyfar plot styles or stlye from
        matplotlib.pyplot.available. the default is 'light'
    **kwargs
        Keyword arguments that are piped to matplotlib.pyplot.plot

    Returns
    -------
    ax : matplotlib.pyplot.axes object
        Axes or array of axes containing the plot.

    See Also
    --------
    matplotlib.pyplot.plot() for possible **kwargs.
    """
    if not isinstance(signal, Signal):
        raise TypeError('Input data has to be of type: Signal.')

    with plt.style.context(plotstyle(style)):
        ax = _line._time(signal, ax, **kwargs)

    plt.tight_layout()
    Interaction('LineXLin', ax, signal, style, **kwargs)

    return ax


def time_dB(signal, log_prefix=20, log_reference=1, ax=None, style='light',
            **kwargs):
    """Plot the time logairhmic data of a signal.

    Plots `prefix * log10(signal.time / log_reference)`.

    Parameters
    ----------
    signal : Signal
        pyfar Signal object.
    log_prefix : integer, float
        Prefix for calculating the logarithmic time data. The default is 20.
    log_reference : integer
        Reference for calculating the logarithmic time data. The default is 1.
    ax : matplotlib.pyplot.axes object
        Axes to plot on. The default is None, which uses the current figure
        ore creates a new one if no figure exists.
    style : str
        'light' or 'dark' to use the pyfar plot styles or stlye from
        matplotlib.pyplot.available. the default is 'light'
    **kwargs
        Keyword arguments that are piped to matplotlib.pyplot.plot

    Returns
    -------
    ax : matplotlib.pyplot.axes object
        Axes or array of axes containing the plot.

    See Also
    --------
    matplotlib.pyplot.plot() for possible **kwargs.
    """

    if not isinstance(signal, Signal):
        raise TypeError('Input data has to be of type: Signal.')

    with plt.style.context(plotstyle(style)):
        ax = _line._time_dB(signal, log_prefix, log_reference, ax, **kwargs)

    plt.tight_layout()
    Interaction('LineXLin', ax, signal, style, **kwargs)

    return ax


def freq(signal, log_prefix=20, log_reference=1, ax=None, style='light',
         **kwargs):
    """
    Plot the logarithmic absolute spectrum on the positive frequency axis.

    Plots `prefix * log10(signal.freq / log_reference)`.

    Parameters
    ----------
    signal : Signal
        pyfar Signal object.
    log_prefix : integer, float
        Prefix for calculating the logarithmic time data. The default is 20.
    log_reference : integer
        Reference for calculating the logarithmic time data. The default is 1.
    ax : matplotlib.pyplot.axes object
        Axes to plot on. The default is None, which uses the current figure
        ore creates a new one if no figure exists.
    style : str
        'light' or 'dark' to use the pyfar plot styles or stlye from
        matplotlib.pyplot.available. the default is 'light'
    **kwargs
        Keyword arguments that are piped to matplotlib.pyplot.plot

    Returns
    -------
    ax : matplotlib.pyplot.axes object
        Axes or array of axes containing the plot.

    See Also
    --------
    matplotlib.pyplot.plot() for possible **kwargs.
    """

    if not isinstance(signal, Signal):
        raise TypeError('Input data has to be of type: Signal.')

    with plt.style.context(plotstyle(style)):
        ax = _line._freq(signal, log_prefix, log_reference, ax, **kwargs)

    plt.tight_layout()
    Interaction('LineXLog', ax, signal, style, **kwargs)

    return ax


def phase(signal, deg=False, unwrap=False, ax=None, style='light', **kwargs):
    """Plot the phase of the spectrum on the positive frequency axis.

    Parameters
    ----------
    signal : Signal
        pyfar Signal object.
    deg : Boolean
        Flag to plot the phase in degrees. The default is False.
    unwrap : Boolean, str
        True to unwrap the phase or "360" to unwrap the phase to 2 pi. The
        default is False.
    ax : matplotlib.pyplot.axes object
        Axes to plot on. If not given, the current figure will be used.
    style : str
        'light' or 'dark' to use the pyfar plot styles or stlye from
        matplotlib.pyplot.available. the default is 'light'
    **kwargs
        Keyword arguments that are piped to matplotlib.pyplot.plot

    Returns
    -------
    ax : matplotlib.pyplot.axes object
        Axes or array of axes containing the plot.

    See Also
    --------
    matplotlib.pyplot.plot() for possible **kwargs.
    """
    if not isinstance(signal, Signal):
        raise TypeError('Input data has to be of type: Signal.')

    with plt.style.context(plotstyle(style)):
        ax = _line._phase(signal, deg, unwrap, ax, **kwargs)

    plt.tight_layout()

    Interaction('LineXLog', ax, signal, style, **kwargs)

    return ax


def group_delay(signal, ax=None, style='light', **kwargs):
    """Plot the group delay on the positive frequency axis.

    Parameters
    ----------
    signal : Signal
        pyfar Signal object.
    ax : matplotlib.pyplot.axes object
        Axes to plot on. The default is None, which uses the current figure
        ore creates a new one if no figure exists.
    style : str
        'light' or 'dark' to use the pyfar plot styles or stlye from
        matplotlib.pyplot.available. the default is 'light'
    **kwargs
        Keyword arguments that are piped to matplotlib.pyplot.plot

    Returns
    -------
    ax : matplotlib.pyplot.axes object
        Axes or array of axes containing the plot.

    See Also
    --------
    matplotlib.pyplot.plot() for possible **kwargs.
    """

    if not isinstance(signal, Signal):
        raise TypeError('Input data has to be of type: Signal.')

    with plt.style.context(plotstyle(style)):
        ax = _line._group_delay(signal, ax, **kwargs)

    plt.tight_layout()
    Interaction('LineXLog', ax, signal, style, **kwargs)

    return ax


def spectrogram(signal, dB=True, log_prefix=20, log_reference=1,
                yscale='linear', window='hann', window_length=1024,
                window_overlap_fct=0.5, cmap=mpl.cm.get_cmap(name='magma'),
                ax=None, style='light'):
    """Plot the magnitude spectrum versus time.

    Parameters
    ----------
    signal : Signal
        pyfar Signal object.
    log : Boolean
        Speciefies, whether the y axis is plotted logarithmically.
        The default is False.
    db : Boolean
        Falg to plot the logarithmic magnitude specturm. The default is True.
    log_prefix : integer, float
        Prefix for calculating the logarithmic time data. The default is 20.
    log_reference : integer
        Reference for calculating the logarithmic time data. The default is 1.
    yscale : str
        'linear' or 'log' to plot on a linear or logarithmic y-axis. The
        default is 'linear'.
    window : str
        Specifies the window (See scipy.signal.get_window). The default is
        'hann'.
    window_length : integer
        Specifies the window length in samples. The default ist 1024.
    window_overlap_fct : double
        Ratio of points to overlap between fft segments [0...1]. The default is
        0.5
    cmap : matplotlib.colors.Colormap(name, N=256)
        Colormap for spectrogram. Defaults to matplotlibs 'magma' colormap.
    ax : matplotlib.pyplot.axes object
        Axes to plot on. If not given, the current figure will be used.
    style : str
        'light' or 'dark' to use the pyfar plot styles or stlye from
        matplotlib.pyplot.available. the default is 'light'

    Returns
    -------
    ax : matplotlib.pyplot.axes object
        Axes or array of axes containing the plot.
    """
    if not isinstance(signal, Signal):
        raise TypeError('Input data has to be of type: Signal.')

    with plt.style.context(plotstyle(style)):
        ax = _line._spectrogram_cb(
            signal, dB, log_prefix, log_reference, yscale,
            window, window_length, window_overlap_fct,
            cmap, ax)

    plt.tight_layout()
    Interaction('spectrogram', ax[0], signal, style)

    return ax


def freq_phase(signal, log_prefix=20, log_reference=1, deg=False, unwrap=False,
               ax=None, style='light', **kwargs):
    """Plot the magnitude and phase spectrum in a 2 by 1 subplot layout.

    Parameters
    ----------
    signal : Signal
        pyfar Signal object.
    log_prefix : integer, float
        Prefix for calculating the logarithmic time data. The default is 20.
    log_reference : integer
        Reference for calculating the logarithmic time data. The default is 1.
    deg : Boolean
        Flag to plot the phase in degrees. The default is False.
    unwrap : Boolean, str
        True to unwrap the phase or "360" to unwrap the phase to 2 pi. The
        default is False.
    ax : matplotlib.pyplot.axes object
        Axes to plot on. The default is None, which uses the current figure
        ore creates a new one if no figure exists.
    style : str
        'light' or 'dark' to use the pyfar plot styles or stlye from
        matplotlib.pyplot.available. the default is 'light'
    **kwargs
        Keyword arguments that are piped to matplotlib.pyplot.plot

    Returns
    -------
    ax : matplotlib.pyplot.axes object
        Axes or array of axes containing the plot.

    See Also
    --------
    matplotlib.pyplot.plot() for possible **kwargs.
    """

    if not isinstance(signal, Signal):
        raise TypeError('Input data has to be of type: Signal.')

    with plt.style.context(plotstyle(style)):
        ax = _line._freq_phase(signal, log_prefix, log_reference, deg, unwrap,
                               ax, **kwargs)
    plt.tight_layout()
    Interaction('LineXLog', ax[0], signal, style, **kwargs)

    return ax


def freq_group_delay(signal, log_prefix=20, log_reference=1, ax=None,
                     style='light', **kwargs):
    """Plot the magnitude and group delay spectrum in a 2 by 1 subplot layout.

    Parameters
    ----------
    signal : Signal
        pyfar Signal object.
    log_prefix : integer, float
        Prefix for calculating the logarithmic time data. The default is 20.
    log_reference : integer
        Reference for calculating the logarithmic time data. The default is 1.
    ax : matplotlib.pyplot.axes object
        Axes to plot on. The default is None, which uses the current figure
        ore creates a new one if no figure exists.
    style : str
        'light' or 'dark' to use the pyfar plot styles or stlye from
        matplotlib.pyplot.available. the default is 'light'
    **kwargs
        Keyword arguments that are piped to matplotlib.pyplot.plot

    Returns
    -------
    ax : matplotlib.pyplot.axes object
        Axes or array of axes containing the plot.

    See Also
    --------
    matplotlib.pyplot.plot() for possible **kwargs.
    """
    if not isinstance(signal, Signal):
        raise TypeError('Input data has to be of type: Signal.')

    with plt.style.context(plotstyle(style)):
        ax = _line._freq_group_delay(signal, log_prefix, log_reference,
                                     ax, **kwargs)

    plt.tight_layout()
    Interaction('LineXLog', ax[0], signal, style, **kwargs)

    return ax


def custom_subplots(signal, plots, ax=None, style='light', **kwargs):
    """
    Generate subplot with a custom layout based on a list of plot function
    handles. The subplot layout is taken from the shape of the plot function
    handle list.

    Parameters
    ----------
    signal : Signal
        A pyfar Signal object
    plots : list, nested list
        list with function handles for plotting (e.g. pyfar.plot.line.time.
        See example below)
    ax : matplotlib.pyplot.axes object
        Axes to plot on. The default is None, which uses the current figure
        ore creates a new one if no figure exists.
    style : str
        'light' or 'dark' to use the pyfar plot styles or stlye from
        matplotlib.pyplot.available. the default is 'light'
    **kwargs
        Keyword arguments that are piped to matplotlib.pyplot.plot

    Returns
    -------
    ax : axes
        List of axes handles

    Examples
    --------
    >>> from pyfar import Signal
    >>> import pyfar.plot.line as ppl
    >>>
    >>> # generate a signal
    >>> s = Signal([0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 1e3)
    >>>
    >>> # two by two plot of time and frequency signals
    >>> ppl.multi(s, [[ppl.time, ppl.time_dB], [ppl.freq, ppl.group_delay]])

    """
    if not isinstance(signal, Signal):
        raise TypeError('Input data has to be of type: Signal.')

    with plt.style.context(plotstyle(style)):
        ax = _line._custom_subplots(signal, plots, ax, **kwargs)
    plt.tight_layout()

    return ax
