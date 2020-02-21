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
            src = trackedFolder + "/" + file

            # get the files extension 
            extension = file.split(".")[-1].lower()
            print(file.split("."))

            # determine where each file type will go, create directory if not already existing 

            if extension in imgType:
                newDestination = destinationFolder + "/" + "IMG"
                if not os.path.exists(newDestination):
                    os.mkdir(newDestination)
                newDestination = newDestination + "/" + file

            elif extension in videoType:
                newDestination = destinationFolder + "/" + "Video"
                if not os.path.exists(newDestination):
                    os.mkdir(newDestination)
                newDestination = newDestination + "/" + file

            elif extension in archiveType:
                newDestination = destinationFolder + "/" + "Archives"
                if not os.path.exists(newDestination):
                    os.mkdir(newDestination)
                newDestination = newDestination + "/" + file

            elif extension in softwareType:
                newDestination = destinationFolder + "/" + "Installers"
                if not os.path.exists(newDestination):
                    os.mkdir(newDestination)
                newDestination = newDestination + "/" + file

            elif extension in appType:
                newDestination = destinationFolder + "/" + "Mobile Apps"
                if not os.path.exists(newDestination):
                    os.mkdir(newDestination)
                # determine the type of app for further organization 
                if extension == "apk":
                    newDestination = newDestination + "/" + "Android"
                    if not os.path.exists(newDestination):
                        os.mkdir(newDestination)
                elif extension == "ipa":
                    newDestination = newDestination + "/" + "iOS"
                    if not os.path.exists(newDestination):
                        os.mkdir(newDestination)
                else:
                    newDestination == newDestination + "/" + "Other"
                    if not os.path.exists(newDestination):
                        os.mkdir(newDestination)
                newDestination = newDestination + "/" + file

            elif extension in devType:
                newDestination = destinationFolder + "/" + "Dev Files"
                if not os.path.exists(newDestination):
                    os.mkdir(newDestination)
                # determine the type of app for further organization 
                if extension == "py":
                    newDestination = newDestination + "/" + "Python"
                    if not os.path.exists(newDestination):
                        os.mkdir(newDestination)
                if extension == "json":
                    newDestination = newDestination + "/" + "JSON"
                    if not os.path.exists(newDestination):
                        os.mkdir(newDestination)
                elif extension == "html" or extension == "htm" or extension == "css" or extension == "js":
                    newDestination = newDestination + "/" + "Web"
                    if not os.path.exists(newDestination):
                        os.mkdir(newDestination)
                    if extension == "html" or extension == "htm":
                        newDestination = newDestination + "/" + "html"
                        if not os.path.exists(newDestination):
                            os.mkdir(newDestination)
                    elif extension == "js":
                        newDestination = newDestination + "/" + "js"
                        if not os.path.exists(newDestination):
                            os.mkdir(newDestination)
                    elif extension == "css":
                        newDestination = newDestination + "/" + "css"
                        if not os.path.exists(newDestination):
                            os.mkdir(newDestination)
                newDestination = newDestination + "/" + file

            elif extension in textType or extension in spreadsheetType or extension in presentationType:
                newDestination = destinationFolder + "/" + "Office"
                if not os.path.exists(newDestination):
                    os.mkdir(newDestination)
                # determine the type of office file for further organization 
                if extension in textType:
                    newDestination = newDestination + "/" + "Text Docs"
                    if not os.path.exists(newDestination):
                        os.mkdir(newDestination)
                elif extension in spreadsheetType:
                    newDestination = newDestination + "/" + "Spreadsheets"
                    if not os.path.exists(newDestination):
                        os.mkdir(newDestination)
                elif extension in presentationType:
                    newDestination = newDestination + "/" + "Presentations"
                    if not os.path.exists(newDestination):
                        os.mkdir(newDestination)
                newDestination = newDestination + "/" + file

            elif extension == "pdf":
                newDestination = destinationFolder + "/" + "PDF"
                if not os.path.exists(newDestination):
                    os.mkdir(newDestination)
                newDestination = newDestination + "/" + file

            elif extension == "whl":
                newDestination = destinationFolder + "/" + "Python Packages"
                if not os.path.exists(newDestination):
                    os.mkdir(newDestination)
                newDestination = newDestination + "/" + file
            
            elif extension == "torrent":
                newDestination = destinationFolder + "/" + "Torrent Files"
                if not os.path.exists(newDestination):
                    os.mkdir(newDestination)
                    
                #This following line is because I download a lot of courses from freecoursesite.com and like to have those files on their own
                if file.split(".")[0] == "FreeCourseSite":
                    newDestination = "C:/Users/Default User.DESKTOP-HLLJF0P/Documents/Courses"
                    if not os.path.exists(newDestination):
                        os.mkdir(newDestination)
                newDestination = newDestination + "/" + file

            else:
                newDestination = destinationFolder + "/" + file

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