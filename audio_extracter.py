import moviepy.editor

cvt_video = moviepy.editor.VideoFileClip("E:\Py\Geeks Projects Python\Audio extracter\Small Talk  Everyday English.3gp.mp4")

ext_audio = cvt_video.audio
ext_audio.write_audiofile("E:\Py\Geeks Projects Python\Audio extracter\Audio_extracted.mp3")