import os
import shutil
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Recursively copy files from source directory to a new directory sorted by file extensions.")
    parser.add_argument('source', type=str, help='Path to the source directory')
    parser.add_argument('-d', '--destination', type=str, default='dist', help='Path to the destination directory (default: "dist")')
    args = parser.parse_args()
    return args

def copy_files(src_path, dest_path):
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    for item in os.listdir(src_path):
        item_path = os.path.join(src_path, item)
        if os.path.isdir(item_path):
            copy_files(item_path, dest_path)  # Recursive call
        else:
            file_ext = os.path.splitext(item)[-1][1:]  # Extract file extension
            if file_ext == '':
                file_ext = 'no_extension'
            ext_dir = os.path.join(dest_path, file_ext)
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)
            shutil.copy(item_path, ext_dir)

def main():
    args = parse_args()
    src = os.path.abspath(args.source)
    dest = os.path.abspath(args.destination)

    try:
        copy_files(src, dest)
        print(f"Files have been copied from {src} to {dest} sorted by their extensions.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
