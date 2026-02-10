#!/usr/bin/env -S uv --script
# /// script
# requires-python = "==3.12"
# dependencies = [
#     "misaki>=0.9.4",
# ]
# ///

import argparse
import shlex
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# DEFAULT_MODEL = "mlx-community/Kokoro-82M-bf16"
DEFAULT_MODEL = "mlx-community/Qwen3-TTS-12Hz-1.7B-VoiceDesign-bf16"
MODEL_URL = "https://github.com/Blaizzy/mlx-audio?tab=readme-ov-file#text-to-speech-tts"
MLX_AUDIO_CLI_TOOL = "mlx_audio.tts.generate"

CLI_TOOLS = [
    "brew",
    "ffmpeg",
    "uv",
    MLX_AUDIO_CLI_TOOL,
]


def check_deps() -> None:
    """Check if all dependencies are installed."""
    for tool in CLI_TOOLS:
        if not shutil.which(tool):
            raise FileNotFoundError(f"Dependency `{tool}` not found, please run `bash install.sh` to install.")


def run_cmd(cmd: str | list, verbose: bool = False):
    if isinstance(cmd, str):
        cmdline = cmd
        shell = True
    else:
        cmd = [str(arg) for arg in cmd if arg]
        cmdline = shlex.join(cmd)
        shell = False
    if verbose:
        print(f"running cmd: {cmdline}")
        return subprocess.run(cmd, check=True, shell=shell, stdout=sys.stdout, stderr=sys.stderr)
    else:
        return subprocess.run(cmd, check=True, shell=shell, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def run(
    text: str = "Hello, Human!",
    model: str = DEFAULT_MODEL,
    out_dir: Path = None,
    audio_stem: str = "audio",
    audio_format: str = "wav",
    voice: str = "af_heart",
    verbose: bool = False,
) -> None:
    """Invoke mlx_audio.stt.generate and return path to transcript."""
    out_dir = Path(out_dir or tempfile.mkdtemp()).expanduser()
    out_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        MLX_AUDIO_CLI_TOOL,
        f"--model={model}",
        f"--text={text}",
        f"--voice={voice}",
        f"--file_prefix={out_dir}/{audio_stem}",
        f"--audio_format={audio_format}",
    ]
    run_cmd(cmd, verbose=verbose)
    return Path(f"{out_dir}/{audio_stem}.{audio_format}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="text-to-speech on macOS with mlx-audio.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("text", help="Text to synthesize")
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Verbose output.",
    )
    parser.add_argument(
        "-m", "--model",
        default=DEFAULT_MODEL,
        help=f"Model to use, more choices: {MODEL_URL}",
    )
    parser.add_argument(
        "-o", "--out_dir", type=Path,
        help="Output directory.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    audio_path = run(
        model=args.model,
        text=args.text,
        out_dir=args.out_dir,
        verbose=args.verbose,
    )
    print(audio_path)


if __name__ == "__main__":
    check_deps()
    main()
