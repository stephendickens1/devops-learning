import os

def remove_prefix_from_directories(prefix):
    # List all items in the current directory
    items = os.listdir('.')
    
    for item in items:
        # Check if the item is a directory and if its name starts with the given prefix
        if os.path.isdir(item) and item.startswith(prefix):
            # Create the new directory name by removing the prefix
            new_dirname = item[len(prefix):]
            # Rename the directory
            os.rename(item, new_dirname)
            print(f'Renamed directory: {item} -> {new_dirname}')

# Set the prefix you want to remove
prefix_to_remove = "day-"

# Call the function to remove the prefix from directories
remove_prefix_from_directories(prefix_to_remove)

