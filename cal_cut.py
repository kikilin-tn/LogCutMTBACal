import datetime
cnt = 0
logs = []

filename = input('please input the file name: ')
with open(filename, 'r') as f:

    start_date = datetime.datetime(2019,5,20,0,0,0)
    end_date = datetime.datetime(2019,5,25,0,0,0)

    for line in f:
        details =  line.split('\t')
        if len(details) < 3:
            continue
        log_date_str = details[0]
        log_type = details[1]
        log_date = datetime.datetime.strptime(log_date_str,'%Y/%m/%d %H:%M:%S')
        if log_date >= start_date and log_date <= end_date and log_type == 'CUT':
            logs.append(line)
    print('指定期間內的切割片數為: ' + str(len(logs)))

"""
print(log_date) #2019-05-20 00:08:04
print(start_date) #2019-05-20 00:00:00
print(type(log_date)) #<class 'datetime.datetime'>
"""
#str.find(str, beg=0, end=len(string))
#str -- 指定检索的字符串
#beg -- 开始索引，默认为0。
#end -- 结束索引，默认为字符串的长度。
#如果包含子字符串返回开始的索引值，否则返回-1。
"""
str1 = "2019/05/30 09:39:09	KC	99,OK CH4:Line=7,1635960545,467,-15,95,311,-10,YES"
str2 = "KC\t"
str3 = "2019"
str4 = "OK"

#str.find(str, beg=0, end=len(string))
print (str1.find(str2)) #20
print (str1.find(str3)) #0
print (str1.find(str4)) #26
"""
