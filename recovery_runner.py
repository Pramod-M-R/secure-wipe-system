import subprocess
import os
import time

SCAN_DURATION = 15  # seconds

def run_photorec():
    print("\n🔍 Scanning for recoverable files...\n")

    exe_path = os.path.join(os.getcwd(), "testdisk-7.2", "photorec_win.exe")

    if not os.path.exists(exe_path):
        print("❌ PhotoRec not found")
        return {}, 0

    try:
        # 🔥 RUN IN BACKGROUND (NO INTERACTIVE SCREEN)
        process = subprocess.Popen(
            [exe_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        # Let it run for fixed time
        time.sleep(SCAN_DURATION)

        # Kill it
        process.terminate()

        print("✅ Scan completed\n")

        return analyze_recovered_files()

    except Exception as e:
        print("❌ Error:", e)
        return {}, 0


def analyze_recovered_files():
    file_groups = {
        "Images": [],
        "Videos": [],
        "Documents": [],
        "Others": []
    }

    image_ext = ["jpg", "jpeg", "png"]
    video_ext = ["mp4", "avi"]
    doc_ext = ["pdf", "txt", "pptx", "docx"]

    total_count = 0

    for folder in os.listdir():
        if folder.startswith("recup_dir"):
            for file in os.listdir(folder):
                total_count += 1

                ext = file.split('.')[-1].lower()
                full_path = os.path.join(folder, file)

                if ext in image_ext:
                    file_groups["Images"].append(full_path)
                elif ext in video_ext:
                    file_groups["Videos"].append(full_path)
                elif ext in doc_ext:
                    file_groups["Documents"].append(full_path)
                else:
                    file_groups["Others"].append(full_path)

    print(f"📊 Total Recoverable Files: {total_count}\n")

    index = 1
    for key in file_groups:
        print(f"{index}. 📁 {key} ({len(file_groups[key])} files)")
        index += 1

    return file_groups, total_count