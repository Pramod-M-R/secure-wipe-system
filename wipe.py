import os
import random

def wipe_file(filepath, passes=3):
    print("\n🔐 Starting secure wipe...")

    try:
        if not os.path.exists(filepath):
            print("❌ File does not exist")
            return

        size = os.path.getsize(filepath)

        with open(filepath, "ba+", buffering=0) as f:
            for p in range(passes):
                print(f"Pass {p+1}/{passes}...")

                f.seek(0)

                if p % 2 == 0:
                    # Random data
                    data = os.urandom(size)
                else:
                    # Zeros
                    data = b'\x00' * size

                f.write(data)

        # Final delete
        os.remove(filepath)

        print("✅ File securely wiped and deleted")

    except Exception as e:
        print("❌ Error during wipe:", e)