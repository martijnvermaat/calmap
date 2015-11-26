.. currentmodule:: calmap


Calendar heatmaps from Pandas time series data
==============================================

Plot `Pandas <http://pandas.pydata.org/>`_ time series data sampled by day in
a heatmap per calendar year, similar to GitHub's contributions plot, using
`matplotlib <http://matplotlib.org/>`_.


Usage
-----

Assume we have some weighted events as a Pandas Series with a
DatetimeIndex. They could be Git commits (with the diff size as weight),
mileage of your runs, or minutes spent on telemarketing phone calls driving
you crazy.

For illustration purposes we just create 500 events as random float values
assigned to random days over a 700-day period:

.. plot::
    :context: close-figs

    import numpy as np; np.random.seed(sum(map(ord, 'calmap')))
    import pandas as pd
    import calmap

    all_days = pd.date_range('1/15/2014', periods=700, freq='D')
    days = np.random.choice(all_days, 500)
    events = pd.Series(np.random.randn(len(days)), index=days)

Using :func:`yearplot`, we can easily plot a heatmap of these events over a
year:

.. plot::
    :context: close-figs

    calmap.yearplot(events, year=2015)

Or we can use :func:`calendarplot` to plot all years as subplots into one
figure:

.. plot::
    :context: close-figs

    calmap.calendarplot(events, monthticks=3, daylabels='MTWTFSS',
                        dayticks=[0, 2, 4, 6], cmap='YlGn',
                        fillcolor='grey', linewidth=0,
                        fig_kws=dict(figsize=(8, 4)))

See the :ref:`API documentation <api>` for more information and examples.


Installation
------------

To install the latest release via PyPI using pip::

    pip install calmap

The latest development version `can be found on GitHub
<https://github.com/martijnvermaat/calmap>`_.


.. _api:

API documentation
-----------------

.. module:: calmap

.. autofunction:: yearplot
.. autofunction:: calendarplot


Copyright
---------

This library is licensed under the MIT License, meaning you can do whatever
you want with it as long as all copies include these license terms. The full
license text can be found in the LICENSE.rst file. See the AUTHORS.rst for for
a complete list of copyright holders.
