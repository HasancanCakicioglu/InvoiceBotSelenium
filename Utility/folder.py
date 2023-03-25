import os


def getLastDownloadedFile(downloadedDic = 'C:\\Users\\Yonet\\Downloads'):
    # Define the path to the download directory
    download_directory = downloadedDic

    # List all files in the download directory
    files = os.listdir(download_directory)

    # Sort the files by modification time
    files.sort(key=lambda x: os.path.getmtime(os.path.join(download_directory, x)), reverse=True)

    # The most recently downloaded file is the first file in the sorted list
    most_recent_file = files[0]

    # The full path to the most recent file
    most_recent_file_path = os.path.join(download_directory, most_recent_file)

    return  most_recent_file_path



