# This script recursively detects invalid unicode code points in filenames in a directory

import os
import sys
import unicodedata

def detect_invalid_unicode(root_path):
    for root, dirs, files in os.walk(root_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file.encode("utf-8")
            except UnicodeEncodeError:
                print(f"Invalid unicode in file: {file_path}")
            try:
                unicodedata.normalize("NFC", file)
            except UnicodeError:
                print(f"Invalid unicode in file: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fix_unicode.py <path>")
        sys.exit(1)
    detect_invalid_unicode(sys.argv[1])
