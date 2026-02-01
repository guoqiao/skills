install:
	bash mlx-stt/install.sh

i: install

metadata:
	uv run skill-metadata.py

m: metadata

test:
	uv run mlx-stt/mlx-stt.py ~/Music/audio.mp3

