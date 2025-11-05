'''my file name is 
"0_male_0.wav", "0_male_2.wav"... "0_male_30.wav"... 
"1_male_0.wav", "1_male_2.wav"... "1_male_30.wav"... 
"8_male_0.wav", "8_male_2.wav"... "8_male_30.wav"

when I wav.read(files) I want to read them in a sorted torder, i.e., "0_male_0.wav"
"0_male_1.wav"
"0_male_2.wav" ...
"0_male_30.wav"
"1_male_0.wav"
"1_male_1.wav"
"1_male_2.wav" ...
"1_male_30.wav"
so this is how I did it.

Just take all files start with "0_*" as an example. Others you can just put it in a loop
'''

import scipy.io.wavfile as wav
import glob 
from os.path import isfile, join

#get all the file names in file_names. THe order is totally messed up
file_names = [f for f in listdir(audio_folder_dir) if isfile(join(audio_folder_dir, f)) and '.wav' in f] 
#find files that belongs to "0_*" group
filegroup0 = glob.glob(audio_folder_dir+'/0_*')
#now you get sorted files in group '0_*' by the last number in the filename
filegroup0 = sorted(filegroup0, key=getKey)

def getKey(filename):
    file_text_name = os.path.splitext(os.path.basename(filename))  #you get the file's text name without extension
    file_last_num = os.path.basename(file_text_name[0]).split('_')  #you get three elements, the last one is the number. You want to sort it by this number
    return int(file_last_num[2])
