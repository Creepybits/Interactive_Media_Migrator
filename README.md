# Interactive Media Migrator

An interactive Python script designed to help reclaim disk space by safely moving large collections of images and videos from a primary folder (like `Downloads` or a project folder) to a secondary drive.

This is a significantly safer and more user-friendly evolution of the original drive-scanning `image_migrator.py` script.

---

## ✨ Key Features

*   **Interactive & Safe:** No more editing the script! It interactively prompts you for the source folder and destination drive, eliminating the risk of hardcoding incorrect paths and accidentally moving system files.
*   **Targeted Cleanup:** Instead of scanning an entire drive, you point it to a specific folder you want to clean up (e.g., `C:\Users\YourName\Desktop\AI_Generations`).
*   **Supports Images & Videos:** Easily configurable to move a wide range of common image and video file formats.
*   **Preserves Directory Structure:** Your folder organization is perfectly mirrored on the destination drive. No more ending up with thousands of files dumped into one big folder.
*   **Organized Destination:** All moved content is placed inside a single, configurable container folder (e.g., `D:\_Moved_media`) on the destination drive to keep its root directory clean.
*   **Built-in Safety Checks:** The script verifies that the source and destination paths exist before attempting to move any files.

## 🚀 How to Use

1.  Save the script as a Python file (e.g., `migrate_media.py`).
2.  Open a terminal or PowerShell in the directory where you saved the script.
3.  Run the script by typing:
    ```
    python migrate_media.py
    ```
4.  Follow the on-screen prompts:
    *   First, it will ask for the **full path to the folder you want to clean**.
        *   *Example:* `C:\Users\zanno\Documents\My_Projects`
    *   Next, it will ask for the **destination drive**.
        *   *Example:* `D:\`
5.  The script will show you a final confirmation of the source and the exact destination folder it will create. Review it carefully.
6.  Type `yes` and press Enter to begin the migration.

### Starting the script  

<img width="748" height="241" alt="image" src="https://github.com/user-attachments/assets/1613eafd-aec9-4110-a579-01a98bc0ad09" />  

### When the script is done  
<img width="748" height="241" alt="image" src="https://github.com/user-attachments/assets/8027091d-f098-4012-bf30-c607f066ea18" />




## 🔧 Configuration

While the script is interactive, you can easily customize its core behavior by editing the variables at the top of the file:

*   `CONTAINER_FOLDER_NAME`: Change the name of the main folder where all files will be moved. (Default: `_Moved_media`)
*   `IMAGE_EXTENSIONS`: Add or remove image file extensions from this list.
*   `VIDEO_EXTENSIONS`: Add or remove video file extensions from this list.

___

# Delete Empty Folders

An interactive python script that deletes empty folder in a given directory.

This script will:
1. Ask for a folder to clean.
2. Walk through every single subfolder within it.
3. Check if a folder is empty.
4. If and only if it is empty, it will delete it.
5. It works from the inside out, so it can delete nested empty folders (e.g., A/B/C where all three are empty).

It's very safe and, as is our tradition, will ask you for confirmation before it touches anything.

## 🚀 How to Use

1.  Save the script as a Python file (e.g., `delete_empty_folders.py`).
2.  Open a terminal or PowerShell in the directory where you saved the script.
3.  Run the script by typing:
    ```
    delete_empty_folders.py
    ```
___
# Sort

A quick sorting batch file. 

This will sort all images in a _image_ folder and all video files in a _video_ folder.

## 🚀 How to Use

Put the sort.bat file **in the folder you want to sort** and double click on it.

### ⚠️ WARNING: This batch file will **not ask for confirmation**
___

## ⚠️ A Word of Caution

While this script is designed to be much safer than its predecessor, it is a powerful tool that **MOVES** files (not copies them). A "move" operation is a "copy" followed by a "delete".

*   **Backup First:** Always have a backup of your important data before running any script that modifies files on your system.
*   **Verify Paths:** Double-check the paths you enter when prompted to ensure you are targeting the correct folder.

Use this script at your own risk. We are not responsible for any data loss.
