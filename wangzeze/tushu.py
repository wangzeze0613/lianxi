# -*- coding: utf-8 -*-

bookcase={'《大学》':11,'《中庸》':12,'《论语》':13,'《孟子》':14}

book_key=list(bookcase.keys())

book_values=list(bookcase.values())

user=int(input(r'''"***********选择列表**************"

    "1、查看当前的所有图书列表"

    "2、查询某本图书的书架位置"

    "3、更改图书书架编号"

    "4、删除某本图书"

    "5、增加图书"

    "0、退出"

    "请输入您要操作的编号："'''))

if user == 1:

  for i in book_key:

    print(i)

elif user == 2:

  book_name=input(r'''

        "请输入书名："''')

  if book_name in book_key:

     print("您查找的%s在书架%d上" % (book_name,bookcase[book_name]))

  else:

     print("查无此书")

elif user == 3:

  book_name2=input(r'''

        "请输入需要修改的书名："''')

  if book_name2 not in book_key:

     print("查无此书")

  elif book_name2 in book_key:

     shujia=int(input(r'''

        "请输入所修改图书新的书架："'''))

     if shujia in book_values:

        print("书架已被占用")

     else:

        bookcase[book_name2]=shujia

        print(bookcase['《大学》'])

elif user == 4:

  book_name3=input(r'''

        "请输入书名："''')

  if book_name3 in book_key:

    bookcase.pop(book_name3)

    print(bookcase)

  else:

    print("查无此书")

elif user == 5:

  book_name4=input(r'''

        "请输入书名："''')

  if book_name4 in book_key:

    print("已有此书")

  else:

    shujia1=int(input(r'''

        "请输入书架：”'''))

    if shujia1 in book_values:

      print("书架被占用")

    else:

      bookcase[book_name4]=shujia1

      print(bookcase)

elif user == 0:

  print("谢谢使用，再见")

else:

  print(r'''

        "输入有误，终止程序"''')