import hashlib
import os

def calculate_hash(file_path, algorithm='sha256'):
    """Calculate the hash of a file using a given algorithm."""
    if not os.path.isfile(file_path):
        print("[❌] File not found.")
        return None

    try:
        hash_func = getattr(hashlib, algorithm)()
    except AttributeError:
        print(f"[❌] Invalid hash algorithm: {algorithm}")
        return None

    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except Exception as e:
        print(f"[❌] Error reading file: {e}")
        return None

def main():
    file_path = input("Enter the full path to the file: ").strip()

    print("\nChoose hash algorithm:")
    print("1. SHA256 (default)")
    print("2. SHA1")
    print("3. MD5")
    choice = input("Enter choice [1/2/3]: ").strip()

    algorithm = 'sha256'
    if choice == '2':
        algorithm = 'sha1'
    elif choice == '3':
        algorithm = 'md5'

    hash_result = calculate_hash(file_path, algorithm)
    
    if hash_result:
        print(f"\n[{algorithm.upper()}] Hash:\n{hash_result}")
        
        compare = input("\nDo you want to compare with a known hash? (y/n): ").strip().lower()
        if compare == 'y':
            known_hash = input("Enter the known hash: ").strip().lower()
            if known_hash == hash_result.lower():
                print("[✅] Hashes match! File is likely authentic.")
            else:
                print("[⚠️] Hashes do not match. File may be tampered.")

if __name__ == "__main__":
    main()
