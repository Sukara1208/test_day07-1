from config import BASE_DIR


def read_txt(filename):
    result = []
    # with open("../data/"+filename,"r",encoding="utf-8") as f:
    with open(BASE_DIR+"/./data/"+filename,"r",encoding="utf-8") as f:
        # return f.readlines()
        for d in f.readlines():
            result.append(tuple(d.strip().split(",")))
        return result[1::]


if __name__ == '__main__':
    print(read_txt('employee_data.txt'))
    print("--" * 50)
    # arr = []
    # for data in read_txt("employee_data.txt"):
    #     arr.append(tuple(data.strip().split(",")))
    # print(arr[1::])

    """
        strip: 去除字符串前后空格、换行符
        split("字符"): 以指定字符分隔字符串，并 以列表的形式返回
    """
