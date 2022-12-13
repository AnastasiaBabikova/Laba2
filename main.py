import json

with open('base.json', 'r', encoding='utf-8') as fh:  # открываем файл на чтение
    data = json.load(fh)  # загружаем из файла данные в словарь data
    print("База знаний", data)


def sravn(arg):
    x = arg[0]
    if x in memory:
        if(arg[1]==memory[x]):
            return False
    return True


def op_and(arg):
    k = 0
    for i in range(0, len(arg)):
        if run(arg[i]) == False :
            k += 1
    if k == len(arg):
        return True
    if k > 0:
        return False


def pprint(arg):
    arg = ''.join(arg)
    print(arg)



memory = {"solution": 0, "jacket": 0, "trousers": 0, "weather": 0, "length": 0, "tight_skirt": 0, "comfortable": 0, "sport": 0, "hood": 0, "warm": 0}


def get(arg):
    return memory[arg[0]]


def yes_or_no(arg):
    arg = ''.join(arg)
    answer = input(arg + ' (да/нет): ')
    return answer


def question_weather(arg):
    arg = ''.join(arg)
    answer = int(input(arg + ' (числовое значение): '))
    return answer


def op_set(arg):
    x = arg[0]
    for i in range(1, len(arg)):
        res = run(arg[i])
        if x in memory:
            if (res != None):
                memory[x] = res


def found(arg):
    x = arg[0]
    if x in memory:
        memory[x] = 1

        
        
func = {'==': sravn,
        'print': pprint,
        'get': get,
        'yes_or_no': yes_or_no,
        'question_weather': question_weather,
        'and': op_and,
        'set': op_set,
        'found': found
        }

def run(expression):#обработка вложенных
    mas = [] #обработанные аргументы
    op = expression.get('op')
    #print("ИМЯ ОПЕРАЦИИ", op)
    func_1 = func.get(op)
    #print(func_1)
    arg = expression.get('arg')
    #print("АРГУМЕНТЫ", arg)
    #print("Второй арг", arg[1])
    for i in range(len(arg)):
        if isinstance(arg, dict):
            mas.append(run(arg[i]))
        else:
            mas.append(arg[i])
    return func_1(mas)


#Если левая часть правильная, то можем выполнить и правую.
for rule in data:
    if (run(rule['left']) == True):
        run(rule['right'])
