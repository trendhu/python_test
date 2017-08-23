

# print("-------条件语句-------");
# if 判断条件：
#     执行语句……
# else：
#     执行语句…

# count = 18
# if count > 15:
#     print("count > 15")
# else:
#     print("count <= 15")


# print("-------循环语句-------");
# 循环语句中会出现控制语句 break , continue , pass
# 其中pass是空语句 , 是为了保持程序结构的完整性

# while 循环
# count = 0
# while (count < 9):
#    print 'The count is:', count
#    count = count + 

# count = 0
# while count < 9:
#     print(count)
#     count += 1  # python 不支持 ++ 



# fruits = ['a', 'b', 'c']
# for fruit in fruits:
#     print(fruit)

# for循环
# fruits = ['banana', 'apple',  'mango']
# for fruit in fruits:        # Second Example
#    print 'Current fruit :', fruit


# 带index的for循环
# fruits = ['banana', 'apple',  'mango']
# for index in range(len(fruits)):
#    print 'Current fruit :', fruits[index]

# fruits = ['banana', 'apple',  'mango']
# for index in range(len(fruits)):
#     print(fruits[index])




# for....else   -------> for … else 表示这样的意思，for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。
# for num in range(10,20):  #to iterate between 10 to 20
#    for i in range(2,num): #to iterate on the factors of the number
#       if num%i == 0:      #to determine the first factor
#          j=num/i          #to calculate the second factor
#          print '%d equals %d * %d' % (num,i,j)
#          break #to move to the next number, the #first FOR
#    else:                  # else part of the loop
#       print num, 'is a prime number'


# testString = "hello"
# print(testString)
# print(testString.capitalize())
# print(testString.center(20) + "|")

# s = "Hello  orld"
# print(s.title())
# print(s.istitle())
# print(s.ljust(20) + "|")

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(str(dict))







