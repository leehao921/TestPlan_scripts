import xml.etree.ElementTree as ET
from .prettyXML import prettyXml
from .WafSpec import WafSpec
from .DieSpec import DieSpec
from .TestSpec import TstSpec
from .PrbSpec import PrbSpec

'''
Author  : jianghao.zheng
Date    : 2023/7/19
Usage   : Data structure of  TestPlan
'''


class TestPlan:

    def __init__(self,wafSpec:WafSpec,dieSpec:DieSpec,tstSpec:TstSpec,prbSpec:PrbSpec):
        self.wafSpec = wafSpec
        self.dieSpec = dieSpec
        self.tstSpec = tstSpec
        self.prbSpec = prbSpec
        self.tree = None
        self.generateXMLTree()

    def generateXMLTree(self):
        root = ET.Element("SMTTestPlan")
        waf_lib = ET.SubElement(root,'WaferSpecLib')
        die_lib = ET.SubElement(root,'DieSpecLib')
        tst_lib = ET.SubElement(root,'TestSpecLib')
        super_testspec_lib = ET.SubElement(root,'SuperTestSpecLib')
        prb_lib = ET.SubElement(root,'ProbeSpecLib')

        if self.wafSpec :
            waf_lib.append(self.wafSpec.tree.getroot())
        if self.dieSpec :
            die_lib.append(self.dieSpec.tree.getroot())
        if self.tstSpec :
            tst_lib.append(self.tstSpec.tree.getroot())
        if self.prbSpec :
            prb_lib.append(self.prbSpec.tree.getroot())
        if self.prbSpec or self.wafSpec or self.dieSpec or self.tstSpec:
            self.tree = ET.ElementTree(root)

    def saveAsXML(self,file):
        root = self.tree.getroot()
        prettyXml(root, '\t', '\n')
        tree = ET.ElementTree(root)
        tree.write(file, xml_declaration=True,encoding='GBK')
        pass


