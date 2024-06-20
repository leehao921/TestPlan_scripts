import xml.etree.ElementTree as ET

from .prettyXML import prettyXml

'''
Author  : jianghao.zheng
Date    : 2023/7/19
Usage   : Data structure of TEST PLAN
'''

default_dict = {
    'Type': 'Die',
    'Name': '',
    'Vers': '1',
    'Desc': 'Description for this Die spec.',
    'Date': '',
    'Time': '',
    'User': '',
}


class TstSpec:
    file_attribute_list = ['Type', 'Name', 'Vers', 'Desc', 'Date', 'Time', 'User']
    device_head_label = ['Select', 'Module', 'Device','Group', 'Algorithm','Input','Pad','Output','Limit','Comment']
    desc_head_label = ['Description']

    def __init__(self, file_attribute={}, attribute_content={}, body_content=[]):
        if len(file_attribute) != 0:
            self.getWaferAttribute(file_atribute=file_attribute)
        else:
            self.getWaferAttribute()
        self.attr_con = attribute_content
        self.body_con = body_content
        self.generateXMLTree()
        pass

    def getWaferAttribute(self, file_atribute=default_dict):
        self.Type = file_atribute[self.file_attribute_list[0]].strip()
        self.Name = file_atribute[self.file_attribute_list[1]].strip()
        self.Vers = file_atribute[self.file_attribute_list[2]].strip()
        self.Desc = file_atribute[self.file_attribute_list[3]].strip()
        self.Date = file_atribute[self.file_attribute_list[4]].strip()
        self.Time = file_atribute[self.file_attribute_list[5]].strip()
        self.User = file_atribute[self.file_attribute_list[6]].strip()

    def generateXMLTree(self):
        root = ET.Element("TestSpec")
        root.set('Name', '{}'.format(self.Name))

        # for sub node
        device_pos = ET.SubElement(root, "Device")
        des = ET.SubElement(root, "Description")

        # for die sub node
        space_list_body = []
        for i in range(len(self.device_head_label)):
            max_con = max([len(row[i]) for row in self.body_con])
            space_list_body.append(max(len(self.device_head_label[i]), max_con))
        device_pos_head = ET.SubElement(device_pos, "Head")
        head_content = []
        for i in range(len(self.device_head_label)):
            str = '[{}] '.format(self.device_head_label[i].ljust(space_list_body[i]))
            head_content.append(str)
        device_pos_head.text = ''.join(head_content)
        for it in self.body_con:
            content = []
            for i in range(len(it)):
                str = ' {}  '.format(it[i].ljust(space_list_body[i]))
                content.append(str)
            item = ET.SubElement(device_pos, "Item")
            item.text = ''.join(content)


        # for desc
        space_list_descs = []
        for i in range(len(self.desc_head_label)):
            if self.desc_head_label[i] == 'Description':
                max_len = max(len(self.Desc), len(self.desc_head_label[i]))
                space_list_descs.append(max_len)

        head_content = []
        for i in range(len(space_list_descs)):
            str = '[{}] '.format(self.desc_head_label[i].ljust(space_list_descs[i]))
            head_content.append(str)
        desc_head = ET.SubElement(des, "Head")
        desc_head.text = ''.join(head_content)
        desc_item = ET.SubElement(des, 'Item')
        str = ' {}  '.format(self.Desc)
        desc_item.text = str

        # end
        self.tree = ET.ElementTree(root)

    def saveAsXml(self, file):
        root = self.tree.getroot()
        prettyXml(root, '\t', '\n')
        tree = ET.ElementTree(root)
        tree.write(file, xml_declaration=True)
        pass


if __name__ == '__main__':
    file_attribute = {'Type': 'Die',
                      'Name': '0145',
                      'Vers': '1',
                      'Desc': 'Description for this Die spec.',
                      'Date': '01/24/2018',
                      'Time': '20:58:37',
                      'User': 'watpe_zj',
                      }
    body_content = [
        ['', 'PIB01', '1', 'R2t_fv', 'BVIA_RCFV_D72_S1D08_1024','VF=3.3,Flg=2,COUNT=1024,H=0,L=1','','BVIA_RCFV_D72_S1D08_1024','',''],
        ['', 'PIB01', '1', 'R2t_fv', 'BVIA_RCFV_D72_S1D08_1024','VF=3.3,Flg=2,COUNT=1024,H=0,L=1','','BVIA_RCFV_D72_S1D08_1024','',''],
        ['', 'PIB01', '1', 'R2t_fv', 'BVIA_RCFV_D72_S1D08_1024','VF=3.3,Flg=2,COUNT=1024,H=0,L=1','','BVIA_RCFV_D72_S1D08_1024','',''],
        ['', 'PIB01', '1', 'R2t_fv', 'BVIA_RCFV_D72_S1D08_1024','VF=3.3,Flg=2,COUNT=1024,H=0,L=1','','BVIA_RCFV_D72_S1D08_1024','',''],
        ['', 'PIB01', '1', 'R2t_fv', 'BVIA_RCFV_D72_S1D08_1024','VF=3.3,Flg=2,COUNT=1024,H=0,L=1','','BVIA_RCFV_D72_S1D08_1024','',''],
        ['', 'PIB01', '1', 'R2t_fv', 'BVIA_RCFV_D72_S1D08_1024','VF=3.3,Flg=2,COUNT=1024,H=0,L=1','','BVIA_RCFV_D72_S1D08_1024','',''],
        ['', 'PIB01', '1', 'R2t_fv', 'BVIA_RCFV_D72_S1D08_1024','VF=3.3,Flg=2,COUNT=1024,H=0,L=1','','BVIA_RCFV_D72_S1D08_1024','',''],
        ['', 'PIB01', '1', 'R2t_fv', 'BVIA_RCFV_D72_S1D08_1024','VF=3.3,Flg=2,COUNT=1024,H=0,L=1','','BVIA_RCFV_D72_S1D08_1024','',''],
        ['', 'PIB01', '1', 'R2t_fv', 'BVIA_RCFV_D72_S1D08_1024','VF=3.3,Flg=2,COUNT=1024,H=0,L=1','','BVIA_RCFV_D72_S1D08_1024','','']
    ]
    waf = TstSpec(file_attribute=file_attribute, body_content=body_content)
    waf.saveAsXml('c.txt')
