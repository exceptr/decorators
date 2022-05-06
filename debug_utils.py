from datetime import datetime
import json


def make_logger(path):
    def _make_logger(old_function):
        current_date = datetime.now()
        file1_log = {f'Date': f'{current_date}', 'Func': f'{old_function.__name__}'}

        def new_function(*args, **kwargs):
            print(f'Дата и время {current_date}. Вызвана функция - {old_function.__name__}')
            print(f'С аргументами {args} и {kwargs}')
            file1_log['Args'] = f'{args} и {kwargs}'
            result = old_function(*args, **kwargs)
            print(f'Получили {result}')
            print('-' * 100)
            print('\n')
            file1_log['Result'] = result
            with open(path, "a", encoding='cp1251') as f:
                json.dump(file1_log, f, ensure_ascii=False, indent=2)
            return result

        return new_function

    return _make_logger
