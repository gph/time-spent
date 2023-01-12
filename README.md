#### How it works?
```commandline
# just pass your function as argument to time_spent
# and assign to a variable, so it'll receive your function modified
# just call the variable created as you would call your function

def your_func():
    ...

your_func_tracked = time_spent(your_func)

result = your_func_tracked()
# it'll print the time spent by your function
```


PS: it's just a simple way to monitor any function...