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

                        success = False
                        break
        except FileExistsError:
            print(f"[FAILED] Folder '{folder}' already exists")
            print("[PROCESS ABORTED]")

            success = False
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

if __name__ == '__main__':
    main()

    if success:
        print("[SUCCESS] Generated NodeJS project!")
