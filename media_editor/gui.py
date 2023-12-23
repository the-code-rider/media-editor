from nicegui import ui, events

from media_editor.audio_editor import AudioEditor
from media_editor.composer import Composer
from media_editor.video_editor import VideoEditor

ae = AudioEditor()
ve = VideoEditor()
vc = Composer()

video_paths = []
audio_paths = []

def handle_audio_upload(e: events.UploadEventArguments):
    with open(e.name, 'wb') as f:
        f.write(e.content.read())
    ui.audio(e.name)
    audio_paths.append(e.name)

def handle_video_upload(e: events.UploadEventArguments):
    # good for local testing; when launching store the file in s3
   with open(e.name, 'wb') as f:
       f.write(e.content.read())
   import os
   print(os.listdir())
   video_paths.append(e.name)
   # video = ve.load_video(e.name)
   ui.video(e.name)

def merge():
    if len(video_paths) == 1 and len(audio_paths) == 1:
        # todo: add progress bar, make it async so that the ui is still responsive
        merged = vc.merge_video_audio(video_paths[0], audio_paths[0])
        vc.save(merged, 'merged.mp4')
        ui.video('merged.mp4')
        # option to download merged video


with ui.row().classes('w-full items-center mr-auto'):
    result = ui.label().classes('mr-auto')
    with ui.button(icon='menu'):
        with ui.menu() as menu:

            # can add callback method to take action
            ui.menu_item('Home')
            ui.menu_item('Subscription')
            ui.menu_item('Setting')

with ui.tabs().classes('w-full') as tabs:
    audio = ui.tab('Audio')
    video = ui.tab('Video')

with ui.tab_panels(tabs, value=audio).classes('w-full'):
    with ui.tab_panel(audio):
        ui.label('upload audios here')
        ui.upload(on_upload=handle_audio_upload)

    with ui.tab_panel(video):
        ui.label('video composer')
        with ui.row():
            ui.upload(on_upload=handle_video_upload, label='upload your video')
            ui.upload(on_upload=handle_audio_upload, label='upload your audio')
        ui.button('Merge', on_click=merge)





ui.run()