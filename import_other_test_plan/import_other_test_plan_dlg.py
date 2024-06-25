import os
import sys
import traceback

from PySide2.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox
from PySide2.QtGui import Qt,QIcon
from UI.main_window_ui import Ui_importOtherTestPlanDlg
from importOtherTestplanLib.importOtherTestplan import importOtherTestPlan
from UI.icon_rc import qInitResources
import time 

'''
Author  : chuiting.kong
Date    : 2024/04/18
Usage   : main window
'''

class MyWidgets(QDialog):
    def __init__(self):
        super().__init__()
        # init qrc
        qInitResources()
        #init ui
        self.ui = Ui_importOtherTestPlanDlg()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowTitleHint)
        self.setWindowIcon(QIcon(':icon/tp.ico'))
        # init val
        self.buttonMap = {}
        self.checkBoxMap = {}
        self.bindButtonAndCheckBox()
        self.res = ''
        self.opration = ''
        # init Control
        for key ,val in self.buttonMap.items():
            val[1].clicked.connect(self.onSelectFile)
        self.ui.pushButtonImport.clicked.connect(self.onImport)
        self.ui.pushButtonCancel.clicked.connect(self.onCancel)

    def onClickUseTpxFile(self,status):
        self.ui.groupBoxWaf.setDisabled(status)
        self.ui.groupBoxDie.setDisabled(status)
        self.ui.groupBoxPrb.setDisabled(status)
        self.ui.groupBoxTst.setDisabled(status)
        self.ui.checkBoxSkipComment.setDisabled(status)

    def bindButtonAndCheckBox(self):
        self.buttonMap['waf'] = ['waf',self.ui.pushButtonWaf,self.ui.lineEditWaf]
        self.buttonMap['die'] = ['die',self.ui.pushButtonDie,self.ui.lineEditDie]
        self.buttonMap['tst'] = ['tst',self.ui.pushButtonTst,self.ui.lineEditTst]
        self.buttonMap['prb'] = ['prb',self.ui.pushButtonPrb,self.ui.lineEditPrb]
        self.buttonMap['limit'] = ['lim',self.ui.pushButtonLim,self.ui.lineEditLim]
        self.buttonMap['mapping'] = ['csv',self.ui.pushButtonMapping,self.ui.lineEditMapping]
        self.buttonMap['template'] = ['csv',self.ui.pushButtonTemplate,self.ui.lineEditTemplate]
        self.buttonMap['shot'] = ['csv',self.ui.pushButtonShotDie,self.ui.lineEditShotDie]
        # checkBox
        self.checkBoxMap['skipComment'] = [self.ui.checkBoxSkipComment]


    def onSelectFile(self):
        _filter = ''
        filePath = ''
        _button = self.sender()
        for key,val in self.buttonMap.items():
           if _button == val[1]:
               _filter = val[0]
               _filter = '*.' + _filter
               filePath, _ext = QFileDialog.getOpenFileName(self, '选择文件', '', _filter)
               if not filePath:
                   return
               val[2].setText(filePath)
               break
        for key, val in self.buttonMap.items():
            if val[2].text() == '' and key != 'mapping' and key != 'template' and key != 'shot':
                _res = self.searchFile(filePath, val[0])
                val[2].setText(_res)

    @staticmethod
    def searchFile(filePath,fileExt):
        _res = ''
        _Dir = os.path.dirname(filePath)
        _NameNoExt = os.path.splitext(os.path.basename(filePath))[0]
        _fileName = os.listdir(_Dir)
        _resFiles = [_file for _file in _fileName if _file.endswith(fileExt) and _NameNoExt in _file]
        if len(_resFiles) != 0:
            _res = os.path.join(_Dir, _resFiles[0]).replace('\\', '/')
        return _res

    def onCancel(self):
        self.close()
        pass

    def onImport(self):
        try:
            tt = importOtherTestPlan()
            # collage val
            filesMap , flagsMap = {}, {}
            if not self.collageValAndCheck(filesMap,flagsMap):
                return False
            flag, err = tt.importTpxFile(filesMap,flagsMap)
            if not flag:
                return self.errBox(err)
            file_path = os.path.abspath("temp.tpx")
            flag, err = tt.exportTpx(file_path)
            if not flag:
                return self.errBox(err)
            else:
                self.res = file_path
                self.opration = 'TST'
                self.close()
        except:
            logFile = os.path.abspath(os.path.join(os.path.dirname(__file__),'../scripts.log'))
            current_time = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))
            with open(logFile, 'a', encoding='utf-8') as f:
                f.write("Last open time "+current_time+':\n-----------------\n')
                traceback.print_exc(file=f)
                f.write('\n')
            return self.errBox("Conversion falied, please check the format !")

    
    def collageValAndCheck(self,filesMap,flagsMap):
        for key,val in self.buttonMap.items():
            _filePath = val[2].text()
            filesMap[key] = _filePath
            if _filePath != '' and not os.path.exists(_filePath):
                err = f'{key} file is not exist !'.capitalize()
                self.errBox(err)
                return False
        for key,val in self.checkBoxMap.items():
            flagsMap[key] = val[0].isChecked()
        return True


    def errBox(self,err):
        dlg = QMessageBox(self)
        dlg.setText(err)
        dlg.setWindowTitle('Error')
        dlg.setIcon(QMessageBox.Critical)
        return dlg.exec_()

def main(_inputMap):
    app = QApplication(sys.argv)
    window = MyWidgets()
    window.show()
    app.exec_()
    if window.opration == '':
        return {'1': ''}
    return {'1': f'{window.opration};{window.res}'}

if __name__ == "__main__":
    inputMap = {}
    res = main(inputMap)
    print(res['1'])