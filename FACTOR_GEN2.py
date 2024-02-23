import tool.pollard.rho as rho
import sys, time


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Example of use: python {} <num>".format(sys.argv[0]))
        exit(-1)

    try:
        n = int(sys.argv[1])
    except:
        exit(-1)
    
    print("\n ==== Trying with RHO simple ==== \n\n")
    t = time.time()
    f = rho.factorization(n, verbose = True)
    t1 = time.time()
    if f == -1:
        print("\n", n, "couldn't be factored :(\n")
        exit(-1)
    else:
        print("\nFactors are: ", f)
        print("\nTime:", t1 - t, "s\n")
        exit(0)

