# print("Hello, Python");

# if True:
#     print("true");
#     print("hello");
# else:
#     print("false");

# a = input("\n\nplass input:");
# print("input --->  "+a);

# a = b = c = 1;
# print(a);
# print(b);
# print(c);

# a, b, c = 1, 4, "hadoop"; 
# print(a);
# print(b);
# print(c);


# vara = 1;
# varb = 2;
# varc = varb;
# print (vara);
# print (varb);
# print (varc);
# del varc;
# print (vara);
# print (varb);
# print (varc);

# print("---字符串---");
# str1 = "Hello World!";
# print(str1);
# print(str1[0]);
# print(str1[2:4]);
# print(str1[2:]);
# print(str1 * 2);
# print(str1 + "TEST");

# print("---列表(数组)---");
# List = ["abcd", 789, 2.23, "hadoop", 70.2];
# tinylist = [113, "hadoop"];
# print(List);
# print(List[0]);
# print(List[1:3]);
# print(List[2:]);
# print(tinylist * 2);
# print(List + tinylist);

# print ("-------元组---------");
# Tuple = ("abcd", 786, 2.23, "john", 70.2)
# tinytuple = (123, "john")

# print (Tuple);  # 输出完整元组
# print (Tuple[0]);  # 输出列表的第一个元素
# print (Tuple[1:3]);  # 输出第二个至第三个的元素
# print (Tuple[2:]);  # 输出从第三个开始至列表末尾的所有元素
# print (tinytuple * 2);  # 输出元组两次
# print (Tuple + tinytuple);  # 打印组合的元组

# print ("-------元组不允许更新 , 但是列表允许---------");
# Tuple = ( "abcd", 786 , 2.23, "john", 70.2 )
# List = [ "abcd", 786 , 2.23, "john", 70.2 ]
# # Tuple[2] = 1000 # 错误！元组中是非法应用
# List[2] = 1000 # 正确！列表中是合法应用


# a = (1, 2);
# b = (1,2.0);
# print(a == b);
# print(id(a));
# print(id(b));

# a2 = [1, 2];
# b2 = [1.0,2.0];
# print(a2 == b2);

# print ("-------字典---------");
# dict = {}
# dict["one"] = "This is one"
# dict[2] = "This is two"

# tinydict = {"name": "john", "code": 6734, "dept": "sales"}

# print (dict["one"]);  # 输出键为"one" 的值
# print (dict[2]);  # 输出键为 2 的值
# print (tinydict);  # 输出完整的字典
# print (tinydict.keys());  # 输出所有键
# print (tinydict.values());  # 输出所有值

# aaa = eval("print ('kkkk')");   #eval(str)函数: 将字符串str当成有效的表达式来求值并返回计算结果
# print (aaa);

# adict = {'name':'allen', 'name':'lucy', 'age':'40'} 

# print(2 ** 3);  #返回x的y次幂
# print(8 // 3);  #返回商的证书部分


# 身份运算符(身份运算符用于比较两个对象的存储单元)
# is , is not
# x is y , 如果 id(x) 等于 id(y) , is 返回结果 1
# print(1 is 1);
# print(1 is 1.0);
# a = 1;
# b = 1;
# print(id(a));
# print(id(b));
# print(a is b);

# count = 0
# while (count < 9):
#     print("the count is:%d"%count);
#     count = count + 1

# a = 4;
# b = 5;
# print(type(a + b));
# print("this sum is:%d"%(a + b));

# fruits = ['banana', 'apple',  'mango']
# print(len(fruits))
# for index in range(len(fruits)):
#    print("Current fruit :%s"%fruits[index])


# for num in range(10,20):  #to iterate between 10 to 20
#    for i in range(2,num): #to iterate on the factors of the number
#       if num%i == 0:      #to determine the first factor
#          j=num/i          #to calculate the second factor
#          print ("%d equals %d * %d"%(num,i,j))
#          break #to move to the next number, the #first FOR
#    else:                  # else part of the loop
#       print (num)

#Python中的for、while循环都有一个可选的else分支(类似if语句和try语句那样），
# 在循环迭代正常完成之后执行。
# 换句话说，如果我们不是除正常以外的其他方式退出循环，那么else分支将被执行。
# 也就是在循环体内没有break语句、没有return语句，或者没有异常出现。

























