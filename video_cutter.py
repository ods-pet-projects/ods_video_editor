from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

from utils import timeit


@timeit
def main():
    idir = 'data/init'
    odir = 'data/output'

    ifile_path = f'{idir}/jd_sample_theplace.mp4'
    ofile_path = f'{odir}/test_sample.mp4'
    start_time = 0
    end_time = 10

    print(f'converting {start_time} - {end_time}')
    ffmpeg_extract_subclip(ifile_path, start_time, end_time, targetname=ofile_path)


if __name__ == '__main__':
    main()
