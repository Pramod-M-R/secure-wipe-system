import os

def list_files(device_path):
    print("\n📁 Device Contents:\n")

    files_list = []

    try:
        items = os.listdir(device_path)

        index = 1
        for item in items:
            full_path = os.path.join(device_path, item)

            if os.path.isfile(full_path):
                print(f"{index}. 📄 {item}")
                files_list.append(full_path)
                index += 1

            elif os.path.isdir(full_path):
                print(f"{index}. 📁 {item}")
                files_list.append(full_path)
                index += 1

        return files_list

    except Exception as e:
        print("Error:", e)
        return []