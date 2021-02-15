import shutil
import sys
from pathlib import Path

from PySide2.QtCore import QEvent, QFile
from PySide2.QtGui import QKeySequence
from PySide2.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox, QShortcut

from ui_window import Ui_MainWindow


class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		if sys.platform == "win32":
			self.browsefolder = str(Path.home()) + '\\Principia\\lvl\\local\\'
		else:
			# if you're smart enough to use anything not windows you should be smart enough to find your level folder
			self.browsefolder = str(Path.home())

		self.ui.browse_button.clicked.connect(self.open_file_dialog)
		self.ui.go_button.clicked.connect(self.dothething)

	def open_file_dialog(self):
		self.ui.path_input.setText(QFileDialog.getOpenFileName(self, 'Select Principia level.', self.browsefolder, 'Principia Level File (*.plvl)')[0])

	def dothething(self):
		self.ui.statusBar.clearMessage()
		file = self.ui.path_input.text()

		if self.ui.backup_checkbox.isChecked():
			print('backing up file')
			shutil.copy(file, file + '.bak')

		with open(file, "rb+") as f:
			print('successfully opened file (%s)' % file)
			level_version = f.read(1)

			if not level_version >= bytes(0) and level_version <= bytes(29):
				QMessageBox.critical(self, 'Error', "File isn't a Principia level or has an unsupported level version.")
				return

			level_type = f.read(1)
			level_community_id = f.read(4)

			print("Level version: 0x%s" % level_version.hex())
			print("Community ID: 0x%s" % level_community_id.hex())
			print("Changing community ID to 0x00000000")

			f.seek(2)
			f.write(b"\00\00\00\00")

			self.ui.statusBar.showMessage('Successfully scrubbed the community ID of selected file!')


if __name__ == "__main__":
	app = QApplication(sys.argv)

	window = MainWindow()
	window.show()

	sys.exit(app.exec_())
