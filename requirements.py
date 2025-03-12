"""
requirements.py

This module centralizes the necessary imports and utility functions for the analysis.
It is used for setting up the environment required for processing and visualizing data,
specifically tailored for the NTCDA/Kondo analysis project.
"""

# -----------------------------------------------------------------------------
# System and Path Setup
# -----------------------------------------------------------------------------
import sys
import os
from os.path import dirname, abspath

# Append the parent directory to the system path for module resolution.
# This allows importing modules from the parent directory.
sys.path.append('..')

# -----------------------------------------------------------------------------
# Custom Modules
# -----------------------------------------------------------------------------
# Import specifications from a custom module to help with dynamic imports or configuration.
from import_functions import import_specs as spec

# -----------------------------------------------------------------------------
# Standard Libraries and Packages
# -----------------------------------------------------------------------------
import numpy as np                    # Fundamental package for array computing.
import matplotlib.pyplot as plt       # Plotting library for visualizations.
import matplotlib as mtpl             # Additional matplotlib functionality.
import matplotlib.cm as cm            # Colormap utilities for plotting.

# -----------------------------------------------------------------------------
# Scientific and Numerical Packages
# -----------------------------------------------------------------------------
from scipy import constants, special, optimize, interpolate  # Various scientific functions.
from scipy.signal import savgol_filter                      # Signal processing for smoothing data.
from scipy.optimize import curve_fit                        # Non-linear curve fitting.

# -----------------------------------------------------------------------------
# Uncertainty Calculations
# -----------------------------------------------------------------------------
from uncertainties import unumpy  # Library for calculations with uncertainties.

# -----------------------------------------------------------------------------
# Additional Utilities
# -----------------------------------------------------------------------------
from matplotlib.legend_handler import HandlerBase  # Custom legend handler for plots.
from itertools import zip_longest                     # Utility for handling iterators of different lengths.

# -----------------------------------------------------------------------------
# Color Utilities
# -----------------------------------------------------------------------------
# tol_cset and tol_cmap are custom color utilities for consistent color schemes in plots.
from colors import tol_cset, tol_cmap

# End of module.