"""
1、列表 ：增删改查
2. 元组： 元组是不可变的，可以通过解包、索引来访问
3. 集合是由不重复元素组成的无序的集，它的基本用法包括成员检测和消除重复元素
4. 字典是Python中唯一的内置映射类型，键可能是数、字符串或者元组. 可通过键进行增删改查
5. 栈(stack)： 后进先出： 浏览器的后退
6. 队列(queue)： 先进先出： 排队和浏览器的前进
7. 堆(heap)： 排序满二叉树，常用的有最小堆和最大堆，可以快速的查找top k;
8. 树（tree）:
"""
import heapq
from collections import deque


def testStack():
    stack = [3, 4, 5]
    stack.append(6)
    stack.append(7)
    print(stack)
    print("pop", stack.pop())
    print(stack)


testStack()

'''
也可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；但是拿列表用作这样的目的效率不高。
在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快
'''


def testQueue():
    queue = deque(["Eric", "John", "Michael"])
    queue.append("Terry")
    queue.append("Graham")
    print(queue)
    print("popleft:", queue.popleft())
    print(queue)


testQueue()


def testHeap():
    l = [1, 12, 10, 4]
    # 最小堆排序list
    heapq.heapify(l)
    print(l)
    # 将-1添加到堆中
    heapq.heappush(l, -1)
    print(l)
    # 弹出最小值
    min = heapq.heappop(l)
    print("min:", min)
    print(l)


testHeap()

from treelib import Tree, Node

print("---- 测试树 ----")


def testNode(node):
    print('node id: ', node.identifier)
    print('node tag:', node.tag)
    print('node data:', node.data)

    print('node is leaf: ', node.is_leaf())
    print('node is root: ', node.is_root())


def testTree():
    tree = Tree()
    tree.show()
    print(tree.identifier)

    # 添加节点
    tree.create_node(tag='Node-5', identifier='node-5', data=5)
    tree.create_node(tag='Node-10', identifier='node-10', parent='node-5', data=10)
    tree.create_node('Node-15', 'node-15', 'node-10', 15)
    tree.show()

    node = Node(data=50)
    tree.add_node(node, parent='node-5')
    node_a = Node(tag='Node-A', identifier='node-A', data='A')
    tree.add_node(node_a, parent='node-5')
    tree.show()
    print('tree len: ', len(tree))
    print('tree size:', tree.size())
    tree.create_node(tag='Node-20', identifier='node-20', parent='node-10', data=20)
    tree.create_node(tag='Node-30', identifier='node-30', parent='node-15', data=30)
    print('tree size:', tree.size())
    '''
    children(nid): 传入节点id，返回节点的所有子节点，返回结果是一个节点列表，如果没有子节点则返回空列表。
    is_branch(nid): 传入节点id，返回节点的所有子节点id，返回结果是一个列表，如果没有子节点则返回空列表。
    siblings(nid): 传入节点id，返回节点的所有兄弟节点，返回结果是一个节点列表，如果没有兄弟节点则返回空列表。
    parent(nid): 传入节点id，返回节点的父节点，如果传入的是根节点，则返回None。
    ancestor(nid, level=None): 传入节点id，返回节点的一个祖先节点，如果指定level则返回level层的祖先节点，如果不指定level则返回父节点，如果指定level比节点的层数大，则报错。
    is_ancestor(ancestor, grandchild): 传入两个节点id，判断ancestor是不是grandchild的祖先，返回布尔值。
    rsearch(nid, filter=None): 传入节点id，遍历节点到根节点的路径上的所有节点id，包含该节点和根节点，返回结果是一个生成器。可以传入过滤条件对结果进行过滤。
    '''
    children = tree.children('node-5')
    print('node-5 children:', children)
    branch = tree.is_branch('node-10')
    print('node-10 branch:', branch)
    print('node-20 siblings:', tree.siblings('node-20'))
    print('node-30 parent:', tree.parent('node-30'))
    print('node-15 ancestor: ', tree.ancestor('node-15'))
    print(tree.is_ancestor('node-15', 'node-30'))
    for node in tree.rsearch('node-30'):
        print(node)
    print('tree depth:', tree.depth())
    print('node-20 depth:', tree.depth(node='node-20'))
    print('node-20 level:', tree.level('node-20'))
    print('tree leaves:', tree.leaves())
    # 树遍历
    # all_nodes(): 返回多叉树中的所有节点，返回结果是一个节点对象构成的列表，节点的顺序是添加到树中的顺序
    # all_nodes_itr(): 返回多叉树中的所有节点，返回结果是一个迭代器，节点的顺序是添加到树中的顺序。
    # expand_tree(): 返回多叉树中的所有节点id，返回结果是一个生成器，顺序是按深度优先遍历的顺序。可以传入过滤条件等参数来改变返回的生成器。
    nodes = tree.all_nodes()
    print(nodes)
    for node in tree.all_nodes_itr():
        print(node)
    for id in tree.expand_tree():
        print(id)
    '''
    contains(nid): 传入节点id，判断节点是否在树中，返回布尔值。
    get_node(nid): 传入节点id，从树中获取节点，返回节点对象，如果传入的节点id不在树中则返回None。
    update_node(nid, **attrs): 传入节点id，修改节点的属性值，需要修改哪个参数就用关键字参数的方式传入，可以传入0个或多个属性。
    move_node(source, destination): 传入两个节点id，将source节点移动成为destination节点的子节点。如果节点id不在树中则报错。
    '''
    print('node-10 is in tree:', tree.contains('node-10'))
    print('node-100 is in tree:', tree.contains('node-100'))
    print(tree.get_node('node-10'))
    print(tree.get_node('node-100'))
    tree.update_node('node-20', data=200)
    print('data of node-20:', tree.get_node('node-20').data)
    tree.move_node('node-30', 'node-20')

    testNode(node)


testTree()
