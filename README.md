# Manim Online Starter

This repo is set up to run in two ways:

1. **Binder** for quick browser-based notebooks.
2. **GitHub Codespaces** for a more stable development environment.

## What is included

- `environment.yml` for Binder / Conda setup
- `postBuild` to install Jupyter kernel and Manim notebook extras
- `.devcontainer/devcontainer.json` for Codespaces
- `scenes/hello_manim.py` sample Manim scene
- `notebooks/QuickStart.ipynb` sample notebook using `%%manim`

## Binder

After pushing this repo to GitHub, open Binder and point it at your repository.

Binder will build from `environment.yml` and run the commands in `postBuild`.

## Codespaces

Open the GitHub repo and create a Codespace. The dev container configuration will install the same base toolchain and recommended VS Code extensions.

## First checks

In a terminal, test:

```bash
python --version
manim --version
ffmpeg -version
jupyter kernelspec list
```

## Render a sample scene

```bash
manim -pql scenes/hello_manim.py HelloManim
```

## Notes

Binder sessions are temporary. Codespaces are much better for ongoing work.
