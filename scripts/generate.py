import os
import json

from template import *

success = True

def generateCoreFiles(entryPoint, package):
    for filename, content in entryPoint.items():
        with open(filename, 'w+') as f:
            f.write(content)

    with open('package.json', 'w+') as packagejson:
        json.dump(package, packagejson)

def buildFolderStructure(folders):
    global success

    # exeptions should never happen because the process creates everything in a new folder but it's better to still handle them
    for folder, subfolders in folders.items():
        try:
            os.mkdir(folder)
            if subfolders:
                for subfolder in subfolders:
                    try:
                        os.mkdir(f"{folder}/{subfolder}")
                    except FileExistsError:
                        print(f"[FAILED] Folder '{folder}/{subfolder}' already exists")
                        print("[PROCESS ABORTED]")

                        break
        except FileExistsError:
            print(f"[FAILED] Folder '{folder}' already exists")
            print("[PROCESS ABORTED]")

            break


def populateWithReadme(readmes):
    for path, content in readmes.items():
        with open(f"{path}/readme.md", 'w+') as f:
            f.write(content)

def generateApp(appFiles):
    for folder, files in appFiles.items():
        for filename, content in files.items():
            with open(f"{folder}/{filename}", 'w+') as f:
                f.write(content)

def installDependencies():
    os.system('npm install .')

def main():
    print("[RUNNING] Generating project...")

    while success:
        print("[WRITING] Core files...")
        generateCoreFiles(entryPoint, package)
        print("[DONE] Folder structure.") 

        print("[BUILDING] Folder structure...")
        buildFolderStructure(folders)
        print("[DONE] Folder structure.")

        print("[WRITING] Readmes...")
        populateWithReadme(readmes)
        print("[DONE] Readmes.")

        print("[WRITING] App files...")
        generateApp(appFiles)
        print("[DONE] App files.")

        print("[INSTALLING] Dependencies from package.json...")
        installDependencies()
        print("[DONE] Installed dependencies.")
        break

if __name__ == '__main__':
    try:
        os.mkdir('app')
    except FileExistsError:
        print("[FAILED] Folder 'app' already exists")
        os._exit(1)

    os.chdir('app')
    main()

    if success:
        print("[SUCCESS] Generated NodeJS project!")
