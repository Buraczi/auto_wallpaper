from importlib.metadata import files
from logging import exception
import os, requests, wget, ctypes, os, ctypes, time, glob
import access_key #module with access key

project_root = os.path.dirname(os.path.abspath(__file__))

#using unsplash API to download random pics
def get_wallpaper():

    #connection to unsplash API
    url = "https://api.unsplash.com//photos/random/?client_id=" + access_key.access_key
    
    #parameters for json
    parameters = {
        "query": "1920x1080",
        "orientation": "landscape"
    }

    #get pic's url from json
    response = requests.get(url, parameters).json()
    image_url = response["urls"]["full"]

    #download pics
    wallpaper = wget.download(image_url, project_root + "/temp/")

    return wallpaper

#seting background on Windows os
def set_background():

    #temp dir for downloaded pics
    temp_dir = project_root + "/temp/"

    #create and sort array with pictures paths
    backgrounds = list(filter(os.path.isfile, glob.glob(temp_dir + "*")))
    backgrounds.sort(key=lambda x: os.path.getmtime(x))

    #setting last pic in dictionary (backgrounds[-1]) as wallpaper 
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(temp_dir, backgrounds[-1]), 0)
    
def main():
    try:
        #while True:
            get_wallpaper()
            set_background()
            #time.sleep(60) #automatyzation made in Task Scheduler on Windows - time.sleep unnessecery
    except KeyboardInterrupt:
        "Nice wallpaper!"
    except Exception:
        pass
        
if __name__ == "__main__":
    main()