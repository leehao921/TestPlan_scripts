import os
from .generalClass import getFileAttr,MapingTable,getLimInfo

'''
Author  : chuiting.kong
Date    : 2023/12/05
Usage   : get TestSpec Info for ZXGJ-BJJC
'''


class getTestSpec:
    def __init__(self, tst_file, map_file, lim_file, template_file,skip):
        self.isTstSpec = None
        self.fileAttr = None
        self.err = ''
        self.isSkip = skip
        # line_content = ['Select', 'Module', 'Device','Group', 'Algorithm','Input','Pad','Output','Limit','Comment']
        self.body_content = []
        self.outputMap = getLimInfo(lim_file)
        self.mapTable = MapingTable(map_file,template_file)
        self.err =  self.mapTable.err
        if self.err:
            return
        self._moduleList = []
        self.getContent(tst_file)
        self.sort()
        if len(self.body_content) == 0:
            self.err = 'No valid items, may be all skiped.'

    def sort(self):
        # module: AABDCBABDC -> AAABBBDDCC
        newList = []
        # line_content = ['Select' 0, 'Module' 1, 'Device' 2,'Group' 3, 'Algorithm' 4,'Input' 5,'Pad','Output' 7,'Limit','Comment']
        for mod in self._moduleList:
            newList.extend([i for i in self.body_content if i[1] == mod])
        self.body_content = newList

    def getContent(self, file):
        if file == '' or not os.path.exists(file):
            return False, 'Tst file is not exist !'
        with open(file, 'r') as f:
            content = f.readlines()
        #  for attribute
        attr_content = []
        len_content = ''
        for it in content:
            if '$' in it and '-' not in it:
                attr_content.append(it.strip())
            if '$-' in it:
                len_content = it.strip()
                break
        self.fileAttr = getFileAttr(line_content=attr_content).file_attr
        if self.fileAttr['Type'] != "Test":
            self.isTstSpec = False
            self.err = "This is not a test spec file or it is empty !"
            return
        else:
            self.isTstSpec = True
        values = len_content.split(' ')
        pos1 = 1
        len1 = len(values[0]) - 1
        pos2 = pos1 + len1 + 1
        len2 = len(values[1])
        pos3 = pos2 + len2 + 1
        len3 = len(values[2])
        pos4 = pos3 + len3 + 1
        len4 = len(values[3])
        pos5 = pos4 + len4 + 1
        len5 = len(values[4])

        v0 = v1 = v2 = v3 = v4 = v5 = ''
        module = device = algo = inputs = output = selected = comment = ''

        # body
        body_true = False
        for i in range(len(content)):
            tmp = content[i].replace('\r', '').replace('\n','')
            if '$' in content[i] and body_true:
                break
            if 'BODY' in content[i]:
                body_true = True
                continue
            if not body_true:
                continue

            # 跳过空行
            wxs_line = tmp
            wxs_line = wxs_line.replace(" ", "")
            if wxs_line == "":
                continue
            s = tmp
            v0 = s[0]
            if v0 == '#' and self.isSkip:continue

            v1 = s[pos1:pos1 + len1]
            if '::' in v1:
                v1 = v1.replace(" ", "")
                v1 = v1.replace("`", "")
                module = v1[:v1.index('::')]
                device = ''
                v1 = v1[v1.index('::')+2:]
            if ':' in v1:
                v1 = v1.replace(" ", "")
                v1 = v1.replace("`", "")
                device = v1[:v1.index(':')]
            v2 = s[pos2:pos2 + len2]
            v2 = v2.replace(" ", "")
            if v2 != "" :
                algo = v2
            else:
                continue
            v3 = s[pos3:pos3 + len3]
            v3 = v3.replace(" ", "").replace('`','')

            tmp_v3 = v3
            if "R[" in v3:
                count = 0
                while True:
                    startpos = tmp_v3.find("R[") + 2
                    endpos = tmp_v3.find("]") - 1
                    if startpos == 1 or endpos == -2:break
                    outcode = tmp_v3[startpos: startpos + endpos - startpos + 1]
                    tmp = "R[" + outcode + "]"
                    if outcode in self.outputMap:
                        v3 = v3.replace(tmp, self.outputMap[outcode])
                    tmp_v3 = tmp_v3[endpos + 2:]
                    count += endpos
            # 若Input列最后以“，”结尾，删掉“，”.
            if len(v3) >= 1 and v3[-1] == ',':
                v3 = v3[:-1]
            # PadNumber拼接到Input列中
            v5 = s[pos5:pos5 + len5]
            v5 = v5.replace(" ", "")
            if v3 != "" and v5 != "":
                inputs = v3 + "," + v5
            elif v3 != "" and v5 == "":
                inputs = v3
            elif v3 == "" and v5 != "":
                inputs = v5
            v3 = inputs
            v4 = s[pos4:pos4 + len4]
            v4 = v4.replace(" ", "")
            v4 = v4.replace("`", "")
            if "R[" in v4:
                tmp_v4 = v4
                count = 0
                while True:
                    startpos = tmp_v4.find("R[") + 2
                    endpos = tmp_v4.find("]") - 1
                    # count += endpos;
                    if startpos == 1 or endpos == -2:break
                    else:
                        outcode = tmp_v4[startpos:endpos + 1]
                        tmp = "R[" + outcode + "]"
                        if outcode in self.outputMap:
                            v4 = v4.replace(tmp, self.outputMap[outcode])
                        tmp_v4 = tmp_v4[endpos + 2:]
                        count += endpos
            output = v4
            selected = v0
            # line_content = ['Select', 'Module', 'Device','Group', 'Algorithm','Input','Pad','Output','Limit','Comment']
            line_content = [selected, module, device,'', algo, v3, '', output, '', '']
            self.mapTable.convert(line_content)
            self.body_content.append(line_content)
            if module not in self._moduleList: self._moduleList.append(module)
