import openpyxl


class Case:  # 这个类储存测试用列
    __slots__ = []  # 特殊类属性，可以用来限制这个类创建的实例属性添加，可写不可写。
    pass


class ReadExcel(object):
    '''按行读取数据，储存在列表中。'''
    def __init__(self, file_name, sheet_name):
        '''
        初始化读取对象
        :param file_name:文件名-->str类型
        :param sheet_name:表单名-->str类型
        '''
        # 打开文件
        self.work_book = openpyxl.load_workbook(file_name)
        # 选择表单
        self.sheet = self.work_book[sheet_name]

    def read_data_line(self):
        # 按行读取数据转换为列表
        rows_data = list(self.sheet.rows)
        print(rows_data)
        # 获取表单的表头信息
        titles = []
        for titles in rows_data[0]:
            titles.append(titles.value)
        print(titles)
        # 定义一个空的列表，用于储存测试用例数据
        cases = []
        for case in rows_data[1:]:
            print(case)
            data = []
            for cell in case:
                print(cell.value)
                data.append(cell.value)
                # 判断该单元格是否为字符串，如果是字符串类型则需要使用eval();如果不是字符串类型则不需要使用eval()
                if isinstance(cell.value, str):
                    data.append(eval(cell.value))
                else:
                    data.append(cell.value)
                    # 讲该数据存放至cases中
                    case_data = dict(list(zip(titles, data)))
                    cases.append(case_data)

        return cases
