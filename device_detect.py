import psutil

print("Detecting connected devices...\n")

partitions = psutil.disk_partitions()

for p in partitions:
    print("Device:", p.device)
    print("Mountpoint:", p.mountpoint)
    print("File system:", p.fstype)
    print("-" * 30)