# 在这个文件下编写代码，题目具体要求见README.md文件
weight=input()
if weight[-2:]=="kg":
  t=2.2046*eval(weight[0:2])
  print("对应的英制重量为{:.3f}磅".format(t))
elif weight[-2:]=="lb":
  m=eval(weight[0:2])/2.2046
  print("对应的公制重量为{:.3f}千克".format(m))
