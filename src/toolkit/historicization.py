from .constant import YEAR, MONTH, DAY, HOUR, MINUTE
import json

def wrire_to_json(expression, result):
    new_record = {
        "expression": expression,
        "result": result,
        "datetime": f'{DAY}.{MONTH}.{YEAR} {HOUR}:{MINUTE}'
    }
    try:
        with open("history.json", "r") as file:
            history = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        history = []

    history.append(new_record)
    
    with open("history.json", "w") as file:
        json.dump(history, file, ensure_ascii=0, indent=4)
