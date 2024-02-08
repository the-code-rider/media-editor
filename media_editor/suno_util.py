from bs4 import BeautifulSoup
import requests



def get_audio_url(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        audio_meta_tag = soup.find('meta', property='og:audio')
        audio_url = audio_meta_tag['content'] if audio_meta_tag else None

    else:
        return None


def download_audio(audio_url, filename):
    with requests.get(audio_url, stream=True) as r:
        r.raise_for_status()  # This will raise an exception for HTTP errors
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
