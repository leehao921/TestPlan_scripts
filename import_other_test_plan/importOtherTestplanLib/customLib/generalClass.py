import csv
from typing import Dict, List

'''
Author  : chuiting.kong
Date    : 2023/12/05
Usage   : Lim , map object class for ZXGJ-BJBF
'''


def getLimInfo(file):
    ID_Map = {}
    if file == '':
        return ID_Map
    with open(file, 'r') as f:
        for line in f:
            items = line.split(' ')
            items = list(filter(None, items))
            if len(items) > 2:
                ID = items[0]
                Output = items[1]
                ID_Map[ID] = Output
            else:
                continue
    return ID_Map

class Template:
    def __init__(self, file):
        self.err = ''
        self.item_list = []
        if file == '':
            return
        with open(file, 'r', encoding='utf-8') as f:
            lines:List[List[str]] = list(csv.reader(f))
        # select module, device, group, algo, input, padnumber, output, limit, comment;
        self.item_list = lines[1:]

class MapingTable:
    class algoItem:
        def __init__(self,newAlgo = '',group = '',special = '',tmplate = ''):
            self.newAlgo = newAlgo
            # {oldInput:newInput}
            self.inputMap = {}
            self.group = group
            self.specialAlgo = special
            self.templateInut = tmplate

    def __init__(self,mapFile,templateFile):
        self.err = ''
        self._mapfile = mapFile
        self._template = Template(templateFile)
        # {oldAlgoName:algoItem}
        self._table:Dict[str,MapingTable.algoItem] = {}
        self.newAlgoToOldAlgo = {}
        self._read()

    # line_content = ['Select' 0, 'Module' 1, 'Device' 2,'Group' 3, 'Algorithm' 4,'Input' 5,'Pad','Output' 7,'Limit','Comment']
    def convert(self,bslItem:List[str]):
        if bslItem[4] not in self._table:
            return True
        algoCell = self._table[bslItem[4]]
        bslItem[4] = algoCell.newAlgo
        bslItem[3] = algoCell.group
        inputList = bslItem[5].split(',')
        inputNameList = []
        for i in inputList:
            tmp = i.split('=')
            if len(tmp) != 2:
                inputNameList.append(tmp)
                continue
            name = tmp[0]
            inputNameList.append(name)
            if name in algoCell.inputMap:
                inputList[inputList.index(i)] = algoCell.inputMap[name]+'='+tmp[1]
        addInputList = [x for x in algoCell.templateInut.split('/') if x]
        for addInput in addInputList:
            if addInput in inputNameList:continue
            # [select 0 module 1, device 2, group 3, algo 4, input 5, padnumber 6, output 7, limit 8, comment 9]
            for tempItem in self._template.item_list:
                if algoCell.specialAlgo == 'yes' and tempItem[4] == algoCell.newAlgo and tempItem[2] == bslItem[2] and addInput+'=' in tempItem[5]:
                    _name = addInput+'='
                    if tempItem[5].find(_name) == -1: continue
                    beg = tempItem[5].index(_name)+len(_name)
                    _val = tempItem[5][beg:]
                    if ',' in _val: _val = _val[:_val.index(',')]
                    inputList.append(_name+_val)
                    bslItem[3] = tempItem[3]
                    break
                elif algoCell.specialAlgo != 'yes' and tempItem[4] == algoCell.newAlgo and addInput+'=' in tempItem[5]:
                    bslOutList = bslItem[7].split(',')
                    tmplateOutList = tempItem[7].split(',')
                    for oneOut in bslOutList:
                        if oneOut not in tmplateOutList:continue
                        _name = addInput + '='
                        if tempItem[5].find(_name) == -1: continue
                        beg = tempItem[5].index(_name) + len(_name)
                        _val = tempItem[5][beg:]
                        if ',' in _val: _val = _val[:_val.index(',')]
                        inputList.append(_name + _val)
                        bslItem[3] = tempItem[3]
                        break
        bslItem[5] = ','.join(inputList)

    def _read(self):
        if self._mapfile == '':
            return True
        with open(self._mapfile, 'r') as f:
            lines:List[List[str]] = list(csv.reader(f))
        if len(lines) < 1: return True
        if not self._checkTitle(lines[0]):
            return False
        curOldAlgo = ''
        for line in lines[1:]:
            items = line
            if len(items) < 7:continue
            if items[0] :
                curOldAlgo = items[0]
                if curOldAlgo not in self._table:
                    if not items[1]:
                        items[1] = curOldAlgo
                    if items[4] == 'yes':
                        items[4] = items[1]
                    self._table[curOldAlgo] = MapingTable.algoItem(items[1],items[4],items[5],items[6])
                    self.newAlgoToOldAlgo[items[1]] = curOldAlgo
            if items[2] and items[3]:
                self._table[curOldAlgo].inputMap[items[2]] = items[3]
        return True

    def _checkTitle(self,titleList):
        items = titleList
        _allTitleList = ['OldAlgoName', 'NewAlgoName','OldInput', 'NewInput', 'Group', 'Special_Algo', 'Template_Algo_Input']
        for i in range(len(items)):
            if items[i] != _allTitleList[i]:
                self.err = f'Column \'{i}\' is not \'{_allTitleList[i]}\' in mapping file \n\'{self._mapfile}\'\n'
                return False
        return True

class getFileAttr:
    def __init__(self, line_content=None):
        if line_content is None:
            line_content = []
        self.file_attr = {
            'Type': '',
            'Name': '',
            'Vers': '',
            'Desc': '',
            'Date': '',
            'Time': '',
            'User': ''
        }
        for it in line_content:
            it = it.strip('$').strip()
            line_list = it.split(':',1)
            if line_list[0] in self.file_attr.keys():
                self.file_attr[line_list[0]] = line_list[1].strip()