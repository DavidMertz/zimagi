#!/usr/bin/env python3
import os
import sys

if __name__ == "__main__":
    from systems.command import cli
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "services.cli.settings")
    cli.execute(sys.argv)