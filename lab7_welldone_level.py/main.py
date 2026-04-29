import uvicorn
import package
import example_functions_for_decorator
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# middleware cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://127.0.0.1",
        "http://127.0.0.1:5500",
        "http://localhost:5000",
        "null"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)


@app.get("/get_matches_result/{k}")
async def get_matches_result(k: int):
    result = package.get_matches_result_recursion(k)
    return {"result" : result}


@app.get("/use_memory_decorator/{index_func}")
async def use_memory_decorator(index_func: int, count: int = None, text: str = None):
    functions = {
        1 : example_functions_for_decorator.list_of_squares,
        2 : example_functions_for_decorator.generator_of_squares,
        3 : example_functions_for_decorator.fibonacci_recursive,
        4 : example_functions_for_decorator.matrix_multiply,
        5 : example_functions_for_decorator.word_frequency
    }

    func = functions[index_func]

    if index_func != 5 and count is not None:
        return func(count)
    
    elif index_func == 5 and text is not None:
        return func(text)


@app.get("/get_pi_numbers/{iterations}")
async def get_pi_numbers(iterations: int):
    result = 0.0
    for i in package.pi_leibniz(iterations):
        result = i
    
    return {"result" : result}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)