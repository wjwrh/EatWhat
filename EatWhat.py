from random import Random
from data import data

r = Random()


if __name__ == '__main__':
    print ("请在下面选择你所需要的分类:")
    KeyList = list(data.keys())
    for key in KeyList:
        print(str(KeyList.index(key)) + ': ' + key)
    
    while True:
        try:
            Choice = int(input('请输入你所选的分类前面的编号: '))
            item = data[KeyList[Choice]]
        except:
            print('输入错误！请重新输入')
            continue
        else:
            break

    print('分类"' + KeyList[Choice] + '"下的食物有:')
    for food in item:
        print(food ,end = ' ')
    print('\n随机抽取的结果为:\n' + r.choice(item))
    
