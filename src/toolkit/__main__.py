import typer
from toolkit import calculator
from toolkit import converter
from toolkit import historicization

app = typer.Typer()

@app.command()
def calc(expression: str):
    historicization.wrire_to_json(expression, calculator.calculate(expression))
    typer.echo(calculator.calculate(expression))
    return calculator.calculate(expression)

@app.command()
def convert(value: float, 
    unit1: str = typer.Option(..., "--from"), 
    unit2: str = typer.Option(..., "--to")):
    typer.echo(converter.convert(float(value), unit1, unit2))
    return float(converter.convert(float(value), unit1, unit2))

if __name__ == '__main__':
    app()
