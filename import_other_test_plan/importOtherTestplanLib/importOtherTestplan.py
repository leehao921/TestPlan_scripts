import os

from .dataLib import TestPlan as tpx
from .dataLib import DieSpec as die
from .dataLib import PrbSpec as prb
from .dataLib import TestSpec as tst
from .dataLib import WafSpec as waf

from .customLib import getWafSpec as get_waf
from .customLib import getDieSpec as get_die
from .customLib import getPrbSpec as get_prb
from .customLib import getTestSpec as get_tst
'''
Author  :chuiting.kong
Date    :2023/12/26
Usage   :Calling other scripts' functions to implement import Other Testplan.
'''


class importOtherTestPlan:

    def __init__(self):
        self.tpx = None
        self.tpx_waf = None
        self.tpx_die = None
        self.tpx_tst = None
        self.tpx_prb = None
        self.err = ''
        return

    def importWafSpec(self, ks_file, shot_file):
        waf_info = get_waf.getWafInfo_TEL(ks_file, False)
        # print(waf_info)
        waf_info.convertWithShotToDie(shot_file)
        if not waf_info.isWafSpec:
            self.err = "This is not a wafer spec file or it is empty !"
            return False
        self.tpx_waf = waf.WafSpec(file_attribute=waf_info.fileAttr, attribute_content=waf_info.attr_content,
                                   body_content=waf_info.body_content)
        return True

    def exportWafSpec(self, target_dir):
        try:
            if not os.path.exists(target_dir):
                os.mkdir(target_dir)
        except Exception as reason:
            return False, str(reason)
        self.tpx_waf.saveAsXml(os.path.join(target_dir, self.tpx_waf.Name + '.waf'))
        return True, ''

    def importDieSpec(self, ks_file, isSkip):
        die_info = get_die.getDieInfo(ks_file, isSkip=isSkip)
        if not die_info.isDieSpec:
            self.err = "This is not a die spec file or it is empty !"
            return False
        self.tpx_die = die.DieSpec(file_attribute=die_info.fileAttr, body_content=die_info.body_content)
        return True

    def exportDieSpec(self, target_dir):
        try:
            if not os.path.exists(target_dir):
                os.mkdir(target_dir)
        except Exception as reason:
            return False, str(reason)
        self.tpx_die.saveAsXml(os.path.join(target_dir, self.tpx_die.Name + '.die'))
        return True, ''

    def importTstSpec(self, tst_file, map_file, lim_file, template_file,skip):
        #    tst_file, map_file, lim_file, skip: bool
        tst_info = get_tst.getTestSpec(tst_file, map_file, lim_file, template_file,skip)
        if tst_info.err != '':
            self.err = tst_info.err
            return False
        self.tpx_tst = tst.TstSpec(file_attribute=tst_info.fileAttr, body_content=tst_info.body_content)
        return True

    def exportTstSpec(self, target_dir):
        try:
            if not os.path.exists(target_dir):
                os.mkdir(target_dir)
        except Exception as reason:
            return False, str(reason)
        self.tpx_tst.saveAsXml(os.path.join(target_dir, self.tpx_tst.Name + '.tst'))
        return True, ''

    def importPrbSpec(self, ks_file, _):
        prb_info = get_prb.getPrbInfo(ks_file)
        if not prb_info.isPrbSpec:
            self.err = "This is not a probe spec file or it is empty !"
            return False
        self.tpx_prb = prb.PrbSpec(file_attribute=prb_info.fileAttr, body_content=prb_info.body_content)
        return True

    def exportPrbSpec(self, target_dir):
        try:
            if not os.path.exists(target_dir):
                os.mkdir(target_dir)
        except Exception as reason:
            return False, str(reason)
        self.tpx_prb.saveAsXml(os.path.join(target_dir, self.tpx_prb.Name + '.prb'))

    def importTpxFile(self, filesMap: {}, flagsMap: {}):
        # waf
        if 'waf' in filesMap and filesMap['waf']:
            if isinstance(filesMap['waf'], list):
                for file in filesMap['waf']:
                    if not self.importWafSpec(file, filesMap["mapping"]):
                        return False, self.err
            else:
                if not self.importWafSpec(filesMap['waf'], filesMap["mapping"]):
                    return False, self.err

        # die
        if 'die' in filesMap and filesMap['die']:
            if isinstance(filesMap['die'], list):
                for file in filesMap['die']:
                    if not self.importDieSpec(file, False):
                        return False, self.err
            else:
                if not self.importDieSpec(filesMap['die'], False):
                    return False, self.err

        # tst
        if 'tst' in filesMap and filesMap['tst']:
            if isinstance(filesMap['tst'], list):
                for file in filesMap['tst']:
                    if not self.importTstSpec(file, filesMap['mapping'], filesMap['limit'], filesMap['template'], flagsMap['skipComment']):
                        return False, self.err
            else:
                if not self.importTstSpec(filesMap['tst'], filesMap['mapping'], filesMap['limit'], filesMap['template'], flagsMap['skipComment']):
                    return False, self.err

        # prb
        if 'prb' in filesMap and filesMap['prb']:
            if isinstance(filesMap['prb'], list):
                for file in filesMap['prb']:
                    if not self.importPrbSpec(file, False):
                        return False, self.err
            else:
                if not self.importPrbSpec(filesMap['prb'], False):
                    return False, self.err

        # testplan
        if self.tpx_waf or self.tpx_die or self.tpx_tst or self.tpx_prb:
            self.tpx = tpx.TestPlan(self.tpx_waf, self.tpx_die, self.tpx_tst, self.tpx_prb)
        else:
            return False, 'Please select at least one spec file !'
        return True, ''

    def exportTpx(self, target_dir):
        try:
            self.tpx.saveAsXML(target_dir)
        except Exception as reason:
            return False, str(reason)
        return True, ''

    @staticmethod
    def checkDieName(tpx_waf,dieFileAttr,autofixdiename):
        # check waferspec and diespec names consisentance
        if tpx_waf and dieFileAttr:
            dienames = []
            tpx_waf.getDieNames(dienames)
            if dieFileAttr['Name'] not in dienames:
                if autofixdiename and len(dienames) == 1:
                    dieFileAttr['Name'] = dienames[0]
                else:
                    return False
        return True
