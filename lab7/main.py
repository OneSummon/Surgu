import typer
import package

app = typer.Typer()

@app.command()
def get_matches_result(k: int):
    result = package.get_matches_result_recursion(k)
    print(result)

@app.command()
def use_memory_decorator():

    @package.memory_decorator
    def example_func_create():
        return [1] * 100

    example_func_create()

@app.command()
def get_pi_numbers(iterations: int):
    gen_pi_numbers = package.pi_leibniz(iterations)

    for i in gen_pi_numbers:
        print(i)

if __name__ == "__main__":
    app()