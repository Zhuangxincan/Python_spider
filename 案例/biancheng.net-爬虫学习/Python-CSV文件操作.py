import csv
# ------CSV文件写入-------------
# 1.csv.writer()
# writer(csvfile, dialect='excel', **fmtparams)
# 参数说明：
# csvfile：必须是支持迭代(Iterator)的对象，可以是文件(file)对象或者列表(list)对象。
# dialect：编码风格，默认为 excel 的风格，也就是使用逗号,分隔。
# fmtparam：格式化参数，用来覆盖之前 dialect 对象指定的编码风格。
# 操作文件对象时，需要添加newline参数逐行写入，否则会出现空行
'''
# # 1.1当行写入
with open('eggs.csv','w',newline='') as csvfile:
    # delimiter 指定分隔符，默认为逗号，这里指定为空格
    # quotechar 表示引用符,当一段话中出现分隔符的时候，用引用符将这句话括起来，以能排除歧义。
    # writerow 单行写入，列表格式传入数据
    spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|')
    spamwriter.writerow(['www.biancheng.net'] * 5 + ['how are you'])
    spamwriter.writerow(['hello world', 'web site', 'www.biancheng.net'])
# # 1.2多行写入
with open('aggs.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    # 注意传入数据的格式为列表元组格式
    writer.writerows([('hello','world'), ('I','love','you')])

# 2.csv.DictWriter()
with open('names.csv','w',newline='') as csvfile:
    #构建字段名称，key
    fieldnames = ['first_name','last_name']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    #写入字段名当作表头
    writer.writeheader()
    #多行写入
    writer.writerows([{'first_name': 'Baked', 'last_name': 'Beans'},
                      {'first_name': 'Lovely', 'last_name': 'Spam'}])
    # 单行写入
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
'''
# ------CSV文件读取-------------
# 2.1csv.reader()
with open('eggs.csv','r',newline='') as csvfile:
    spamreader = csv.reader(csvfile,delimiter=' ',quotechar = '|')
    for row in spamreader:
        print(','.join(row))
# 2.2csv.DictReader
with open('names.csv','r',newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first_name'],row['last_name'])