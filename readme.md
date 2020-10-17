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


Feature Inner DSL for video preparing pipeline
Set file aliasing
```python
params = {
    'ww': 'data/init_hb/ww trailer 2 season.mp4',
    'ww_a': 'data/init_hb/ww music.mp4',
    'wh': 'data/init_hb/wh trailer.mp4',
    'wch': 'data/init_hb/wtch wild.mp4',
    'hb_i': 'data/init_hb/hb eu.png',
}
```
Describe pipeline, using syntax
- `obj.a` - get audio
- `obj.v` - get video
- `*` merge into one clip different sources (video, audio, image)
- `+` concat by timeline video clips
- `obj[10: 13]` numpy like slice by time in seconds
Example
```
query = '''
        ww[43: 50].v * ww_a[75: 82].a +
        wh[158: 173].v * wch[15: 30].a +
        hb[3: 21].v * hb[3: 21].a * hb_i[0:18].i + hb_i.i[0:10]
'''
```
Create `MovDSL` pipeline, run `query` and save result file
```
dsl = MovDSL(params) \
    .query(query) \
    .save('data/output/dsl_example.mp4')
```