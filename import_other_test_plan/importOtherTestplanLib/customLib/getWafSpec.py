import csv

from .generalClass import getFileAttr

'''
Author  : chuiting.kong
Date    : 2023/12/26
Usage   :get Waf spec for Tel , TSK
'''

class getWafInfo:
    attr_value_label = ['SIZE', 'STEPX',
                        'STEPY', 'FLAT',
                        'ALIGNDIEX', 'ALIGNDIEY',
                        'ALIGNMOEX', 'ALIGNMOEY',
                        'CENTERDIEX', 'CENTERDIEY',
                        'OFFSETDIEX', 'OFFSETDIEY',
                        'COORDINATE', 'WAFERSHAPE']

    def __init__(self, file, isSkip=False):
        with open(file, 'r') as f:
            content = f.readlines()
        attr_content = []
        flag = True
        len_content = []
        for it in content:
            if '$' in it and '-' not in it:
                attr_content.append(it.strip())
            if '$' in it and '-' in it and flag:
                flag = False
                len_content = it.strip()
        self.fileAttr = getFileAttr(line_content=attr_content).file_attr
        if self.fileAttr['Type'] != "Wafer":
            self.isWafSpec = False
            return
        else:
            self.isWafSpec = True

        len_list = [len(item) for item in len_content.split(' ')]
        pos_list = []
        for i in range(len(len_list)):
            pos_list.append(sum(len_list[0:i]) + i * 1)
        self.body_content = []
        self.attr_content = {}
        body_true = False
        attr_true = False
        for i in range(len(content)):
            content[i].replace('\n', '')
            if '$' in content[i] and body_true:
                break
            if 'ATTRIBUTE' in content[i]:
                body_true = False
                attr_true = True
                continue
            if 'BODY' in content[i]:
                body_true = True
                attr_true = False
                continue
            if body_true and not attr_true:
                comment = content[i][pos_list[0]:pos_list[0] + len_list[0]].replace(' ', '')
                die_name = content[i][pos_list[1]:pos_list[1] + len_list[1]].replace(' ', '').replace("`", "")
                die_x_y = content[i][pos_list[2]:pos_list[2] + len_list[2]]
                site = content[i][pos_list[3]:pos_list[3]+len_list[3]].replace(' ','').strip()
                if len(die_x_y.split(',')) < 2:continue
                die_x, die_y = die_x_y.split(',')
                die_item = [comment, die_name.replace("`", ""), die_x.strip(), die_y.strip(), site]
                if not isSkip or comment != "#":
                    self.body_content.append(die_item)
            if not body_true and attr_true:
                item_name = content[i][pos_list[1]:pos_list[1] + len_list[1]].replace(' ', '').replace("'", "")
                value = content[i][pos_list[2]:pos_list[2] + len_list[2]].strip()
                item_list = item_name.split(',')
                item_type = item_list[0]
                if len(item_list) > 1:
                    unit = item_list[1].replace('"', '')
                else:
                    unit = ''
                name, type_s = item_type.split('=')
                if name in 'ALIGNMODX':
                    name = 'ALIGNMOEX'
                elif name in 'ALIGNMODY':
                    name = 'ALIGNMOEY'

                if name in self.attr_value_label:
                    self.attr_content[name] = [type_s, unit, value]
        pass


class getWafInfo_TEL(getWafInfo):
    def __init__(self, file, isSkip):
        super().__init__(file, isSkip)
        if not self.isWafSpec: return
        pitchx = self.attr_content[self.attr_value_label[1]][2]
        pitchy = self.attr_content[self.attr_value_label[2]][2]
        offsetx = self.attr_content[self.attr_value_label[10]][2]
        offsety = self.attr_content[self.attr_value_label[11]][2]
        # coord固定为4
        self.attr_content[self.attr_value_label[12]][2] = '4'
        newoffsetx = float(offsetx) - float(pitchx) / 2
        newoffsety = float(offsety) - float(pitchy) / 2
        self.attr_content[self.attr_value_label[10]][2] = '{:.6f}'.format(newoffsetx)
        self.attr_content[self.attr_value_label[11]][2] = '{:.6f}'.format(newoffsety)

    def convertWithShotToDie(self,shotFilePath):
        if not shotFilePath: return True
        with open(shotFilePath,'r',errors='ignore') as f:
            reader = csv.reader(f)
            tableList = list(reader)
        shotMap = {}
        for i in tableList[1:]:
            bslDieName = i[1]
            bslX = i[2]
            bslY = i[3]
            bslSite = i[4]
            smtDieName = i[8]
            smtX = i[9]
            smtY = i[10]
            smtSite = i[11]
            bslKey = bslDieName+bslX+bslY+bslSite
            shotMap[bslKey] = [smtDieName,smtX,smtY,smtSite]
        # [comment, die_name.replace("`", ""), die_x.strip(), die_y.strip(), site]
        for i in self.body_content:
            bslDieName = i[1]
            bslX = i[2]
            bslY = i[3]
            bslSite = i[4]
            bslKey = bslDieName + bslX + bslY + bslSite
            if bslKey in shotMap:
                i[1] = shotMap[bslKey][0]
                i[2] = shotMap[bslKey][1]
                i[3] = shotMap[bslKey][2]
                i[4] = shotMap[bslKey][3]
        return True


class getWafInfo_TSK(getWafInfo):

    def __init__(self, file, isSkip):
        super().__init__(file, isSkip)
        if not self.isWafSpec:
            return
        pitchx = self.attr_content[self.attr_value_label[1]][2]
        pitchy = self.attr_content[self.attr_value_label[2]][2]
        offsetx = self.attr_content[self.attr_value_label[10]][2]
        offsety = self.attr_content[self.attr_value_label[11]][2]
        coord = self.attr_content[self.attr_value_label[12]][2]
        newoffsetx = newoffsety = 0.0
        if coord == '1':
            newoffsetx = float(offsetx) - float(pitchx) / 2
            newoffsety = float(offsety) - float(pitchy) / 2
        elif coord == '2':
            newoffsetx = float(offsetx) - float(pitchx) / 2
            newoffsety = float(offsety) - float(pitchy) / 2
        elif coord == '3':
            newoffsetx = -float(offsetx) - float(pitchx) / 2
            newoffsety = float(offsety) - float(pitchy) / 2
        elif coord == '4':
            newoffsetx = float(offsetx) - float(pitchx) / 2
            newoffsety = -float(offsety) - float(pitchy) / 2

        self.attr_content[self.attr_value_label[10]][2] = '{:.6f}'.format(newoffsetx)
        self.attr_content[self.attr_value_label[11]][2] = '{:.6f}'.format(newoffsety)

        for it in self.body_content:
            die_x = -int(it[2]) + 128
            die_y = int(it[3]) + 128
            it[2] = '{}'.format(die_x)
            it[3] = '{}'.format(die_y)
