# a program to convert a video to DVD
import subprocess
# fps = [25, 29.97,]
# size = ['720x576', '720x480']


# options for interlaced video
# interlaced = ('-flags +ilme+ildct', -top -1')
# field_order = (str(0), str(1), str(2)) -top 1 => top, -top 0 => bottom, -top -1 => auto

# framerate, size, pix_fmt, video bitrate, profile name
DVD_NTSC_p = ('NTSC progressive 6400k (VBR)',)
DVD_NTSC_i = ('NTSC interlaced 6400k (VBR)',)

DVD_PAL_p = ('PAL progressive 6400k (VBR)',)
DVD_PAL_i = ('PAL interlaced 6400k (VBR)',)

print('\n\nThis little program allows you to transcode a file to the mpeg2video codec (DVD).')
file = '-i ' + input('Please enter the source video file name: ') #  i.e. example.mkv'
output = input('Please enter a new filename for the transcoded video: ')

print('\nTo transcode to DVD please make a choice.')
print('Which profile would you like to use for transcoding?\n\n')
print('1 - ' + DVD_NTSC_p[0] + '\n2 - ' + DVD_NTSC_i[0] + '\n3 - ' + DVD_PAL_p[0] + '\n4 - ' + DVD_PAL_i[0] + '\n')
profile = input('Type the number:  ')

if profile == str(1):
	ffmpegcmd1 = 'ffmpeg ' + file + ' -v error -c:v mpeg2video -r 29.97 -pix_fmt yuv420p -color_primaries smpte170m -color_trc smpte170m -colorspace smpte170m -me_method epzs -dc 9 -g 15 -bf 2 -cmp 2 -subcmp 2 -trellis 0 -vf yadif=0:1:0 -s 720x480 -b:v 6400k -maxrate 7200k -bufsize 1835008 -packetsize 2048 -an -threads 2 -y -stats -f dvd NULL'
	ffmpegcmd2 = 'ffmpeg ' + file + ' -v error -c:v mpeg2video -r 29.97 -pix_fmt yuv420p -color_primaries smpte170m -color_trc smpte170m -colorspace smpte170m -me_method epzs -dc 9 -g 15 -bf 2 -cmp 2 -subcmp 2 -trellis 0 -vf yadif=0:1:0 -s 720x480 -b:v 6400k -maxrate 7200k -bufsize 1835008 -packetsize 2048 -c:a ac3 -ac 2 -ar 48k -b:a 192k -async 1 -threads 2 -y -stats -vstats ' + output
elif profile == str(2):
    ffmpegcmd1 = 'ffmpeg ' + file + ' -v error -c:v mpeg2video -r 29.97 -pix_fmt yuv420p -color_primaries smpte170m -color_trc smpte170m -colorspace smpte170m -me_method epzs -dc 9 -g 15 -bf 2 -cmp 2 -subcmp 2 -trellis 0 -flags +ilme+ildct -top -1 -s 720x480 -b:v 6400k -maxrate 7200k -bufsize 1835008 -packetsize 2048 -an -threads 2 -y -stats -f dvd NULL'
    ffmpegcmd2 = 'ffmpeg ' + file + ' -v error -c:v mpeg2video -r 29.97 -pix_fmt yuv420p -color_primaries smpte170m -color_trc smpte170m -colorspace smpte170m -me_method epzs -dc 9 -g 15 -bf 2 -cmp 2 -subcmp 2 -trellis 0 -flags +ilme+ildct -top -1 -s 720x480 -b:v 6400k -maxrate 7200k -bufsize 1835008 -packetsize 2048 -c:a ac3 -ac 2 -ar 48k -b:a 192k -async 1 -threads 2 -y -stats -vstats ' + output
elif profile == str(3):
    ffmpegcmd1 = 'ffmpeg ' + file + ' -v error -c:v mpeg2video -r 25 -pix_fmt yuv420p -color_primaries bt470bg -color_trc gamma28 -colorspace bt470bg -me_method epzs -dc 9 -g 12 -bf 2 -cmp 2 -subcmp 2 -trellis 0 -vf yadif=0:1:0 -s 720x576 -b:v 6400k -maxrate 7200k -bufsize 1835008 -packetsize 2048 -an -threads 2 -y -stats -f dvd NULL'
    ffmpegcmd2 = 'ffmpeg ' + file + ' -v error -c:v mpeg2video -r 25 -pix_fmt yuv420p -color_primaries bt470bg -color_trc gamma28 -colorspace bt470bg -me_method epzs -dc 9 -g 12 -bf 2 -cmp 2 -subcmp 2 -trellis 0 -vf yadif=0:1:0 -s 720x576 -b:v 6400k -maxrate 7200k -bufsize 1835008 -packetsize 2048 -c:a ac3 -ac 2 -ar 48k -b:a 192k -async 1 -threads 2 -y -stats -vstats ' + output
elif profile == str(4):
    ffmpegcmd1 = 'ffmpeg ' + file + ' -v error -c:v mpeg2video -r 25 -pix_fmt yuv420p -color_primaries bt470bg -color_trc gamma28 -colorspace bt470bg -me_method epzs -dc 9 -g 12 -bf 2 -cmp 2 -subcmp 2 -trellis 0 -flags +ilme+ildct -top -1 -s 720x576 -b:v 6400k -maxrate 7200k -bufsize 1835008 -packetsize 2048 -an -threads 2 -y -stats -f dvd NULL'
    ffmpegcmd2 = 'ffmpeg ' + file + ' -v error -c:v mpeg2video -r 25 -pix_fmt yuv420p -color_primaries bt470bg -color_trc gamma28 -colorspace bt470bg -me_method epzs -dc 9 -g 12 -bf 2 -cmp 2 -subcmp 2 -trellis 0 -flags +ilme+ildct -top -1 -s 720x576 -b:v 6400k -maxrate 7200k -bufsize 1835008 -packetsize 2048 -c:a ac3 -ac 2 -ar 48k -b:a 192k -async 1 -threads 2 -y -stats -vstats ' + output
elif profile != str(1) or str(2) or str(3) or str(4):
    print('Your choice must be a number between 1 and 4')
    exit()
else:
    print('Unexpected error!\nBYE!')
    exit()


def convert(ffmpegcmd1):
    print('\n\nConversion in progress. Pass 1. Please wait...\n\n')
    cmd = subprocess.run(ffmpegcmd1,shell=False,stdout=subprocess.PIPE)
    print('\n==================\n  PASS 1 = DONE!  \n==================\n')
    

def convert2(ffmpegcmd2):
    print('\n\nConversion in progress. Pass 2. Please wait...\n\n')
    cmd = subprocess.run(ffmpegcmd2,shell=False,stdout=subprocess.PIPE)
    print('\n==================\n  PASS 2 = DONE!  \n==================\n')
    exit()
    
convert(ffmpegcmd1)
convert2(ffmpegcmd2)
