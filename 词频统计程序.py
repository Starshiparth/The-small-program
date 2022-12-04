import re

'矮睿科技版权认证号：P558283908-001'
'No.1'
text = input('请输入一篇文章，我们将进行词频统计，切记，文章需要统计的点开头用！文章！标示，结尾用？文章？进行标示。谢谢你的配合！')
text = re.findall('！文章！(.*?)？文章？', text, re.S)
list_text = text[0]
text_list = list(list_text)

'No.2'
dicta = {}
for ca in range(0, len(text_list)-1):
    if text_list[ca] not in dicta.keys():
        dicta[list_text[ca]] = 0
    elif text_list[ca] in dicta.keys():
        pass
if text_list[-1] not in dicta.keys():
    dicta[list_text[-1]] = 0
elif text_list[-1] in dicta.keys():
    pass
for a in range(0, len(text_list)-1):
    dicta[list_text[a]] = dicta[list_text[a]]+1
dicta[list_text[-1]] = dicta[list_text[-1]]+1
print('完成（没有排序的）（自行排序吧hhh）')
print(dicta)