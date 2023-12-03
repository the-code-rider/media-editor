from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips, transfx

class VideoEditor:

    def load_video(self, video_path):
        return VideoFileClip(video_path)

    def add_audio(self, video: VideoFileClip, audio:AudioFileClip):
        return video.set_audio(audio)

    def export_video(self, video: VideoFileClip, output_path):
        video.write_videofile(output_path)

    def loop_with_transition(self, video: VideoFileClip, number_of_loops: int, crossfadein_time: int = 1):
        # loops same video with a transitions

        loopale_video = video.fx(transfx.make_loopable, crossfadein_time)
        video_list = [loopale_video for _ in range(number_of_loops)]
        final_clip = concatenate_videoclips(video_list)

        return final_clip



