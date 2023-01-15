# time-tracker

## How it works?

```python
# just pass your function as argument to time_tracker 
# and assign to a variable, so it'll receive your function modified
from time_tracker import tracker
...

def your_func():
    ...

your_func_tracked = tracker.timer(your_func)

# now just starting using the variable as you would call your function
your_func_tracked()

# or can be use as decorator
@tracker.timer
def your_func()
```


##### example output
```commandline
TIME_SPENT: your_func took 5.01 seconds
```

PS: it's just a simple way to monitor any function.