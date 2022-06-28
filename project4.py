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

def main():

    print()

    for i in range(100):

        instance, target = generateInstance(i)

        export_ILP(i, instance, target)
    
    print()

    return

def readFile(i: int):

    filename = f'out/{i}.txt'
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

    outf = open(f'out1/instance{i}.txt', "w")

    outf.write(f'N: {N}\n')
    outf.write(f'time: {time}')
    outf.write(f'value: {value}\n')
    outf.write(f'target: {target}')
    outf.write(f'instance: {instance}\n')
    outf.write(f'solution: {solution}')
    outf.close()

    return

def mainRead():

    for i in range(99):
        readFile(i)

    return

if __name__ == '__main__':
    # main()
    mainRead()