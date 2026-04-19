import sys

# 🔥 AUTO SETUP (INSTALL DEPENDENCIES WITH USER FEEDBACK)
try:
    from auto_install import setup_environment
except:
    print("❌ auto_install.py missing")
    sys.exit()

setup_environment()

# 🔥 IMPORTS
import psutil
import time
import os
from metadata import get_device_info
from file_explorer import list_files
from wipe import wipe_file
from recovery_runner import run_photorec
from verification import generate_hash, verify_wipe
from ml_analysis import compute_recoverability_score
from logger import log_event
from certificate_generator import generate_certificate

print("🔌 Monitoring for new device...\n")

before = set([p.device for p in psutil.disk_partitions()])

while True:
    time.sleep(2)

    after = set([p.device for p in psutil.disk_partitions()])
    new_devices = after - before

    if new_devices:
        print("✅ New device detected!\n")

        for dev in new_devices:
            print("Device:", dev)

            info = get_device_info(dev)
            print("Device Info:", info)

            # 🔍 BEFORE SCAN
            print("\n🔍 Running initial recovery scan...")
            recovered_groups, before_count = run_photorec()

            # 📁 DEVICE FILES
            device_files = list_files(dev)

            print("\nSelect file source:")
            print("1. Device Files")
            print("2. Recoverable Files")

            source_choice = int(input("\nEnter choice: ").strip())

            try:
                # 🔷 DEVICE FILES
                if source_choice == 1:
                    file_index = int(input("\nEnter file number to wipe: ").strip())
                    selected_file = device_files[file_index - 1]

                # 🔷 RECOVERABLE FILES
                elif source_choice == 2:
                    group_keys = list(recovered_groups.keys())

                    print("\nSelect category:")
                    for i, key in enumerate(group_keys, start=1):
                        print(f"{i}. {key}")

                    group_choice = int(input("\nEnter category number: ").strip())
                    selected_group = group_keys[group_choice - 1]

                    files = recovered_groups[selected_group]

                    print(f"\n📁 {selected_group}:\n")
                    for i, f in enumerate(files, start=1):
                        print(f"{i}. {os.path.basename(f)}")

                    file_index = int(input("\nEnter file number to wipe: ").strip())
                    selected_file = files[file_index - 1]

                else:
                    print("❌ Invalid choice")
                    break

                print("\nSelected:", selected_file)
                log_event(f"Selected file: {selected_file}")

                # 🔐 CONFIRMATION
                confirm = input("\n⚠️ Are you sure you want to erase this file? (y/n): ").strip().lower()

                if confirm != "y":
                    print("❌ Operation cancelled")
                    log_event("Operation cancelled by user")
                    continue

                # 🔐 HASH BEFORE
                before_hash = generate_hash(selected_file)
                print("\n🔑 Hash before wipe:", before_hash)

                # 🔥 WIPE
                wipe_file(selected_file)
                log_event(f"File wiped: {selected_file}")

                # 🔐 HASH AFTER
                after_hash = generate_hash(selected_file)
                print("🔑 Hash after wipe:", after_hash)

                # 🔍 VERIFY HASH
                verify_wipe(before_hash, after_hash)

                # 🔍 AFTER SCAN
                print("\n🔍 Running recovery scan after wipe...")
                _, after_count = run_photorec()

                # 🤖 ML ANALYSIS
                hash_changed = (before_hash != after_hash)

                score, level, prediction = compute_recoverability_score(
                    before_count,
                    after_count,
                    hash_changed
                )

                print("\n🤖 ML Analysis Result:")
                print(f"Recoverability Score: {score}")
                print(f"Security Level: {level}")
                print(f"Prediction: {prediction}")

                log_event(f"ML Result - Score: {score}, Level: {level}, Prediction: {prediction}")

                # 🔐 FINAL VERIFICATION (STRONG PROOF)
                print("\n🔐 FINAL VERIFICATION:")

                if after_count == 0:
                    print("✅ No recoverable files found - Data completely erased")
                    log_event("Final Result: Fully erased")
                elif after_count < before_count:
                    print("⚠️ Partial recovery possible - Some traces remain")
                    log_event("Final Result: Partially recoverable")
                else:
                    print("❌ Data still recoverable - Wipe not effective")
                    log_event("Final Result: Still recoverable")

                # 📄 GENERATE PDF CERTIFICATE
                generate_certificate(selected_file, score, level, prediction)

            except Exception as e:
                print("❌ Error:", e)
                log_event(f"Error: {str(e)}")

        break

    before = after