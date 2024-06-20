from .generalClass import getFileAttr

'''
Author  : jianghao.zheng
Date    : 2023/7/19
Usage   :get die spec
'''


class getDieInfo:

    def __init__(self, file,isSkip = False):
        with open(file, 'r') as f:
            content = f.readlines()
        attr_content = []
        flag = True
        len_content = ''
        for it in content:
            if '$' in it and '-' not in it:
                attr_content.append(it.strip())
            if '$-' in it and flag:
                flag = False
                len_content = it.strip()

        self.fileAttr = getFileAttr(line_content=attr_content).file_attr
        if self.fileAttr['Type'] != "Die":
            self.isDieSpec = False
            return
        else:
            self.isDieSpec = True

        len_list = [len(item) for item in len_content.split(' ')]
        pos_list = []
        for i in range(len(len_list)):
            pos_list.append(sum(len_list[0:i]) + i * 1)
        self.body_content = []
        body_true = False
        for i in range(len(content)):
            content[i] = content[i].replace('\n', '')
            if '$' in content[i] and body_true:
                break
            if 'BODY' in content[i]:
                body_true = True
                continue
            if body_true:
                comment = content[i][pos_list[0]:pos_list[0] + len_list[0]].replace(' ', '')
                module_name = content[i][pos_list[1]:pos_list[1] + len_list[1]].replace(' ', '').replace("`", "").replace("'","")
                die_x_y = content[i][pos_list[2]:pos_list[2] + len_list[2]]
                site = ''
                if not die_x_y :continue
                die_x, die_y = die_x_y.split(',')
                module_item = [comment, module_name, die_x.strip(), die_y.strip(), site]
                if not isSkip or comment != "#":
                    self.body_content.append(module_item)

        pass

    def getAllModules(self):
        res = []
        for item in self.body_content:
            comment = item[0]
            module = item[1]
            if comment != '#' and module not in res:
                res.append(module)
        return res


if __name__ == '__main__':
    die = getDieInfo(r'D:\Users\jianghao.zheng\Desktop\客户汇总\Linux重构\0145\0145.die')
    pass
