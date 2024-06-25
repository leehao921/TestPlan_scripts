import xml.etree.ElementTree as ET

from .prettyXML import prettyXml



'''
Author  : jianghao.zheng
Date    : 2023/7/19
Usage   : Data structure of WAFER SPEC
'''

default_dict = {
    'Type': 'Wafer',
    'Name': '',
    'Vers': '1',
    'Desc': 'Description for this Wafer spec.',
    'Date': '',
    'Time': '',
    'User': '',
}


class WafSpec:
    file_attribute_list = ['Type', 'Name', 'Vers', 'Desc', 'Date', 'Time', 'User']
    die_pos_head_label = ['Select', 'Die', 'X', 'Y', 'Site']
    attr_head_label = ['Name', 'Value', 'Type', 'Unit', 'Comment']
    attr_com_content = ['Diameter of wafer',
                        'Die Width',
                        'Die Height',
                        'Orientation of wafer flat or notch in degrees',
                        'X index of alignment die',
                        'Y index of alignment die',
                        'X position (in microns) of alignment modules',
                        'Y position (in microns) of alignment modules',
                        'Center die index in the wafer',
                        'Center die index in the wafer',
                        'Offset X distance from the center point of the wafer to the left bottom point of the center die',
                        'Offset Y distance from the center point of the wafer to the left bottom point of the center die',
                        'Define direction of coordinate. 1: (0,0) locates lower left. 2: (0,0) locates lower right. 3: (0,0) locates upper right. 4: (0,0) locates upper left',
                        'Select the shape of wafer from wafer flat(WAFERSHAPE=0) or norch(WAFERSHAPE=1)']
    attr_value_label = ['SIZE', 'STEPX',
                        'STEPY', 'FLAT',
                        'ALIGNDIEX', 'ALIGNDIEY',
                        'ALIGNMOEX', 'ALIGNMOEY',
                        'CENTERDIEX', 'CENTERDIEY',
                        'OFFSETDIEX', 'OFFSETDIEY',
                        'COORDINATE', 'WAFERSHAPE']

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
        root = ET.Element("WaferSpec")
        root.set('Name', '{}'.format(self.Name))

        # for sub node
        die_pos = ET.SubElement(root, "DiePosition")
        attr = ET.SubElement(root, "Attribute")
        des = ET.SubElement(root, "Description")

        # for die sub node
        space_list_body = []
        for i in range(len(self.die_pos_head_label)):
            max_con = max(len(row[i]) for row in self.body_con)
            space_list_body.append(max(len(self.die_pos_head_label[i]), max_con))
        die_pos_head = ET.SubElement(die_pos, "Head")
        head_content = []
        for i in range(len(self.die_pos_head_label)):
            str = '[{}] '.format(self.die_pos_head_label[i].ljust(space_list_body[i]))
            head_content.append(str)
        die_pos_head.text = ''.join(head_content)
        for it in self.body_con:
            content = []
            for i in range(len(it)):
                str = ' {}  '.format(it[i].ljust(space_list_body[i]))
                content.append(str)
            item = die_pos_head = ET.SubElement(die_pos, "Item")
            item.text = ''.join(content)

        # for attr
        space_list_attr = []
        # name length max
        for i in range(len(self.attr_head_label)):
            max_len = len(self.attr_head_label[i])
            if self.attr_head_label[i] == 'Name':
                max_len_2 = max([len(s) for s in self.attr_con.keys()])
                space_list_attr.append(max(max_len, max_len_2))
            elif self.attr_head_label[i] != 'Comment':
                value_list = []
                for key, item in self.attr_con.items():
                    if self.attr_head_label[i] == 'Value':
                        value_list.append(item[2])
                    elif self.attr_head_label[i] == 'Type':
                        value_list.append(item[0])
                    elif self.attr_head_label[i] == 'Unit':
                        value_list.append(item[1])
                max_len_2 = max([len(s) for s in value_list])
                space_list_attr.append(max(max_len, max_len_2))
            elif self.attr_head_label[i] == 'Comment':
                max_len_2 = max([len(s) for s in self.attr_com_content])
                space_list_attr.append(max(max_len, max_len_2))

        attr_head = ET.SubElement(attr, "Head")
        head_content = []
        for i in range(len(self.attr_head_label)):
            str = '[{}] '.format(self.attr_head_label[i].ljust(space_list_attr[i]))
            head_content.append(str)
        attr_head.text = ''.join(head_content)

        for it in self.attr_value_label:
            item = ET.SubElement(attr, "Item")
            i = self.attr_value_label.index(it)
            content = []
            content.append(' {}  '.format(it.ljust(space_list_attr[0])))
            content.append(' {}  '.format(self.attr_con[it][2].ljust(space_list_attr[1])))
            content.append(' {}  '.format(self.attr_con[it][0].ljust(space_list_attr[2])))
            content.append(' {}  '.format(self.attr_con[it][1].ljust(space_list_attr[3])))
            content.append(' {}  '.format(self.attr_com_content[i].ljust(space_list_attr[4])))
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

    def getDieNames(self,dieNames):
        for i in self.body_con:
            _name = i[1]
            _comment = i[0]
            if _comment != '#' and dieNames.count(_name) == 0:
                dieNames.append(_name)
        pass

if __name__ == '__main__':
    file_attribute = {'Type': 'Wafer',
                      'Name': '0145',
                      'Vers': '1',
                      'Desc': 'Description for this Wafer spec.',
                      'Date': '01/24/2018',
                      'Time': '20:58:37',
                      'User': 'watpe_zj',
                      }
    attribute_content = {'SIZE': ['REAL', "mm", '300'], 'STEPX': ['REAL', "um", '24836.000000'],
                         'STEPY': ['REAL', "um", '32638.000000'], 'FLAT': ['INTEGER', "deg", '180'],
                         'ALIGNDIEX': ['INTEGER', '', '-3'], 'ALIGNDIEY': ['INTEGER', '', '3'],
                         'ALIGNMOEX': ['REAL', 'um', '0.00000'], 'ALIGNMOEY': ['REAL', 'um', '0.00000'],
                         'CENTERDIEX': ['INTEGER', '', '0'], 'CENTERDIEY': ['INTEGER', '', '0'],
                         'OFFSETDIEX': ['REAL', '', '0.000000'], 'OFFSETDIEY': ['REAL', '', '0.000000'],
                         'COORDINATE': ['INTEGER', '', '1'], 'WAFERSHAPE': ['INTEGER', '', '1']}

    body_content = [
        ['', '0145', '0', '3', ''],
        ['#', '0145', '-2', '1', ''],
        ['', '0145', '2', '1', ''],
        ['', '0145', '5', '0', ''],
        ['', '0145', '0', '0', ''],
        ['', '0145', '-5', '0', ''],
        ['', '0145', '-2', '-1', ''],
        ['', '0145', '2', '-1', ''],
        ['', '0145', '0', '-3', '']
    ]

    waf = WafSpec(file_attribute=file_attribute, attribute_content=attribute_content, body_content=body_content)
    waf.saveAsXml('a.txt')
