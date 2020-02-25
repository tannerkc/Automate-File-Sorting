from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for file in os.listdir(trackedFolder):

            # make lists of file types 

            imgType = ["png", "jpg", "jpeg", "gif"]
            videoType = ["mp4", "mov", "avi", "flv", "mpeg", "webm", "mpg", "wmv", "m4p"]
            archiveType = ["zip", "Gzip", "rar", "7z", "iso", "tar", "tgz", "xz", "z"]
            softwareType = ["dmg", "exe"]
            textType = ["docx", "doc", "docm", "dotx", "odt", "rtf", "xps", "txt"]
            spreadsheetType = ["csv", "pds", "xlsm", "xlsx", "xlam", "xltx", "xml"]
            presentationType = ["bmp", "ppa", "ppam", "ppt", "pps"]
            appType = ["apk", "ipa", "xap"]
            devType = ["py", "json", "css", "html", "htm", "js"]

            # grab each files original path 
            src = os.path.join(trackedFolder, file)

            # get the files extension 
            extension = file.split(".")[-1].lower()
            print(file.split("."))

            # determine where each file type will go, create directory if not already existing 

            if extension in imgType:
                newDestination = os.path.join(destinationFolder, "IMG")
                if not os.path.exists(newDestination):
                    os.mkdir(newDestination)
                newDestination = os.path.join(newDestination, file)

            elif extension in videoType:
                newDestination = os.path.join(destinationFolder, "Video")
                if not os.path.exists(newDestination):
                    os.mkdir(newDestination)
                newDestination = os.path.join(newDestination, file)

            elif extension in archiveType:
                newDestination = os.path.join(destinationFolder, "Archives")
                if not os.path.exists(newDestination):
                    os.mkdir(newDestination)
                newDestination = os.path.join(newDestination, file)

            elif extension in softwareType:
                newDestination = os.path.join(destinationFolder, "Installers")
                if not os.path.exists(newDestination):
                    os.mkdir(newDestination)
                newDestination = os.path.join(newDestination, file)

            elif extension in appType:
                newDestination = os.path.join(destinationFolder, "Mobile Apps")
                if not os.path.exists(newDestination):
                    os.mkdir(newDestination)
                # determine the type of app for further organization 
                if extension == "apk":
                    newDestination = os.path.join(newDestination, "Android")
                    if not os.path.exists(newDestination):
                        os.mkdir(newDestination)
                elif extension == "ipa":
                    newDestination = os.path.join(newDestination, "iOS")
                    if not os.path.exists(newDestination):
                        os.mkdir(newDestination)
                else:
                    newDestination = os.path.join(newDestination, "Other")
                    if not os.path.exists(newDestination):
                        os.mkdir(newDestination)
                newDestination = os.path.join(newDestination, file)

            elif extension in devType:
                newDestination = os.path.join(destinationFolder, "Dev Files")
                if not os.path.exists(newDestination):
                    os.mkdir(newDestination)
                # determine the type of app for further organization 
                if extension == "py":
                    newDestination = os.path.join(newDestination, "Python")
                    if not os.path.exists(newDestination):
                        os.mkdir(newDestination)
                if extension == "json":
                    newDestination = os.path.join(newDestination, "JSON")
                    if not os.path.exists(newDestination):
                        os.mkdir(newDestination)
                elif extension == "html" or extension == "htm" or extension == "css" or extension == "js":
                    newDestination = os.path.join(newDestination, "Web")
                    if not os.path.exists(newDestination):
                        os.mkdir(newDestination)
                    if extension == "html" or extension == "htm":
                        newDestination = os.path.join(newDestination, "html")
                        if not os.path.exists(newDestination):
                            os.mkdir(newDestination)
                    elif extension == "js":
                        newDestination = os.path.join(newDestination, "js")
                        if not os.path.exists(newDestination):
                            os.mkdir(newDestination)
                    elif extension == "css":
                        newDestination = os.path,join(newDestination, "css")
                        if not os.path.exists(newDestination):
                            os.mkdir(newDestination)
                newDestination = os.path.join(newDestination, file)

            elif extension in textType or extension in spreadsheetType or extension in presentationType:
                newDestination = os.path.join(destinationFolder, "Office")
                if not os.path.exists(newDestination):
                    os.mkdir(newDestination)
                # determine the type of office file for further organization 
                if extension in textType:
                    newDestination = os.path.join(newDestination, "Text Docs")
                    if not os.path.exists(newDestination):
                        os.mkdir(newDestination)
                elif extension in spreadsheetType:
                    newDestination = os.path.join(newDestination, "Spreadsheets")
                    if not os.path.exists(newDestination):
                        os.mkdir(newDestination)
                elif extension in presentationType:
                    newDestination = os.path.join(newDestination, "Presentations")
                    if not os.path.exists(newDestination):
                        os.mkdir(newDestination)
                newDestination = os.path.join(newDestination, file)

            elif extension == "pdf":
                newDestination = os.path.join(destinationFolder, "PDF")
                if not os.path.exists(newDestination):
                    os.mkdir(newDestination)
                newDestination = os.path.join(newDestination, file)

            elif extension == "whl":
                newDestination = os.path.join(destinationFolder, "Python Packages")
                if not os.path.exists(newDestination):
                    os.mkdir(newDestination)
                newDestination = os.path.join(newDestination, file)
            
            elif extension == "torrent":
                newDestination = os.path.join(destinationFolder, "Torrent Files")
                if not os.path.exists(newDestination):
                    os.mkdir(newDestination)

                #This following line is because I download a lot of courses from freecoursesite.com and like to have those files on their own
                if file.split(".")[0] == "FreeCourseSite":
                    newDestination = "C:/Users/Default User.DESKTOP-HLLJF0P/Documents/Courses"
                    if not os.path.exists(newDestination):
                        os.mkdir(newDestination)
                newDestination = os.path.join(newDestination, file)

            else:
                newDestination = os.path.join(destinationFolder, file)

            # check if file exists in sorted destination and add (copy) to end of file name
            if os.path.exists(newDestination):

                # split destination path at each period and get the length of that list, subtract one to get the second to last position (similar to -2 index) so the (copy) string gets placed just before the file extension

                newDestination = newDestination.split(".")
                index = len(newDestination)-1

                newDestination.insert(index, "(copy)")

                newDestination = '.'.join([str(elem) for elem in newDestination]) #convert back to string with periods between each item

                os.rename(src, newDestination)
            else:
                os.rename(src, newDestination) #rename original source to determined destinations


#set the observer to run only if this file is run directly, this is because I import this script into my personal virtual assistant to sort any folder I tell it 
if __name__ == "__main__":
# i keep the sorting folder separate rather than directly sorting the downloads folder so that longer downloads aren't moved before they're finished
    trackedFolder = "C:/Users/Default User.DESKTOP-HLLJF0P/Downloads/sortingFolder" 
    destinationFolder = "C:/Users/Default User.DESKTOP-HLLJF0P/Downloads" 

    eventHandler = FileHandler()
    observer = Observer()
    observer.schedule(eventHandler, trackedFolder, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
