
# input()은 입력 받은 값을 문자열로 저
# a = input("값을 입력하세요 :")
# print(a)
#
# a = int(input("정수를 입력하세요 :"))
# b = float(input("실수를 입력하세요 :"))
# print("두 수를 더한 결과는: ", a + b, "입니다.")
# print(type(a+b))

a = 10
b = -2.5
c = 1 + 2j
d = 0xDA # 218

print("2j : ", 2j)

print(a, type(a))
print(b, type(b))
print(c, c.real , c.imag, c.conjugate(), type(c))
print(d, type(d))

print(a + b, type(a + b))
print(c + d, type(c + d))

num1 = 17.5
num2 = 10
cpx1 = 3 + 3j
cpx2 = 1 - 2j
str1 = "Hello"
str2 = "goorm"

print(num1 + num2)
print(str1 + str2)
print(num1 - num2)
print(num1 * num2)
print(num2 ** num1)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)
print(cpx1 / cpx2)