#打开文件test1source.txt，并存入data缓冲区
With open('C:/Users/A/Desktop/dataa/test1source.txt','r') as f:
     data=f.read()
#从键盘中输入到x缓冲区
#x=input('some chars')
#print(x)
#将data中数据的空格替换为‘#’，并存入data1中
data1=data.replace(' ','#')
#将data1中数据的空格替换为‘#’，并存入data2中
data2=data1.replace('\n','#')
#输出data2查看结果
print(data2)
