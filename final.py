from project4 import readBenchmark

def main():

    f = open("final.txt", "w")
    f.write(f'i, N, T, s_exh1, s_exh10, s_greedy, s_ILP, s_dp, s_local, t_exh1, t_exh10, t_greedy, t_ILP, t_dp, t_local\n')

    for i in range(100):

        instance, target = readBenchmark(i)

        # exh1
        s_exh1 = -1
        t_exh1 = -1

        f_temp = open("Exhaustive_sln", "r")
        for line in f_temp:
            if line.split(", ")[0] == str(i):
                s_exh1 = line.split(", ")[3]
                t_exh1 = line.strip().split(", ")[4]
                break

        f_temp.close()
        
        # exh10
        s_exh10 = -1
        t_exh10 = -1

        f_temp = open("Exhaustive10_sln", "r")
        for line in f_temp:
            if line.split(", ")[0] == str(i):
                s_exh10 = line.split(", ")[3]
                t_exh10 = line.strip().split(", ")[4]
                break
        f_temp.close()

        # greedy | ILP
        s_greedy = -1
        t_greedy = 0
        s_ILP = -1
        t_ILP = -1

        f_temp = open("Greedy_ILP", "r")
        for line in f_temp:
            if line.split(", ")[0] == str(i):
                s_greedy = line.split(", ")[3]
                s_ILP = line.split(", ")[4]
                t_ILP = line.strip().split(", ")[5]
                break

        f_temp.close()

        # DP
        s_dp = -1
        t_dp = -1

        f_temp = open("DP.txt", "r")
        for line in f_temp:
            if line.split(", ")[0] == str(i):
                s_dp = line.split(", ")[1]
                t_dp = line.strip(", ").split()[2]
                break

        f_temp.close()

        # local
        s_local = -1
        t_local = -1
        
        f.write(f'{i}, {len(instance)}, {target}, {s_exh1}, {s_exh10}, {s_greedy}, {s_ILP}, {s_dp}, {s_local}, {t_exh1}, {t_exh10}, {t_greedy}, {t_ILP}, {t_dp}, {t_local}\n')
        
    f.close()
    return


if __name__ == '__main__':
    main()