# time-tracker

## How it works?

```python
# just pass your function as argument to time_tracker 
# and assign to a variable, so it'll receive your function modified
def your_func():
    ...
    
your_func_tracked = time_tracker(your_func)

# now just starting using the variable as you would call your function

your_func_tracked()
```

##### example print
```commandline
TIME_TRACKER: your_func took 5.01 seconds
```

PS: it's just a simple way to monitor any function...