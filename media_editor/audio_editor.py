from pydub import AudioSegment
from moviepy.editor import AudioFileClip
class AudioEditor:

    def load_audio_clip(self, audio_path):
        return AudioFileClip(audio_path)

    def overlay(self, audio1_path: str, audio2_path: str, auto_clip: bool = False):
        # auto clip will clip second sound

        sound1 = self.load_audio(audio1_path)
        sound2 = self.load_audio(audio2_path)
        sound2_clipped = None

        if auto_clip:
            # print("")
            sound1_length = len(sound1)
            sound2_clipped = sound2[:sound1_length]

        if sound1 and sound2:
            if sound2_clipped:
                overlay = sound1.overlay(sound2_clipped)
            else:
                overlay = sound1.overlay(sound2)

            return overlay
        else:
            raise Exception('Failed to read both sound')

    def export_audio(self, audio: AudioSegment, export_path: str, format: str = 'wav'):
        audio.export(export_path, format=format)

    def load_audio(self, audio_path):
        sound = None
        if audio_path.endswith('.mp3'):
            sound = AudioSegment.from_mp3(audio_path)
        elif audio_path.endswith('.wav'):
            sound = AudioSegment.from_wav(audio_path)

        return sound

    # def increase_loude


# if __name__ == mains