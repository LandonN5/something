import sys
from random import randint
file = sys.argv[1]
run = True
var = {}
lines = 0
times_s = 0
with open(file, "r") as file:
    contents = file.readlines()
    script_length = len(contents)
    if not contents[0].startswith("start=__PROGRAM__"):
        run = False
    while lines < script_length:
        if run == False:
            break
        if contents[lines].startswith("end=__PROGRAM__") or contents[lines].startswith("!s!"):
            break
        if contents[lines].startswith("puts"):
            if contents[lines].split('(')[1].split(')')[0].startswith('"'):
                print(contents[lines].split('("')[1].replace('")',''))
            else:
                variable_to_print = contents[lines].split('(')[1].split(')')[0]
                print(var[variable_to_print])

                
        if contents[lines].startswith("add.puts"):
            args = contents[lines].split('(')[1].split(')')[0].split(',')
            print(int(args[0]) + int(args[1]))
        if contents[lines].startswith("sub.puts"):
            args = contents[lines].split('(')[1].split(')')[0].split(',')
            print(int(args[0]) - int(args[1]))
        if contents[lines].startswith("div.puts"):
            args = contents[lines].split('(')[1].split(')')[0].split(',')
            print(int(args[0]) / int(args[1]))
        if contents[lines].startswith("mul.puts"):
            args = contents[lines].split('(')[1].split(')')[0].split(',')
            print(int(args[0]) * int(args[1]))

            print(int(args[0]) * int(args[1]))
        if contents[lines].startswith("import -> PI"):
            var['PI'] = 3.14
        if contents[lines].startswith("int"):
            name = contents[lines].split()[1]
            value = int(contents[lines].split()[3])
            var[name] = value
        if contents[lines].startswith("String"):
            name = contents[lines].split()[1]
            value = contents[lines].split()[3].replace('"','')
            var[name] = value

        if contents[lines].startswith("FUNC"):
            endFunc = 0
            nameFunc = str(contents[lines].split()[1].split("(")[0])
            for end_of_func in range(lines,script_length):
                if contents[end_of_func].startswith("ENDED"):
                    endFunc = end_of_func
            for oy in range(lines,script_length):
                if contents[oy].startswith(str(nameFunc) + "()"):
                    can_run = True
                    break
                else:
                    can_run = False

            if can_run == False:
                lines = endFunc


        if contents[lines].startswith("auto"):
            name = contents[lines].split()[1]
            value = contents[lines].split()[3]
            var[name] = value
        if contents[lines].startswith('end=__LOOP__'):
            for t in range(0,script_length):
                if contents[t].startswith("!halt!"):
                    break
                if contents[t].startswith('start=__LOOP__'):
                    lines = t

        if contents[lines].startswith('end=__REPEAT__'):
            count = int(contents[lines].split()[1]) - 1
            for t in range(0,script_length):
                if contents[t].startswith("!halt!"):
                    break
                if times_s == count:
                    break
                if contents[t].startswith('start=__REPEAT__'):
                    times_s += 1
                    lines = t
        if contents[lines].startswith("!add.puts"):
            args = contents[lines].split('(')[1].split(')')[0].split(',')
            print(int(var[args[1]]) + int(var[args[1]]))
        if contents[lines].startswith("!sub.puts"):
            args = contents[lines].split('(')[1].split(')')[0].split(',')
            print(int(var[args[1]]) - int(var[args[1]]))
        if contents[lines].startswith("!div.puts"):
            args = contents[lines].split('(')[1].split(')')[0].split(',')
            print(int(var[args[1]]) / int(var[args[1]]))
        if contents[lines].startswith("!mul.puts"):
            args = contents[lines].split('(')[1].split(')')[0].split(',')
            print(int(var[args[1]]) * int(var[args[1]]))

        if contents[lines].startswith("purge"):
            del var[contents[lines].split('(')[1].split(')')[0]]

        if contents[lines].startswith("gets"):
            questi = contents[lines].split('(')[1].split(')')[0].split(',')[0].split('"')[1]
            variable = contents[lines].split('(')[1].split(')')[0].split(',')[1]
            inp = input(questi)
            var[variable] = inp
        if contents[lines].startswith("convertINT"):
            variable_to_take = contents[lines].split('(')[1].split(')')[0]
            int(var[variable_to_take])
        if contents[lines].startswith("rand"):
            args = contents[lines].split('(')[1].split(')')[0].split(',')
            var[args[0]] = randint(int(args[1]),int(args[2]))
        if contents[lines].startswith("--"):
            name = contents[lines].split()[1]
            value = int(contents[lines].split()[2])
            var[name] -= value

        if contents[lines].startswith("IF"):
            state = False
            end = ''
            for end_of_if in range(lines,script_length):
                if contents[end_of_if].startswith('END'):
                    end = end_of_if
            if eval(contents[lines].split()[1]):
                state = True
            else:
                state = False
                lines = end
        

        lines += 1

