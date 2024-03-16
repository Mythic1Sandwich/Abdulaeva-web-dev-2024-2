import datetime

def function_logger(log_file):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = datetime.datetime.now()
            result = func(*args, **kwargs)
            end_time = datetime.datetime.now()
            execution_time = end_time - start_time
            
            with open(log_file, 'a') as file:
                file.write(f'{func.__name__}\n')
                file.write(f'{start_time}\n')
                file.write(f'{args if args else kwargs}\n')
                file.write(f'{result if result else "-"}\n')
                file.write(f'{end_time}\n')
                file.write(f'{execution_time}\n\n')
            
            return result
        
        return wrapper
    return decorator

@function_logger('the.log')
def greeting_format(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    greeting_format('John')
