import os,sys, tarfile, shutil

def validatePath(path):
    if os.path.isdir(path): 
        print("Path exists"); 
        return True; 
    else: 
        print("Path does not exist");
        return False;   

def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

def copy_tarfile(source_filename, dest_filename):
    shutil.move(source_filename, dest_filename)

def validateExtension(filename):
    if filename.endswith(".tar.gz"):
        print("File name valid");
        return True;
    else:
        print("File name invalid");
        return False;


# Main function

#Insert a path to 
source = input("Enter a path to backup content: ")
print("The path is: " + source)

print("Validating source path...")
isSourceValid = validatePath(source)

dest = input("Enter a destination path: ")
print("The path is: " + dest)

print("Validating destination path...")
isDestValid = validatePath(dest)


filename = input("Enter a filename: ")
isFileValid = validateExtension(filename)


if isSourceValid and isDestValid and isFileValid:
    print("Starting backup process...")
    make_tarfile(filename,source);
    print("Copy file to " + dest)
    copy_tarfile(filename,os.path.join(dest,'',filename))
    print("Backup done!")
else:
    sys.exit(1)




