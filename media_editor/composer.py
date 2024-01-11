import math

from moviepy.video.VideoClip import ImageClip

from media_editor.audio_editor import AudioEditor
from media_editor.video_editor import VideoEditor

class Composer:

    def __init__(self):
        self.video_editor = VideoEditor()
        self.audio_editor = AudioEditor()

    def merge_video_audio(self, video_path, audio_path):
        video = self.video_editor.load_video(video_path)
        audio = self.audio_editor.load_audio_clip(audio_path)
        merged = None
        if video.duration == audio.duration:
            merged = self.video_editor.add_audio(video, audio)

        elif audio.duration > video.duration:
            loops_required = math.ceil(audio.duration/video.duration) + 1
            looped_video = self.video_editor.loop_with_transition(video, loops_required)
            clipped_video = looped_video.subclip(0, math.ceil(audio.duration) + 2)
            merged = self.video_editor.add_audio(clipped_video, audio)

        return merged

    def merge_image_and_audio(self, image_path, audio_path):
        audio_clip = self.audio_editor.load_audio_clip(audio_path)
        audio_duration = audio_clip.duration

        video_clip = ImageClip(image_path, duration=audio_duration)
        video_clip = video_clip.set_audio(audio_clip)

        return video_clip


    def save(self, video, output_path):
        self.video_editor.export_video(video, output_path)





    