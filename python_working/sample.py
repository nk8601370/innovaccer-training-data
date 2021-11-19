x=5
print(x)

#lamda function

add_func = lambda a,b:a+b

def sum_n(func,n):
    val=0
    for i in range(n):
        val=func(val,i)
    return val
sum_n(add_func,100)


mul_func=lambda a,b: a*b

def return_func(string):
    if (string=='add'):
        return add_func
    else:
        return mul_func

return_func('add')(3,4)


#######
l=[3,4,5,6,7,8,9]
mod_cum = lambda x: x*2 if x%2==0 else 0

l=lambda a:a[0:10] 

func = lambda a: a*2 for a in l


#####
sqr = lambda x:x**2

[a**2 for a in l]#list comprehension

[(lambda x:x**2)(a) for a in l]

l=[3,4,5,6,7,8,9]
v=[1,2,3,4,5,6,7]

[i+j for i,j in list(zip(l,v))]


########

def square(num):
    return  num**2
my_nums=[1,2,3,4,5]

list(map(square,my_nums))

or

list(map(square,[1,2,3,4,5]))