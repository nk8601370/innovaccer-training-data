import os 


#path="/home/adminroot/Desktop/python_working/test_folder" 
#path='/mnt/shared_from_host'
path=os.environ.get("path_of_dir")

for filename in os.listdir(path):
    with open(os.path.join(path,filename),"r") as f:
        if filename.endswith("txt"):
            #print(filename)
            c=0
            for line in f.readlines():
                c+=len(line.split())
            print("file name ",filename, "word count ",c)