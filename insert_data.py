'''
数据导入,数据导入是数据分析的开始
'''
#导入csv数据
import pandas as pda
i=pda.read_csv("C:/Users/Administrator/Desktop/dd.csv",encoding = 'gb18030') #如果encoding参数不加,可能会报错
#print(i.describe())

#根据某一列排序数据
i_sort = i.sort_values(by='price')
#i_comment_count = i.sort_values(by="comment_count")
print(i_sort)
#print(i_comment_count)


