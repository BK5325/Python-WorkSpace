import pytube

def download_video(link):
    try:
        yt = pytube.YouTube(link)
        
        # Show video details
        print("Title: ", yt.title)
        print("Author: ", yt.author)
        print("Length: ", yt.length, "seconds")
        print("Views: ", yt.views)
        
        # Download video
        print("Downloading...")
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        print("Downloaded Successfully:", link)
    
    except pytube.exceptions.VideoPrivate:
        print("Video is private or removed.")
    except pytube.exceptions.VideoRegionBlocked:
        print("Video is regionally blocked.")
    except Exception as e:
        print("Error:", str(e))

def main():
    link = input('Paste the YouTube video URL here: ')
    download_video(link)

if __name__ == "__main__":
    main()
