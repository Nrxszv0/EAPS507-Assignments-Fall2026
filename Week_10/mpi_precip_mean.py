from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Each rank creates a reproducible local precipitation sample.
rng = np.random.default_rng(507 + rank)
local_precip = rng.gamma(shape=2.0, scale=4.0, size=10_000)
local_sum = local_precip.sum()
local_count = local_precip.size

global_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)
global_count = comm.reduce(local_count, op=MPI.SUM, root=0)

print(f"rank {rank}/{size}: local mean = {local_precip.mean():.3f}")
if rank == 0:
    print(f"Global mean = {global_sum / global_count:.3f}")
