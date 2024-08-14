import os
import shutil


def delete_pycache(start_dir):
    deleted_count = 0
    deleted_locations = []

    for root, dirs, files in os.walk(start_dir):
        if '__pycache__' in dirs:
            pycache_path = os.path.join(root, '__pycache__')
            print(f"Deleting: {pycache_path}")
            shutil.rmtree(pycache_path)
            deleted_count += 1
            deleted_locations.append(pycache_path)

    return deleted_count, deleted_locations


# Get the home directory
home_dir = os.path.expanduser('~')

# Run the deletion function
count, locations = delete_pycache(home_dir)

print(f"\nTotal __pycache__ directories deleted: {count}")
print("\nDeleted from:")
for location in locations:
    print(location)

print("\nFinished deleting __pycache__ directories.")
