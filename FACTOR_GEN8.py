import tool.euler.euler as e
import sys, time, primefac as p


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Example of use: python {} <num>".format(sys.argv[0]))
        exit(-1)

    try:
        n = int(sys.argv[1])
    except:
        exit(-1)
        
    print("\n ==== Trying with EULER ==== \n\n")
    t = time.time()
    f = p.multifactor(n, methods=(p.pollardrho_brent, p.pollard_pm1, p.williams_pp1, p.ecm, p.siqs))

    t1 = time.time()
    if len(f) == 0:
        print("\n", n, "couldn't be factored :(\n")
        exit(-1)
    else:
        print("\nFactors are: ", f)
        print("\nTime:", t1 - t, "s\n")
        exit(0)

