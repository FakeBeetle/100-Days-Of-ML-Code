import copy as cp
l1 = [3,9,'223',4,['555'],2,7,8,6,0]
#l2 = l1#同一个地址
#l2 = l1.copy()#复制一份item所指的地址表，在修改元素时，修改的是地址表所指元素的data；
l2 = cp.deepcopy(l1)#deepcopy也复制一张地址表，但在修改元素时，直接修改表中地址，呈现出与原表无关的效果

l2[4][0] ='SSS'
print('l1: ',id(l1),id(l1[2]),l1)
print('l2: ',id(l2),id(l2[2]),l2)