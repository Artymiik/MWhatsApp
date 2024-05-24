import psutil
import time

def INFO_PC():
  cpu_count = psutil.cpu_count()

  cpu = psutil.virtual_memory()
  cpu_memmory = cpu.total / (1024 * 1024)

  if (cpu_memmory >= 6000 and cpu_memmory < 10000):
    if (cpu_count < 2):
      time.sleep(20)
    elif (cpu_count >= 2 and cpu_count < 3):
      time.sleep(15)
    elif (cpu_count >= 3 and cpu_count <= 4):
      time.sleep(8)
    else:
      time.sleep(13)