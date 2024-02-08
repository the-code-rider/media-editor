from pydub import AudioSegment
from moviepy.editor import AudioFileClip
from pydub.playback import play
import io
class AudioEditor:

    def load_audio_clip(self, audio_path):
        return AudioFileClip(audio_path)

    def merge_audio_clips(self, audio_list):
        # pydub
        merged_audio = sum(audio_list)
        return merged_audio

    def play_audio(self, audio_clip):
        play(audio_clip)

    def snip_audio_clip(self, audio_clip, start_min, start_sec, end_min, end_sec):
        # time in seconds
        start_time = start_min*60*1000 + start_sec*1000
        end_time = end_min*60*1000 + end_sec*1000

        clipped_audio = audio_clip[start_time:end_time]
        return clipped_audio

    def match_target_amplitude(self, source_clip, target_clip):
        change_in_dBFS = target_clip.dBFS - source_clip.dBFS
        return source_clip.apply_gain(change_in_dBFS)


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

    def load_binary_audio(self, binary_audio, format: str = 'mp3'):
        audio_stream = io.BytesIO(binary_audio)
        return AudioSegment.from_file(audio_stream, format=format)

    def get_max_amplitude(self, audio_clip):
        return audio_clip.max

    def get_max_loudness(self, audio_clip):
        return audio_clip.max_dBFS


    # def increase_loude


# if __name__ == mains