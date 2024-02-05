def solve(numheads, numlegs):
    for numCh in range(1,numlegs+1):
        numR=(numlegs-2*numCh)/4
        numCh=numheads-numR
        if numlegs==numCh*2+numR*4:
            print(numR)        
            print(numCh)
            break
solve(35, 94)

