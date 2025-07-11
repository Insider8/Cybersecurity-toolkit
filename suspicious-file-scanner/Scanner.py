import os

# Define suspicious file extensions
suspicious_extensions = ['.exe', '.bat', '.vbs', '.js', '.scr', '.cmd', '.jar']

def scan_folder(path):
    print(f"\n[🔍] Scanning folder: {path}\n")
    found = False
    for root, _, files in os.walk(path):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext.lower() in suspicious_extensions:
                full_path = os.path.join(root, file)
                print(f"[⚠️] Suspicious file found: {full_path}")
                found = True
    if not found:
        print("[✅] No suspicious files found.")

if __name__ == "__main__":
    folder_to_scan = input("Enter the full path of the folder to scan: ").strip()
    
    if os.path.exists(folder_to_scan):
        scan_folder(folder_to_scan)
    else:
        print("[❌] The specified path does not exist.")
