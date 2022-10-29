
# # using read mode
# f=open("text1_document.txt",mode="r")
# f.seek(3)
# print(f.tell())
# print(f.read())
# print(f.readline())
# f.close()
#
# # using write mode
# f1=open("text1_document.txt",mode="a")
# f1.writelines("hii")
# f1.writelines("hello")
# f1.writelines("welcome")
# f1.writelines("to python")
# f1.close()
# #
# f2=open("text1_document.txt",mode='r')
# print(f2.read())
# f2.close()

#
# f3=open("newtext.txt","x")
# f3.close()

# f4=open("newtext.txt","w")
# f4.writelines("hellllooo helllooo")
# f4.writelines("hiiiiii hiiiii")
# f4.close()
# #

# f7=open("newtext.txt","w")

# for remove file
# import os
# os.remove("newtext.txt")
# import os
# if os.path.exists("newtext.txt"):
#     os.remove("newtext.txt")  #os.rmdir() empty file remove
# else:
#     print("there is no such file")
#


