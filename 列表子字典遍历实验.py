test = [{'id': '1', 'name': 'q', 'tel': '11'},{'id': '2', 'name': 'qq', 'tel': '111'}]
for i in test:
    print(i['id'])   #遍历列表子dict后根据k找v。

    if 'qq' == i['name']:    #匹配子字典，v匹配k
        print(f"id是：{i['id']}")
        test.remove(i)
        print(test)         # 结果 [{'id': '2', 'name': 'qq', 'tel': '111'}]  #匹配到的子dict被删了