#!/usr/bin/env python3

import hpcMpi
import sys
import time as t


if __name__ == '__main__':
    comm = hpcMpi.COMM_WORLD
    worldRank = comm.Get_rank()
    worldSize = comm.Get_size()

    # parse command line arguments
    step = 1e-3
    if len(sys.argv) == 2:
        step = float(sys.argv[1])

    t0 = t.time()

    # compute

    ai = worldRank/worldSize 
    bi = (worldRank+1)/worldSize
    calcul = ((1-0)/worldSize)*worldRank
    values = hpcMpi.compute(hpcMpi.fPi, ai, bi, step)

    t1 = t.time()

    comm.Reduce(values,op=MPI.SUM)

    # output result
    if worldRank == 0 :
        time = t1 - t0
        print(value[0])
        print(time)
