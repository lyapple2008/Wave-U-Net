import librosa
from Predict import ex
import os
import logging

rootdir = "E:/MusicVocalSeparation/TestSets"
# rootdir = "E:/MusicVocalSeparation/test"
savedir = "E:/MusicVocalSeparation/wave-u-net_full_44KHz"
modeldir = ""

subdirs = ["流行", "摇滚", "说唱", "民谣", "其它"]

# attach log
logging.basicConfig(level=logging.DEBUG, filename='batch_process.log', filemode='a')
logger = logging.getLogger('batch_process')
logger.handles = []
ch = logging.StreamHandler()
formatter = logging.Formatter('[%(levelname).1s] %(name)s >> "%(message)s"')
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel('INFO')

ex.logger = logger

for subdir in subdirs:
    indir = os.path.join(rootdir, subdir)
    files = librosa.util.find_files(indir, ext='mp3', recurse=False)
    outdir = os.path.join(savedir, subdir)

    for file in files:
        logger.info("----input_path: {}".format(file.encode('gbk', 'ignore')))
        logger.info("----output_path: {}".format(outdir.encode('gbk', 'ignore')))
        cmd = "python Predict.py with input_path=\"%s\" output_path=\"%s\" cfg.full_44KHz" % (file, outdir)
        os.system(cmd)
