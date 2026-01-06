import os

def batch_rename():
    # --- CONFIGURATION ---
    # The text you want to remove from the front
    prefix_to_remove = "500 Parking Rep"
    
    # Set this to False only when you are ready to actually rename the files
    dry_run = False
    
    # The folder where the files are. "." means the current folder where this script is saved.
    # You can change this to a full path like "C:/Users/Name/Documents/Files"
    folder_path = "." 
    # ---------------------

    print(f"--- Starting Process (Dry Run: {dry_run}) ---\n")

    count = 0
    
    # Loop through all files in the directory
    for filename in os.listdir(folder_path):
        
        # Check if the file starts with the specific prefix
        if filename.startswith(prefix_to_remove):
            
            # Remove the prefix
            # len(prefix_to_remove) calculates the length of the text to cut
            # .strip() removes any extra spaces left at the start (like the space after "Rep")
            new_name = filename[len(prefix_to_remove):].strip()
            
            # Get full file paths
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_name)
            
            if dry_run:
                print(f"[PREVIEW] Would rename: '{filename}'  -->  '{new_name}'")
            else:
                try:
                    os.rename(old_file, new_file)
                    print(f"[SUCCESS] Renamed: '{filename}'  -->  '{new_name}'")
                except FileExistsError:
                    print(f"[ERROR] Could not rename '{filename}' because '{new_name}' already exists.")
                except Exception as e:
                    print(f"[ERROR] {e}")
            
            count += 1

    if count == 0:
        print("\nNo files found starting with that prefix.")
    else:
        print(f"\nProcessed {count} files.")

if __name__ == "__main__":
    batch_rename()