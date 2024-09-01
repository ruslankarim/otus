def self_decorator(function_to_decorate):
    def wrap_original_function():  # объявляем вложенную функцию
        print("before")
        function_to_decorate()  # вызываем оригинальную функцию
        print("after")

    return wrap_original_function


@self_decorator
def easy_function():
    print("i am just printing this")


easy_function()
