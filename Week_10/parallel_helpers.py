import os

def member_diagnostic(member, n=700_000):
    total = 0.0
    for i in range(1, n):
        total += ((i + member) % 997) ** 0.5
    return {"member": member, "diagnostic": total / n, "pid": os.getpid()}
