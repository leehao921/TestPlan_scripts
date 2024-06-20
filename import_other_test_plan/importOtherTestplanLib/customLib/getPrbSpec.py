from .generalClass import getFileAttr
'''
Author  : chuiting.kong
Date    : 2023/12/05
Usage   : read prb
'''

class getPrbInfo:

    def __init__(self, file, isSkip=False):
        self.error = ''
        pin_map = {}
        for key in range(7, 19):
            value = 24 - (key - 7)
            pin_map[key] = value
        for key in range(31,44):
            value = key - 31
            pin_map[key] = value
        with open(file, 'r') as f:
            content = f.readlines()
        attr_content = []
        flag = True
        len_content = ''
        for it in content:
            if '$' in it and '-' not in it:
                attr_content.append(it.strip())
            if '$' in it and '-' in it and flag:
                flag = False
                len_content = it.strip()

        self.fileAttr = getFileAttr(line_content=attr_content).file_attr
        if self.fileAttr['Type'] != "Probe":
            self.isPrbSpec = False
            return
        else:
            self.isPrbSpec = True

        len_list = [len(item) for item in len_content.split(' ')]
        pos_list = []
        for i in range(len(len_list)):
            pos_list.append(sum(len_list[0:i]) + i * 1)
        self.body_content = []
        body_true = False
        for i in range(len(content)):
            content[i].replace('\n', '')
            if '$' in content[i] and body_true:
                break
            if 'BODY' in content[i]:
                body_true = True
                continue
            if body_true:
                comment = content[i][pos_list[0]:pos_list[0] + len_list[0]].replace(' ', '')
                pad_pin = content[i][pos_list[2]:pos_list[2] + len_list[2]]
                if len(pad_pin.split(',')) < 2: continue
                pad, pin = pad_pin.split(',')
                # ['Select', 'PadNumber', 'PinNumber', 'Comment']
                module_item = [comment, pad, pin, '']
                if not isSkip or comment != "#":
                    self.body_content.append(module_item)

        pass

