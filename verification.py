import hashlib
import os

def generate_hash(filepath):
    try:
        if not os.path.exists(filepath):
            return None

        sha256 = hashlib.sha256()

        with open(filepath, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)

        return sha256.hexdigest()

    except Exception as e:
        print("❌ Hash error:", e)
        return None


def verify_wipe(before_hash, after_hash):
    print("\n🔍 Verification Result:")

    if before_hash is None:
        print("⚠️ File did not exist after wipe (expected)")
        return True

    if before_hash != after_hash:
        print("✅ Hash mismatch - Wipe successful")
        return True
    else:
        print("❌ Hash match - Wipe failed")
        return False