import os
import shutil

def remove_virtual_envs(root_dir):
    for root, dirs, files in os.walk(root_dir, topdown=False):
        for name in dirs:
            # Check if the directory name ends with 'env'
            if name.endswith('env'):
                env_path = os.path.join(root, name)
                print(f"Removing virtual environment: {env_path}")
                try:
                    shutil.rmtree(env_path)
                except Exception as e:
                    print(f"Failed to remove {env_path}: {e}")

if __name__ == "__main__":
    workspace_folder = input("Enter the path to the workspace folder: ")
    remove_virtual_envs(workspace_folder)