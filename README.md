# Backup Automation Script 🔄

## Description  
This Python script automates the process of backing up files from a source directory to a destination directory. It ensures that only modified or new files are copied by checking the file's hash value, making it an efficient backup solution.  

---

## How It Works 🚀  

1. **Calculating File Hash**:  
   - The script calculates the MD5 hash of each file to ensure that the file contents are compared accurately (avoiding unnecessary copying of identical files).  
   - It uses the `hashlib` library to create the hash.  

2. **Backup File**:  
   - If the file doesn't already exist in the destination directory, it's copied.  
   - If the file exists, the hash of the source and destination files are compared. If the hashes differ, the file is updated in the backup directory.

3. **Backup Directory**:  
   - The script traverses the source directory and copies all files (and subdirectories) to the destination directory.

4. **Preserving File Metadata**:  
   - The script uses `shutil.copy2()` to preserve the file’s metadata (timestamps, etc.) when copying.

---

## Usage Instructions 🛠️  

### Prerequisites:  
- Python installed on your system (preferably version 3.6+).  
- The script only uses built-in Python libraries (`os`, `shutil`, `hashlib`, `datetime`), so no additional installation is required.  

