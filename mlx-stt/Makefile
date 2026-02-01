install:
	bash mlx-stt/install.sh

i: install

metadata:
	uv run skill-metadata.py

m: metadata

test:
	uv run mlx-stt/mlx-stt.py ~/Music/audio.mp3

tags:
	@echo "latest,asr,stt,audio,glm,glm-asr,glm-asr-nano-2512,macOS,mlx,mlx-audio"

