import os
import shutil
import sys

# --- CONFIGURATION ---
CONTAINER_FOLDER_NAME = "_Moved_media"
IMAGE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.webp', '.gif', '.bmp', '.tiff'}
VIDEO_EXTENSIONS = {'.mp4', '.mov', '.avi', '.mkv', '.webm', '.flv'}
MEDIA_EXTENSIONS = IMAGE_EXTENSIONS.union(VIDEO_EXTENSIONS)
# --- END OF CONFIGURATION ---

def migrate_media(source_folder, dest_root_folder):
    # (The rest of this function is unchanged)
    print("-" * 50)
    print(f"Scanning '{source_folder}' for media files...")
    total_files_moved = 0
    total_space_saved = 0

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_ext = os.path.splitext(file)[1].lower()
            if file_ext in MEDIA_EXTENSIONS:
                source_path = os.path.join(root, file)

                try:
                    file_size = os.path.getsize(source_path)
                    relative_path = os.path.relpath(root, source_folder)
                    dest_dir = os.path.join(dest_root_folder, relative_path)
                    os.makedirs(dest_dir, exist_ok=True)

                    dest_path = os.path.join(dest_dir, file)

                    print(f"Moving: {file} ({file_size / 1024 / 1024:.2f} MB)")
                    shutil.move(source_path, dest_path)

                    total_files_moved += 1
                    total_space_saved += file_size

                except Exception as e:
                    print(f"ERROR: Could not move {source_path}. Reason: {e}")

    print("-" * 50)
    print("Migration complete!")
    print(f"Total files moved: {total_files_moved}")
    print(f"Total space cleared: {total_space_saved / 1024 / 1024:.2f} MB")

if __name__ == "__main__":
    print("--- Media Migration Script ---")
    print("This script will move images and videos from a specified folder")
    print("and its subfolders to a container folder on another drive.")
    print("-" * 50)

    source_folder_path = input("Enter the FULL path to the folder you want to clean: ")
    dest_drive_path = input("Enter the destination drive (e.g., D:\\ or E:\\): ")

    # --- Safety Checks ---
    if not os.path.isdir(source_folder_path):
        print(f"ERROR: The source folder '{source_folder_path}' does not exist. Aborting.")
        sys.exit()

    if not os.path.isdir(dest_drive_path):
        print(f"ERROR: The destination drive '{dest_drive_path}' does not exist. Aborting.")
        sys.exit()

    # --- NEW AND IMPROVED SAFETY CHECK ---
    # Get the drive letter from both paths
    source_drive = os.path.splitdrive(source_folder_path)[0]
    dest_drive_letter = os.path.splitdrive(dest_drive_path)[0]

    # Only perform the 'commonpath' check if the drives are the same
    if source_drive.lower() == dest_drive_letter.lower():
        print("Source and destination are on the same drive. Checking for conflicts...")
        # Now this check is safe to run
        if os.path.commonpath([source_folder_path, dest_drive_path]) == source_folder_path:
            print("ERROR: The destination cannot be inside the source folder. Aborting.")
            sys.exit()
    # If drives are different, we don't need the check, it's always safe.

    final_destination_root = os.path.join(dest_drive_path, CONTAINER_FOLDER_NAME)

    print("\n--- PLEASE CONFIRM ---")
    print(f"Source folder: {source_folder_path}")
    print(f"ALL media will be moved into this new folder: '{final_destination_root}'")
    print("The original folder structure will be preserved inside that new folder.")
    print("This is a MOVE operation, not a copy.")

    confirm = input("Are you absolutely sure you want to proceed? (yes/no): ")

    if confirm.lower() == 'yes':
        migrate_media(source_folder_path, final_destination_root)
    else:
        print("Migration cancelled by user.")
