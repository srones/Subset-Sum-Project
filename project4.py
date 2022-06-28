from main import generateInstance

def export_ILP(i: int, instance: list[int], target: int):

    f = open(f'data/{i}.txt', "w")
    
    f.write("data;\n")
    f.write(f'param T := {int(target)};\n')
    f.write(f'param N := {len(instance)};\n')
    
    f.write(f'param W := \n')

    for index in range(len(instance)):
        f.write(f'[{index}] {instance[index]}\n')

    f.write(";\nend;")
    f.close()

    return

def parseILP(i: int):

    filename = f'ILP_raw_sln/{i}.txt'
    f = open(filename, "r")

    time = 0.0
    N = 0
    instance = []
    target = 0
    solution = []

    readingInstance = False
    readingSolution = False

    for line in f:

        if "N" in line:
            N = line.split()[2]

        if "solve" in line:
            time = line.split(" ")[2]
        
        if "T" in line:
            target = line.split(" ")[2]

        # --------

        if "W" in line:
            readingInstance = True
            continue

        if "X" in line:
            readingSolution = True
            continue

        if ";" in line:
            readingInstance = False
            readingSolution = False
            continue

        if(readingInstance):
            instance.append(int(line.split()[1]))

        if(readingSolution):
            solution.append(int(line.split()[1]))

    

    value = 0
    for j in range(len(solution)):
        if solution[j] == 1:
            value += instance[j]

    outf = open(f'ILP_parsed_sln/instance{i}.txt', "w")

    outf.write(f'N: {N}\n')
    outf.write(f'time: {time}')
    outf.write(f'value: {value}\n')
    outf.write(f'target: {target}')
    outf.write(f'instance: {instance}\n')
    outf.write(f'solution: {solution}')
    outf.close()

    return

def generateBenchmark():

    f = open("benchmark.txt", "w")

    for i in range(100):

        instance, target = generateInstance(i)

        f.write(f'i {i} T {int(target)}\n')
        f.write(" ".join(str(e) for e in instance) + "\n")

    f.close()

    return

def readBenchmark(i: int):

    f = open("benchmark.txt", "r")

    instance = []
    target = 0

    readingInstance = False

    for line in f:

        if "i" in line:

            if i == int(line.split()[1]):
                target = int(line.split()[3])
                readingInstance = True
                continue

        if readingInstance:
            for e in line.split(" "):
                if e != "\n":
                    instance.append(int(e))    
            f.close()
            return instance, target

    return instance, target

def compileGreedyILP(i):

    instance, target = readBenchmark(i)

    # greedy
    f_greedy = open("greedy_sln", "r")

    sGreedy = 0
    for line in f_greedy:

        if line[0] == "i":
            continue

        if int(line.split(",")[0]) == i:
            sGreedy = line.split()[6]

    # ILP
    f_ilp = open(f'ILP_parsed_sln/instance{i}.txt')

    sILP = 0
    for line in f_ilp:
        if "value" in line:
            sILP = line.split()[1]
        if "time" in line:
            tILP = line.split()[1]
    f_ilp.close()

    # compile
    f = open("Greedy_ILP", "a")
    print(f'{i}, {len(instance)}, {int(target)}, {sGreedy}, {sILP}, {tILP}\n')
    f.write(f'{i}, {len(instance)}, {int(target)}, {sGreedy}, {sILP}, {tILP}\n')
    f.close()

    return 

def main():

    # export_ILP()
    
    # generateBenchmark()

    f = open("Greedy_ILP", "w")
    f.write(f'i, N, T, sGreedy, sILP, tILP\n')

    for i in range(100):

        compileGreedyILP(i)

        # instance, target = readBenchmark(i)
        # export_ILP(i, instance, target)
        # parseILP(i)

        
    return

if __name__ == '__main__':
    main()
