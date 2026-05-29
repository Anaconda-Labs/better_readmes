#!/usr/bin/env python3
"""Check the links in this repository's Markdown files.

Standard library only, so it runs in the pinned environment with no extra
packages. By default it requests every external (http or https) link and
reports any that do not respond with a success or redirect status. Pass
--list to print the links it finds without making any network requests,
which is handy for a quick sanity check or for running offline.

Usage:
    python tools/check_links.py            # check links in all .md files
    python tools/check_links.py --list     # just list the links, no network
    python tools/check_links.py README.md  # check a specific file
"""

import re
import sys
import urllib.request
import urllib.error
from pathlib import Path

# Matches the URL inside a Markdown link of the form [text](url).
LINK_PATTERN = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+)\)")


def find_markdown_files(args):
    """Return the list of Markdown files to scan."""
    paths = [a for a in args if not a.startswith("-")]
    if paths:
        return [Path(p) for p in paths]
    return sorted(Path(".").rglob("*.md"))


def extract_links(text):
    """Return every external link found in the given text."""
    return LINK_PATTERN.findall(text)


def check_link(url):
    """Return (ok, detail) for a single URL."""
    request = urllib.request.Request(url, method="HEAD")
    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            return True, response.status
    except urllib.error.HTTPError as error:
        # Some servers reject HEAD but accept GET, so retry once with GET.
        if error.code in (403, 405):
            try:
                with urllib.request.urlopen(url, timeout=10) as response:
                    return True, response.status
            except Exception as inner:
                return False, repr(inner)
        return False, error.code
    except Exception as error:
        return False, repr(error)


def main():
    args = sys.argv[1:]
    list_only = "--list" in args
    files = find_markdown_files(args)

    if not files:
        print("No Markdown files found.")
        return 0

    failures = 0
    for path in files:
        text = path.read_text(encoding="utf-8")
        links = extract_links(text)
        for url in links:
            if list_only:
                print(f"{path}: {url}")
                continue
            ok, detail = check_link(url)
            status = "ok" if ok else "BROKEN"
            print(f"[{status}] {url} ({detail})")
            if not ok:
                failures += 1

    if not list_only and failures:
        print(f"\n{failures} link(s) need attention.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
