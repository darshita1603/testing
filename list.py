# my_list= [1,2]
# print(my_list[0])

# list2=[1,2,"a",[1,2,3]]
# print(list2[3][1])

# # add list into list

# a=[1,2,2]
# b=[a+[3,5,7]]
# print(b)

# dic={}
# dic["key1"]=[1,2,3]
# new_list=[1,2,3]
# dic["key1"].append(new_list)
# print(dic)

# random=[1,2,('a','b'),('a','b')]
# count=random.count(('a','b'))
# print(count)

# l1=[1,2,3]
# print(l1)
# l1.reverse() #[::-1]
# print(l1)

# #reversed loop create
# for i in reversed(l1):
#     print(i)


# l2= [5, 6, [], 3, [], [], 9]
# for l in range(len(l2)):
#     print(l)

# ls2=[5, 6, [], 3, [], [], 9]
# ls3=[i for i in ls2 if i!=[]]
# print(ls3)

# for i in ls2:
# 	if type(i) is list:
#          ls2.remove(i)
# print(ls2)

# l3=[1,2,[3,4,5],[[6],[[[7,[None]],[8,9]]]]]
# l4=[]

# def reemovNestings(i):
#   for i in l3:
#       if type(i)==list:
#         reemovNestings(i)
#       else:
#         l4.append(i)

# print ('The original list: ', l3)
# reemovNestings(l3)
# print ('The list after removing nesting: ', l)

# def nestedlist(i):
#     for i in l3:
#         if isinstance(i,list):
#             nestedlist(i)
#         else:
#             l4.append(i)

# nestedlist(l3)
# print(l4)

l1 = [1,2,[3,4,5],[[6],[[[7,[None]],[8,9]]]]]

l2=[]

def r(ls):
	for i in ls:
		if isinstance(i,list):
			r(i)
		else:
			l2.append(i)

r(l1)
print(l2)