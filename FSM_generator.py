import sys
import pygraphviz as pgv


A=pgv.AGraph(directed=True,strict=True,encoding='UTF-8')
#A=pgv.AGraph(encoding='UTF-8')
A.add_edge('initial','msg',label='event.message.text')
A.add_edge('msg','help',label='determine text')
A.add_edge('help','instruction',label="reply")
A.add_edge('msg','other text',label='determine text')
A.add_edge('other text','same msg',label="reply")
A.add_edge('msg','eat_what',label='determine text')
A.add_edge('eat_what','restaurant',label='reply with random')
A.add_edge('instruction','initial',label='back')
A.add_edge('same msg','initial',label='back')
A.add_edge('restaurant','initial',label='back')
'''
中文會有亂碼，所以尚不採用
A.add_edge('吃什麼','煦悅',label="1")
A.add_edge('吃什麼','麥當勞',label="2")
A.add_edge('吃什麼','肯德基',label="3")
A.add_edge('吃什麼','大醬',label="4")
A.add_edge('吃什麼','鴨霸',label="5")
A.add_edge('吃什麼','牛伯',label="6")
A.add_edge('吃什麼','食方味',label="7")
A.add_edge('吃什麼','鹿耳晚晚',label="8")
A.add_edge('吃什麼','isaac吐司',label="9")
A.add_edge('吃什麼','十六咖哩',label="10")
A.add_edge('吃什麼','克林台包',label="11")
A.add_edge('吃什麼','subway',label="12")
A.add_edge('吃什麼','Au主廚_義大利麵',label="13")
A.add_edge('吃什麼','傑米廚房',label="14")
A.add_edge('吃什麼','億哥牛肉湯',label="15")
A.add_edge('吃什麼','小叉子',label="16")
A.add_edge('吃什麼','山大廚房',label="17")
A.add_edge('吃什麼',"八峰亭_拉麵",label="18")
'''
A.graph_attr['epsilon']='0.001'
print(A.string()) # print dot file to standard output
A.write('FSM.dot')
A.layout('dot') # layout with dot
A.draw('FSM.png') # write to file