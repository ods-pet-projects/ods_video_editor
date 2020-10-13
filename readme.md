## ODS video editor
Video editor jupyter notebook

Feature `Concat audio and video parts`
- cut (start, end) part of audio and video files
- merge video and audio file with the same length
- concat video files into common file

Feature `Concat video and images frames`
- cut (start, end) part of video files
- create video sample from static image with fixed duration
- concat ordered samples to common video

Structure
- `notebooks/ods_video_converter.ipynb`
- `data`
- - `init` *.mp4 files with audio
- - `input`
- - - `audio` *.mp3 files
- - - `img` *.jpeg files
- - - `video`  *.mp4 files without audio
- - `output` *.mp4 result files with video and audio
