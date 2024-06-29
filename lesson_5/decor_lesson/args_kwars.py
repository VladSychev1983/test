def foo(*args, **kwargs):
    for item in args:
        print(item)
    kwargs["key"] = "value"
    print(kwargs)


foo("a", "b", named_1=1, named_2=2)


def foo2(arg_1, arg_2, param_1=1, param_2=2):
    print(f"{arg_1=}")
    print(f"{arg_2=}")
    print(f"{param_1=}")
    print(f"{param_2=}")


some_list = ["a", "b"]
some_dict = {"param_1": "10", "param_2": "20"}

foo2(*some_list, **some_dict)


some_list = ["a", "b", "c"]
a, *b = some_list
print(f"{a=}")
print(f"{b=}")
