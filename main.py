from add import add_func  # add.py를 foo가 작성하도록 함. 파라미터 2개.
from sub import sub_func  # sub.py를 master가 작성. 파라미터 2개.

# 전역 변수부
num1, num2, result = 100, 200, 0

## 메인 코드부
result = add_func(num1, num2)
print(result)
result = sub_func(num1, num2)
print(result)
