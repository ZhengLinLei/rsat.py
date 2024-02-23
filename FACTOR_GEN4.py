import tool.pollard.pm1 as pm1
import sys, time, sympy


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Example of use: python {} <num>".format(sys.argv[0]))
        exit(-1)

    try:
        n = int(sys.argv[1])
    except:
        exit(-1)
        
    print("\n ==== Trying with PM1 ==== \n\n")
    t = time.time()
    f = []
    while(True):
        e = pm1.factorizatePm1(n)
        
        f.append(e)
        r = int(n/e)
        
        # check for prime using sympy
        if(sympy.isprime(r)):
            # both prime factors obtained
            f.append(r)
            break
        
        # reduced n is not prime, so repeat
        else:
            n = r

    t1 = time.time()
    if f == -1:
        print("\n", n, "couldn't be factored :(\n")
        exit(-1)
    else:
        print("\nFactors are: ", f)
        print("\nTime:", t1 - t, "s\n")
        exit(0)

