from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips, transfx
import io
class VideoEditor:

    def load_video(self, video_path):
        return VideoFileClip(video_path)

    def load_binary_video(self, video_bytes):
        video_stream = io.BytesIO(video_bytes)
        return VideoFileClip(video_stream)


    def add_audio(self, video: VideoFileClip, audio:AudioFileClip):
        return video.set_audio(audio)

    def export_video(self, video: VideoFileClip, output_path):
        video.write_videofile(output_path)

    def export_video_index_error(self, video: VideoFileClip, output_path):
        # https://github.com/Zulko/moviepy/issues/646#issuecomment-475036696
        # Short by one frame, so get rid on the last frame:
        final_clip = video.subclip(t_end=(video.duration - 1.0 / video.fps))
        final_clip.write_videofile(output_path, threads=8, logger=None)
        print("Saved .mp4 after Exception at {}".format(output_path))


    def loop_with_transition(self, video: VideoFileClip, number_of_loops: int, crossfadein_time: int = 1):
        # loops same video with a transitions

        loopale_video = video.fx(transfx.make_loopable, crossfadein_time)
        video_list = [loopale_video for _ in range(number_of_loops)]
        final_clip = concatenate_videoclips(video_list)

        return final_clip

    def convert_to_gif(self, video_clip: VideoFileClip, output_name):
        # slow, use ffmpeg instead
        # ffmpeg -i wasteland_looped.mp4 -vf "fps=30,scale=1280:-1:flags=lanczos" -c:v gif -b:v 2M -maxrate 2M -bufsize 2M  output.gif
        video_clip.write_gif()



