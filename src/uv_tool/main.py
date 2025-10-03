#!/usr/bin/env python3

import argparse
import subprocess
from .config import get_global_envs_dir

def cmd_create(args):
    envs_dir = get_global_envs_dir()
    target_dir = envs_dir / args.name

    cmd = ["uv", "venv", str(target_dir)]
    if args.python:
        cmd.extend(["--python", args.python])

    subprocess.run(cmd, check=True)

def main():
    parser = argparse.ArgumentParser(prog="uv-tool", description="Manage global envs with uv")
    subparsers = parser.add_subparsers(dest="command", required=True)

    create_parser = subparsers.add_parser("create", help="Create a new global environment")
    create_parser.add_argument("name", help="Name of the environment")
    create_parser.add_argument("--python", help="Python version to be installed", required=False)
    create_parser.set_defaults(func=cmd_create)

    args = parser.parse_args()
    args.func(args)
