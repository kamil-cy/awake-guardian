#!/usr/bin/env python

from PySide2.QtWidgets import QApplication
from sys import argv, exit

from awake_guardian import AwakeGurdian

if not QApplication.instance():
    app = QApplication(argv)
else:
    app = QApplication.instance()
aw = AwakeGurdian(app)
exit(app.exec_())
