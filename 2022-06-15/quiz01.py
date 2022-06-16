def test1(num1, num2, *args, **kwargs):
    print(f"num1 : {num1}")
    print(f"num2 : {num2}")
    print(args)
    print(kwargs)

    return


test1(1, 2,
     3, 4, 5, 6, 7, 8, 9, 4, 5, 6, 7, 8,
     num3=5, num4=5, num5=6
     )
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
def test2(*args, **kwargs):
    print(args)
    return True


sample_list = [1, 2, 3, 4, 5]
sample_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
}

test2(*sample_list, ** sample_dict)
test2(1, 2, 3, 4, 5,
     key1="value1",
     key2="value2",
     key3="value3",
     key4="value4",
     )


a = [1, 2, 3, 4, 5]

print(a)  # == print([1,2,3,4,5])
print(*a)  # == print(1,2,3,4,5)
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# from user.models import User

# def user(requset):
#     if request.method == "POST":
#         username = request.POST.get('username'),
#         fullname = request.POST.get('fullname'),
#         gender = request.POST.get('gender'),
#         birthdat = request.POST.get('birthdat'),

#         user = User.objects.create(
#             username ="username",
#             fullname ="fullname",
#             gender ="gender",
#             birthdat ="birthdat",
#         )

# def user(requset):
#     if request.method == "POST":
#         user = User.objects.create(
#             **requset.POST
#         )

# 작업속도는 딱히 차이는 안나지만 가독성이 좋다