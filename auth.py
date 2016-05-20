#coding=utf8
import xlrd, xlwt, pinyin, hashlib
from datetime import datetime


sql_pattern = 'insert into tb_user(uid, phone, password, complete, created, login_count) values("%s", "%s", "%s", %s, "%s", %s);\n'
ur_pattern = 'insert into tb_user_role(uid, role, auth) values("%s", "%s", %s);\n'


sql_file = open('auth.sql', 'a+')



filename = xlwt.Workbook(encoding='utf-8')
sheet = filename.add_sheet('data')
sheet.write(0, 0, "全称")
sheet.write(0, 1, "简称")
sheet.write(0, 2, "地址")
sheet.write(0, 3, "帐户名")
sheet.write(0, 4, "密码")


data = xlrd.open_workbook('auth.xlsx')
table = data.sheet_by_index(0)
rows = table.nrows
for i in xrange(0, rows):
    row = table.row_values(i)
    name = row[0]
    place = row[1]
    short_name = row[2]
    uname = pinyin.get(short_name)
    password = uname + '888'

    cnt = i + 1
    sheet.write(cnt, 0, name)
    sheet.write(cnt, 1, short_name)
    sheet.write(cnt, 2, place)
    sheet.write(cnt, 3, uname)
    sheet.write(cnt, 4, password)

    s = hashlib.sha1()
    s.update(uname)
    uid = s.hexdigest()

    s1 = hashlib.md5()
    s1.update(password)
    password = s1.hexdigest()

    sql_file.write(sql_pattern%(uid, uname, password, '1', str(datetime.now()), '1'))
    sql_file.write(ur_pattern%(uid, '企业HR', '1'))
    '4bd6 7a0c d9b0 1906 1180 2d9a 08ec fa91 26fe aae4'
    '96e7 9218 965e b72c 92a5 49dd 5a33 0112'


filename.save('./auth_new.xlsx')
