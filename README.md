# uv-tool

`uv-tool` is a lightweight command-line helper that streamlines the management of "global" virtual environments created with [`uv`](https://github.com/astral-sh/uv). Environments are stored under `~/.uv-tool-envs` so they can be reused across multiple projects without rebuilding them each time.

## Prerequisites

- Python 3.8 or newer
- The [`uv`](https://docs.astral.sh/uv/getting-started/installation/) executable available on your `PATH`

## Installation

Install `uv-tool` from a local clone of the repository:

```bash
# Clone the repository (if you have not already)
git clone https://github.com/SimoneMartino98/uv-tools.git
cd uv-tools

uv tool install .
```

## Uninstallation

Remove `uv-tool` from your system with:

```bash
uv tool uninstall uv-tool
```

Environments created in `~/.uv-tool-envs` are not deleted automatically; delete them manually if you no longer need them.

## Usage

After installation, the main entry point is `uv-tool`. All operations happen through the subcommands described below.

### Create a new global environment

```bash
uv-tool create <environment-name> [--python <version>]
```

- `<environment-name>`: name of the environment.
- `--python <version>` (optional): select the Python version to use (for example `3.11`). When omitted, the default `uv` interpreter is used.

### List available environments

```bash
uv-tool list
```

Displays a table with the environment name, detected Python version, and last modified timestamp.

### Remove an environment

```bash
uv-tool remove <environment-name>
```

Recursively deletes the selected environment folder from `~/.uv-tool-envs`. The operation cannot be undone, so make sure no projects still depend on that environment.