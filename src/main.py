# -*- coding: utf-8 -*-

import tsdb
import gui

parameter = gui.getParameterFromGUI()
print parameter
tsdb.getData(parameter[0], parameter[1], parameter[2], parameter[3])