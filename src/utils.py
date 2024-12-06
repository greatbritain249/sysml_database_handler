import os

def list_files_by_type(directory:str="./", file_extension:str=os.getenv("FILE_FILTER_TYPE", ".csv")):
    """
    Prints files in the specified directory with the given file extension.

    Parameters:
        directory (str): The path of the directory to search in.
        file_extension (str): The file extension to filter by (e.g., ".txt", ".csv").
    """
    files=[]
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return
    
    if not os.path.isdir(directory):
        print(f"The path '{directory}' is not a directory.")
        return

    print(f"Files with '{file_extension}' extension in '{directory}':")
    
    files_found = False
    for file in os.listdir(directory):
        if file.endswith(file_extension):
            files.append(f"{file}")
            files_found = True
    
    if not files_found:
        print(f"No files with extension '{file_extension}' found in the directory.")
    return files