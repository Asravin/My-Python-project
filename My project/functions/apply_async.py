def apply_async(func, *args, callback):
    result = func(*args)
    callback(result)