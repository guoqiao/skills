#!/bin/bash

set -ueo pipefail

# path to input audio/video path
input=$1

# path/to/audio.wav
wav_path=$2

# convert to wav for transcription
ffmpeg -y -loglevel error -i "${input}" -vn -ac 1 -ar 16000 -af loudnorm -c:a pcm_s16le "${wav_path}"
