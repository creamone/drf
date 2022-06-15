# def test(num1, num2, *args, **kwargs):
#     print(f"num1 : {num1}")
#     print(f"num2 : {num2}")
#     print(args)
#     print(kwargs)

#     return


# test(1, 2,
#      3, 4, 5, 6, 7, 8, 9, 4, 5, 6, 7, 8,
#      num3=5, num4=5, num5=6
#      )

def test(*args, **kwargs):
    print(args)
    return True


sample_list = [1, 2, 3, 4, 5]
sample_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
}

test(*sample_list, ** sample_dict)
test(1, 2, 3, 4, 5,
     key1="value1",
     key2="value2",
     key3="value3",
     key4="value4",
     )


# a = [1, 2, 3, 4, 5]

# print(a)  # == print([1,2,3,4,5])
# print(*a)  # == print(1,2,3,4,5)
