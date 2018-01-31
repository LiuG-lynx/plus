class List(list):  # 取中间值
    def  show_middle(self):
        mid_index = int(len(self)/2)
        return self[mid_index]

l1 = List('Hello!word')
print(l1, type(l1))
print(l1.show_middle())


l2 = list('hello!word')
print(l2, type(l2))
