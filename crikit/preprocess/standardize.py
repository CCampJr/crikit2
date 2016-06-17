# -*- coding: utf-8 -*-
"""
Standardization

Created on Thu Apr 14 08:53:08 2016

@author: chc
"""

__all__ = ['anscombe', 'anscombe_inverse']

if __name__ == '__main__':  # pragma: no cover
    import sys as _sys
    import os as _os
    _sys.path.append(_os.path.abspath('../../'))

import timeit as _timeit
import copy as _copy
import numpy as _np

from crikit.preprocess.algorithms.anscombe import (gen_anscombe_forward as ansc,
                                                   gen_anscombe_inverse_exact_unbiased as inv_ansc)

class Anscombe:
    """
    Implement the generalized forward Anscombe transformation.

    Signal : :math:`X`

    Mean of Gaussian noise :  :math:`<g>`

    Standard deviation of Gaussian noise :  :math:`\sigma_g`

    Noise of type 'type' : :math:`N_{type}`

    Poisson noise multiplier : :math:`\\alpha`

    Model : :math:`X = \\alpha*N_{Poisson}\{X\} + N_{Gauss}\{<g>, \sigma_g\},`

    Parameters
    ----------
    data : ndarray.
        Signal with mixed Gaussian and Poisson noise to transform.

    gauss_std : float
        Standard deviation of Gaussian noise. :math:`\sigma_g` in model.

    poisson_multi : float, optional (default=1.0)
        A multiplier that scales the effect of the Poisson noise. \
        :math:`\\alpha` in model.

    gauss_mean : float, optional (default=0.0)
        Mean Gaussian noise level. :math:`<g>` in model.

    rng : ndarray (1D), optional
        Range of pixels to perform operation over.

    overwrite : bool, optional (default=True)

    Returns
    -------
    ndarray
        Altered data if overwrite is False

    None
        Return None if overwrite is True

    See Also
    -----
    * See the docstring of ./algorithms/anscombe for more information.

    Citation Refs
    ------------------
    [1] M. Mäkitalo and A. Foi, "Optimal inversion of the generalized Anscombe \
        transformation for Poisson-Gaussian noise", IEEE Trans. Image Process., \
        doi:10.1109/TIP.2012.2202675

    [2] J.L. Starck, F. Murtagh, and A. Bijaoui, Image  Processing  and  Data \
        Analysis, Cambridge University Press, Cambridge, 1998)

    [3] C. H. Camp Jr, Y. J. Lee, and M. T. Cicerone, "Quantitative, \
        comparable coherent anti-Stokes Raman scattering (CARS) \
        spectroscopy: Correcting errors in phase retrieval," Journal of Raman \
        Spectroscopy 47, 408-415 (2016). arXiv:1507.06543.
    """
    def __init__(self, gauss_std, gauss_mean=0.0, poisson_multi=1.0,
             rng=None):

        self.gauss_std = gauss_std
        self.gauss_mean = gauss_mean
        self.poisson_multi = poisson_multi

        if rng is None:
            self.rng = None
        elif len(rng) == 2:
            rng.sort()
            self.rng = _np.arange(rng[0],rng[1])
        else:
            self.rng = rng

    def _calc(self, data, ret_obj):
        # Anscombe transform
        if self.rng is None:
            self.rng = _np.arange(data.shape[-1])
            out = ansc(data, gauss_std=self.gauss_std,
                       gauss_mean=self.gauss_mean,
                       poisson_multi=self.poisson_multi)
        else:
            out = ansc(data[..., self.rng], gauss_std=self.gauss_std,
                       gauss_mean=self.gauss_mean,
                       poisson_multi=self.poisson_multi)

        try:
            ret_obj *= 0
            ret_obj[..., self.rng] = out
        except:
            return False
        else:
            return True

    def transform(self, data):
        """
        Generalized Anscombe transform (Overwrite data).

        Parameters
        ----------
        data : ndarray
            Input data.

        Returns
        -------
        bool
            Returns the success state (True=success)

        """
        success = self._calc(data, ret_obj=data)
        return success

    def calculate(self, data):
        """
        Generalized Anscombe transform (Return copy).

        Parameters
        ----------
        data : ndarray
            Input data.

        Returns
        -------
        ndarray
            Returns Anscombe-transformed data (or None if fails)

        """
        data_copy = _copy.deepcopy(data)
        success = self._calc(data, ret_obj=data_copy)
        if success:
            return data_copy
        else:
            return None


class AnscombeInverse:
    """
    Applies an exact, unbiased inverse of the generalized Anscombe \
    variance-stabilizing transformation assuming a mixed Poisson-Gaussian \
    noise model as:


    Signal : :math:`X`

    Mean of Gaussian noise :  :math:`<g>`

    Standard deviation of Gaussian noise :  :math:`\sigma_g`

    Noise of type 'type' : :math:`N_{type}`

    Poisson noise multiplier : :math:`\\alpha`

    Model : :math:`X = \\alpha*N_{Poisson}\{X\} + N_{Gauss}\{<g>, \sigma_g\},`

    Parameters
    ----------
    data : Spectrum (or subclass) object or ndarray.
        Signal with mixed Gaussian and Poisson noise to transform.

    gauss_std : float
        Standard deviation of Gaussian noise. :math:`\sigma_g` in model.

    poisson_multi : float, optional (default=1.0)
        A multiplier that scales the effect of the Poisson noise. \
        :math:`\\alpha` in model.

    gauss_mean : float, optional (default=0.0)
        Mean Gaussian noise level. :math:`<g>` in model.

    rng : ndarray (1D), optional
        Range of pixels to perform operation over.

    overwrite : bool, optional (default=True)

    See Also
    -----
    * See the docstring of ./algorithms/anscombe for more information.

    Citation Refs
    ------------------
    [1] M. Mäkitalo and A. Foi, "Optimal inversion of the generalized Anscombe \
        transformation for Poisson-Gaussian noise", IEEE Trans. Image Process., \
        doi:10.1109/TIP.2012.2202675

    [2] J.L. Starck, F. Murtagh, and A. Bijaoui, Image  Processing  and  Data \
        Analysis, Cambridge University Press, Cambridge, 1998)

    [3] C. H. Camp Jr, Y. J. Lee, and M. T. Cicerone, "Quantitative, \
        comparable coherent anti-Stokes Raman scattering (CARS) \
        spectroscopy: Correcting errors in phase retrieval," Journal of Raman \
        Spectroscopy 47, 408-415 (2016). arXiv:1507.06543.
    """

    def __init__(self, gauss_std, gauss_mean=0.0, poisson_multi=1.0, rng=None):
        self.gauss_std = gauss_std
        self.gauss_mean = gauss_mean
        self.poisson_multi = poisson_multi

        if rng is None:
            self.rng = None
        elif len(rng) == 2:
            rng.sort()
            self.rng = _np.arange(rng[0],rng[1])
        else:
            self.rng = rng

    def _calc(self, data, ret_obj):

        # Inverse Anscombe transform
        if self.rng is None:
            self.rng = _np.arange(data.shape[-1])
            out = inv_ansc(data, gauss_std=self.gauss_std,
                       gauss_mean=self.gauss_mean,
                       poisson_multi=self.poisson_multi)
        else:
            out = inv_ansc(data[..., self.rng], gauss_std=self.gauss_std,
                       gauss_mean=self.gauss_mean,
                       poisson_multi=self.poisson_multi)

        try:
            ret_obj *= 0
            ret_obj[..., self.rng] = out
        except:
            return False
        else:
            return True

    def transform(self, data):
        """
        Generalized Inverse Anscombe transform (Overwrite data).

        Parameters
        ----------
        data : ndarray
            Input data.

        Returns
        -------
        bool
            Returns the success state (True=success)

        """
        success = self._calc(data, ret_obj=data)
        return success

    def calculate(self, data):
        """
        Generalized Inverse Anscombe transform (Return copy).

        Parameters
        ----------
        data : ndarray
            Input data.

        Returns
        -------
        ndarray
            Returns Anscombe-transformed data (or None if fails)

        """
        data_copy = _copy.deepcopy(data)
        success = self._calc(data, ret_obj=data_copy)
        if success:
            return data_copy
        else:
            return None

if __name__ == '__main__': # pragma: no cover

    from crikit.data.spectrum import Spectrum as _Spectrum

    stddev = 20
    gain = 1

    f = _np.linspace(500,4000,1000)
    sig = 10e4*_np.exp(-(f-2000)**2/(500**2))

    gnoise = stddev*_np.random.randn(f.size)

    sig_mix = _np.random.poisson(sig) + gnoise

    import matplotlib.pyplot as _plt

    anscombe = Anscombe(gauss_std=stddev, gauss_mean=0, poisson_multi=gain)

    sig2 = _Spectrum(sig)

    out = anscombe.calculate(sig2.data)
    _plt.subplot(211)
    _plt.plot(sig2.data, label='Data')
    _plt.title('Untransformed Space')
    _plt.legend(loc='best')

    _plt.subplot(212)
    _plt.plot(out, label='Calculate')

    out2 = anscombe.transform(sig2.data)
    _plt.plot(sig2.data, label='Transform')
    _plt.legend(loc='best')
    _plt.title('Anscombe Transform')
    _plt.show()

    print('Transform and Calculate Equivalent: {}'.format(_np.allclose(out,
          sig2.data)))

    inverse_anscombe = AnscombeInverse(gauss_std=stddev, gauss_mean=0,
                                       poisson_multi=gain)

    sig2 = _Spectrum(sig)
    sig2_ansc = anscombe.calculate(sig2.data)

    out = inverse_anscombe.calculate(sig2_ansc)
    _plt.subplot(211)
    _plt.plot(sig2.data, label='Data')
    _plt.plot(out, label='Calculate')
    _plt.title('Untransformed Space/Inverse Anscombe')

    _plt.legend(loc='best')

    _plt.subplot(212)
    _plt.plot(sig2_ansc, label='Anscombe')


    _plt.legend(loc='best')
    _plt.title('Anscombe Transform')
    _plt.show()

#    print('Data and Inverse of Anscombe Close: {}'.format(_np.allclose(out,
#          sig2.data)))

    _plt.figure()
    _plt.plot(out-sig2.data)
    _plt.title('Inverse Anscombe - Original Data')
    _plt.show()
#
#    print((out-sig2.data)[0])

#    # Recalc sig
#    sig = 10e4*_np.exp(-(f-2000)**2/(500**2))
#
#    _plt.figure()
#    sig_ansc = anscombe(sig.data, gauss_std=stddev, poisson_multi=gain, overwrite=False)
#    out = anscombe_inverse(sig_ansc, gauss_std=stddev, poisson_multi=gain, overwrite=False)
#    _plt.plot(sig)
#    _plt.plot(out)
#    anscombe_inverse(sig_ansc, gauss_std=stddev, poisson_multi=gain, overwrite=True)
#    _plt.plot(sig_ansc)
#    _plt.show()