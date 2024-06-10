#смена переменной из под внутренней функции внутри функции. Деректива nonlocal
def func_outer():
    x = 2
    print('x в outer равно', x)
    
    def func_inner():
        nonlocal x
        x = 5
        print('x в inner равно', x)
        
    func_inner()
    print('Локальное x в outer сменилось на ', x)

func_outer()
