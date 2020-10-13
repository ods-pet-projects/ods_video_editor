import moviepy.editor as mp

input_video_dir = '../data/input/video'
input_audio_dir = '../data/input/audio'

ofile_path = '../data/output/jd_videos_all.mp4'
# set name and time slice in seconds (start_sec, end_sec)
concat_dict = {'jd_sample_yota_4': (0, 10),
               'jd_sample_yota3': (1, 6),
               'jd_sample_yota_2': (0, 10),
               'jd_sample_theplace': (5, 15),
               'jd_sample_yota_1': (1, 11)}


def main():
    for name, (start_sec, end_sec) in concat_dict.items():
        print(name)
        ifile_path = f'../data/{name}.mp4'
        clip = mp.VideoFileClip(ifile_path)
        audio = clip.audio
        clip.write_videofile(f'{input_video_dir}/{name}.mp4', audio=False)
        audio.write_audiofile(f'{input_audio_dir}/{name}.mp3')


if __name__ == '__main__':
    main()
