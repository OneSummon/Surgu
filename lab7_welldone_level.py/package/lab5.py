import sys
import tracemalloc
import functools


def memory_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if wrapper._is_running:
            return func(*args, **kwargs)
        
        wrapper._is_running = True
        tracemalloc.start()
        
        try:
            result = func(*args, **kwargs)
        finally:
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            wrapper._is_running = False

        return {
            "result": result,
            "memory_current": current,
            "memory_peak": peak,
            "describe": f"Память: текущая {current} байт | пик {peak} байт"
        }
    
    wrapper._is_running = False
    return wrapper