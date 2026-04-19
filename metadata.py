import psutil

def get_device_info(device_name):
    partitions = psutil.disk_partitions()
    
    for p in partitions:
        if p.device == device_name:
            return {
                "Device": p.device,
                "Mountpoint": p.mountpoint,
                "FileSystem": p.fstype
            }

    return "Device not found"