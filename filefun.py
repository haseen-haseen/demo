# f=open("exampletxt",'a')
# f=open("exampletxt",'w')
# f=open("exampletxt",'rb')

# txt=f.read()
# # txt=f.write(" yuppp")
# print(txt)
# f.close()
# with open("exampletxt",'a') as f:
#  f.write("heeeyyyy")
# r=open("exampletxt",'r')
# i=0
# while True:
#  i=i+1
#  text=r.readline()
#  if not text :
#   break
#  m1=text.split(",")[0]
#  m2=text.split(",")[1]
#  m3=text.split(",")[2]



#  print(f"stud marks{i} {m1}")
#  print(f"stud marks{i} {m2}")
#  print(f"stud marks{i} {m3}")

# with open("exampletxt",'w') as f:
#     i=0
#     line=["1\n","2\n","3\n"]
#     for i in line:
      
#       f.writelines(i)

# with open("exampletxt",'r') as f:
#      f.seek(10)
#      print(f.tell())
#      print(f.read(5))

with open("exampletxt",'w') as f:
     f.write("shineji")
     f.truncate(5)
