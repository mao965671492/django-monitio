#!/usr/bin/env python
import os
import sys

import sys

# Add ../monitio to sys.path

sys.path = [ os.path.join(os.path.dirname(__file__), '..'), ] + sys.path

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
