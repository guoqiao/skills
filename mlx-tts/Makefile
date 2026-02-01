name: mlx-tts

install:
	bash ${name}/install.sh

i: install

metadata:
	uv run skill-metadata.py

m: metadata

test:
	uv run ${name}/mlx-tts.py "Stay Hungry, Stay Foolish."

tags:
	@echo "latest,audio,macOS,mlx,mlx-audio,tts,text-to-speech"
