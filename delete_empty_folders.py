import os
import sys

def delete_empty_folders(root_path):
    """
    Walks through a directory from the bottom up and deletes any empty folders.
    """
    deleted_folders_count = 0

    # We walk from the bottom up (topdown=False) so we can delete empty
    # child directories before we check their parents.
    try:
        for dirpath, dirnames, filenames in os.walk(root_path, topdown=False):
            # Check if the directory is empty
            if not dirnames and not filenames:
                try:
                    print(f"Deleting empty folder: {dirpath}")
                    os.rmdir(dirpath)
                    deleted_folders_count += 1
                except OSError as e:
                    print(f"Error deleting {dirpath}: {e}")
    except FileNotFoundError:
        print(f"Error: The directory '{root_path}' was not found.")
        return 0

    return deleted_folders_count

if __name__ == "__main__":
    print("--- Empty Folder Cleanup Script ---")
    print("This script will find and delete ALL empty subfolders within a specified directory.")
    print("\nWARNING: This action is permanent and cannot be undone.")
    print("--------------------------------------------------")

    # Get the target directory from the user
    target_dir = input("Enter the FULL PATH of the folder you want to clean: ")

    # Validate the path
    if not os.path.isdir(target_dir):
        print(f"\nError: The path '{target_dir}' is not a valid directory.")
        input("Press Enter to exit.")
        sys.exit()

    # Final confirmation
    print(f"\nTarget directory: {target_dir}")
    confirm = input("Are you absolutely sure you want to proceed? (yes/no): ").lower()

    if confirm == 'yes':
        print("\nStarting cleanup...")
        count = delete_empty_folders(target_dir)
        print("\n--- Cleanup Complete ---")
        if count > 0:
            print(f"Successfully deleted {count} empty folder(s).")
        else:
            print("No empty folders were found to delete.")
    else:
        print("\nOperation cancelled by user.")

    input("\nPress Enter to exit.")
