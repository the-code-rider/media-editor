from pytube import YouTube

class YoutubeClient:

    def get_video(self, url):
        # todo : add url validation
        return YouTube(url)

    def download_vide(self):
        pass
