
import sys
import os

def count_contents_in():
    
    if len(sys.argv) == 2:
        dir_path = sys.argv[1]
        if os.path.exists(dir_path): 
            count = 0         
            for path in os.listdir(dir_path):
                if os.path.isfile(os.path.join(dir_path, path)):
                    count += 1
            print(f"Number of files in {sys.argv[1]}: {count} ")
        else:
            print("Invalid path")
    else:
        print("Usage: count_directory_contents.py <<directory path>>")

def main():
    count_contents_in()

if __name__ == '__main__':
    main()