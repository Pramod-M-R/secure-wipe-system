import subprocess
import sys
import time

def install_and_import(package_name):
    try:
        __import__(package_name)
        print(f"✅ {package_name} already installed")
    except ImportError:
        print(f"\n📦 {package_name} is not installed.")
        print("⬇️ Installing now... Please wait (Do NOT close the program)\n")

        try:
            # Show installation process
            process = subprocess.Popen(
                [sys.executable, "-m", "pip", "install", package_name],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )

            # Print live output
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    print(output.strip())

            print(f"\n✅ {package_name} installed successfully!\n")

        except Exception as e:
            print(f"❌ Failed to install {package_name}")
            print("Error:", e)
            sys.exit()


def setup_environment():
    print("\n⚙️ Checking required components...\n")
    time.sleep(1)

    install_and_import("psutil")
    install_and_import("reportlab")

    print("🚀 All dependencies ready. Starting program...\n")
    time.sleep(1)