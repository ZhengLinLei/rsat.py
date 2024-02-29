import sys, time
from factordb.factordb import FactorDB


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
    f = FactorDB(n)
    f.connect()
    l = f.get_factor_list()
    t1 = time.time()
    if len(l) == 0:
        print("\n", n, "couldn't be factored :(\n")
        exit(-1)
    else:
        print("\nFactors are: ", l)
        print("\nFactor API: ", f.get_factor_from_api())
        print("\nTime:", t1 - t, "s\n")
        exit(0)

