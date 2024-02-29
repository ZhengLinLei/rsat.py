import sys, time
import tool.brute.brute1 as b


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Example of use: python {} <num>".format(sys.argv[0]))
        exit(-1)

    try:
        n = int(sys.argv[1])
    except:
        exit(-1)
        
    print("\n ==== Trying with BRUTE1 ==== \n\n")
    t = time.time()
    f = b.factors(n)
    t1 = time.time()
    if f == 0:
        print("\n", n, "couldn't be factored :(\n")
        exit(-1)
    else:
        print("\nFactors are: ", f)
        print("\nTime:", t1 - t, "s\n")
        exit(0)

