## a program to manage project creation
import os
# import sys
# import argparse

# a function to create a working directpry or folder

def create_poject_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)
    else:
        print(f"{directory} already exists")

#create_poject_dir("Planets")
#create_poject_dir(r"C:\Users\USER\Desktop/ORBITALS")

def create_project(name, language, project_dir):
    language = language.lower()
    #move project to folder
    os.chdir(project_dir)

    if language == 'python' or language == 'python3':
        #execute project creation
        print(f"Creating python project: {name}")
        os.system('python -m venv venv')
        os.system('source venv/bin/activate' if not os.name == 'nt' else '.\\venv\\scripts\\activate')
        os.system('git init')
        os.system('curl https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore >> .gitignore')
        os.system('echo >> main.py if' if os.name == 'nt' else 'touch main.py')
        os.system('git add . && git commit -m "Initial commit')
        os.system('code .')

    else:
        print("Unsupported language")

#main function
def main():
    print('Welcome to my project creator')
    project_name = input("Enter project name: ")
    project_dir = input("Enter project directory: ")
    language = input('Enter language to use: ')
    create_poject_dir(project_dir)
    create_project(project_name, language, project_dir)

if __name__ == '__main__':
    main()
    