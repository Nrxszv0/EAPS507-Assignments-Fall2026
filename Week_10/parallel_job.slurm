#!/bin/bash
#SBATCH --job-name=eaps507_mpi
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=1
#SBATCH --time=00:10:00
#SBATCH --mem=4G
#SBATCH --output=eaps507_mpi_%j.out

# Activate the course environment here.
# module load <mpi-module>
# source <environment-activation-command>

srun -n 4 python mpi_precip_mean.py
