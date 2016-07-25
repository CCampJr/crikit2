# -*- coding: utf-8 -*-
"""
CRIkit Options Dialogs (crikit.ui.dialog_options)
=======================================================

Classes that present dialog boxes that retrieve options

DialogDarkOptions : Dark subtraction options dialog

DialogKKOptions : Phase retrieval options dialog. Note: this class only\
                    considers the Kramers-Kronig currently

References
----------
[1] C H Camp Jr, Y J Lee, and M T Cicerone, "Quantitative, Comparable Coherent \
Anti-Stokes Raman Scattering (CARS) Spectroscopy: Correcting Errors in Phase \
Retrieval," Journal of Raman Spectroscopy (2016). arXiv:1507.06543.

Software Info
--------------

Original Python branch: Feb 16 2015

author: ("Charles H Camp Jr")

email: ("charles.camp@nist.gov")

version: ("16.03.14")
"""

# Append sys path
import sys as _sys
import os as _os
if __name__ == '__main__':
    _sys.path.append(_os.path.abspath('../../'))

# Generic imports for QT-based programs
from PyQt5.QtWidgets import (QApplication as _QApplication,
                             QWidget as _QWidget, QDialog as _QDialog,
                             QMainWindow as _QMainWindow,
                             QSizePolicy as _QSizePolicy)
import PyQt5.QtCore as _QtCore

# Other imports
import numpy as _np

# Import from Designer-based GUI
from crikit.ui.qt_KKOptions import Ui_Dialog as Ui_KKOptions

from crikit.ui.subui_ploteffect import DialogPlotEffect as _DialogPlotEffect
from crikit.ui.widget_ploteffect import widgetKK as _widgetKK

# Generic imports for MPL-incorporation
import matplotlib as _mpl
_mpl.use('Qt5Agg')
_mpl.rcParams['font.family'] = 'sans-serif'
_mpl.rcParams['font.size'] = 10
#import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as _FigureCanvas, \
    NavigationToolbar2QT as _NavigationToolbar)

from matplotlib.figure import Figure as _Figure


class DialogKKOptions(_QDialog):
    """
    DialogKKOptions : Phase-Retrieval (only Kramers-Kronig currently \
        supported) options dialog

    Static Method
    -------------
    dialogKKOptions : Used to call UI and retrieve results of dialog

    References
    ----------
    [1] Y. Liu, Y. J. Lee, and M. T. Cicerone, "Broadband CARS spectral \
    phase retrieval using a time-domain Kramers-Kronig transform," \
    Opt. Lett. 34, 1363-1365 (2009).

    [2] C H Camp Jr, Y J Lee, and M T Cicerone, "Quantitative, Comparable Coherent \
    Anti-Stokes Raman Scattering (CARS) Spectroscopy: Correcting Errors in Phase \
    Retrieval," Journal of Raman Spectroscopy (2016). arXiv:1507.06543.

    Software Info
    --------------

    Original Python branch: Feb 16 2015

    author: ("Charles H Camp Jr")

    email: ("charles.camp@nist.gov")

    version: ("16.2.16")
    """
    NORM_TO_NRB = True
    NRB_AMP = 0.0
    CARS_AMP = 0.0
    PHASE_OFFSET = 0.0
    PAD_FACTOR = 1

    def __init__(self, parent=None, data=None):
        super(DialogKKOptions, self).__init__(parent) ### EDIT ###
        self.ui = Ui_KKOptions() ### EDIT ###
        self.ui.setupUi(self)     ### EDIT ###

        self.ui.doubleSpinBoxCARSAmp.setValue(self.CARS_AMP)
        self.ui.doubleSpinBoxNRBAmp.setValue(self.NRB_AMP)
        self.ui.doubleSpinBoxPhase.setValue(self.PHASE_OFFSET)
        self.ui.checkBoxNormToNRB.setChecked(self.NORM_TO_NRB)
        self.ui.spinBoxPadFactor.setValue(self.PAD_FACTOR)

        self.norm_to_nrb = self.NORM_TO_NRB

        self.data = data

        if data is None:
            self.ui.pushButtonInteractive.setEnabled(False)
        else:
            self.ui.pushButtonInteractive.pressed.connect(self.goInteractive)

    def goInteractive(self):

        plugin = _widgetKK()

        winPlotEffect = _DialogPlotEffect.dialogPlotEffect(self.data, x=self.data[0], plugin=plugin, xlabel='Wavenumber (cm$^{-1}$)', ylabel='Imag. {$\chi_R$} (au)')

        if winPlotEffect is not None:
            self.ui.doubleSpinBoxCARSAmp.setValue(winPlotEffect.cars_bias)
            self.ui.doubleSpinBoxNRBAmp.setValue(winPlotEffect.nrb_bias)
            self.ui.checkBoxNormToNRB.setChecked(winPlotEffect.nrb_norm)
            self.ui.doubleSpinBoxPhase.setValue(winPlotEffect.phaselin)
            self.ui.spinBoxPadFactor.setValue(winPlotEffect.pad_factor)

    @staticmethod
    def dialogKKOptions(parent=None, data=None):
        """
        Static Method.

        Retrieve dark subtraction dialog results

        Inputs
        ----------
        None : None

        Returns
        ----------
        out : dict{'cars_amp' : float, 'nrb_amp' : float,
                   'phase_offset' : float, 'norm_to_nrb' : bool,
                   'pad_factor' : int}
            In order: CARS amp offset, NRB amp offset, phase offset, normalize
                by NRB, pad factor
        """
        dialog = DialogKKOptions(parent=parent,data=data)

        result = dialog.exec_()

        if result == 1:
            ret = {}
            ret['cars_amp'] = dialog.ui.doubleSpinBoxCARSAmp.value()
            ret['nrb_amp'] = dialog.ui.doubleSpinBoxNRBAmp.value()
            ret['phase_offset'] = dialog.ui.doubleSpinBoxPhase.value()
            ret['norm_to_nrb'] = dialog.ui.checkBoxNormToNRB.isChecked()
            ret['pad_factor'] = dialog.ui.spinBoxPadFactor.value()
            return ret
        else:
            return None

if __name__ == '__main__':


    app = _QApplication(_sys.argv)
    app.setStyle('Cleanlooks')


#    winDark = DialogDarkOptions.dialogDarkOptions(darkloaded=True)

    from crikit.data.hsi import Hsi as _Hsi

    temp = _Hsi()

    WN = _np.linspace(500,4000,1000)

    CARS = _np.zeros((20,20,WN.size))
    CARS[:,:,:] = _np.abs(1/(1000-WN-1j*20) + 1/(3000-WN-1j*20) + .055)
    temp.data = CARS
    temp.freq.data = WN


    NRB = 0*WN + .055


    winKK = DialogKKOptions.dialogKKOptions(data=[WN, NRB,
        temp.get_rand_spectra(10, pt_sz=3, quads=False)])

    print('KK return: {}'.format(winKK))

    _sys.exit()