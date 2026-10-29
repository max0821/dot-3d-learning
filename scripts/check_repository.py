#!/usr/bin/env python3
"""Offline checks for Markdown and relative links in this illustrated learning repository. Python 3.9+. No Blender required."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


def check(root):
    errors = []
    notes = sorted((root / 'experiments').glob('*/NOTES.md'))
    if len(notes) != 61:
        errors.append(f'Expected 61 experiment notes; found {len(notes)}')
    private = re.compile(r'(?:Sentinel_|libfile_|CalpicoFile_|file_id|/workspace/|/home/agent/|/tmp/)')
    count = 0
    for page in sorted(root.rglob('*.md')):
        content = page.read_text(encoding='utf-8')
        if private.search(content):
            errors.append(f'Potential internal identifier/path: {page.relative_to(root)}')
        # Repository uses simple inline links; URLs with parenthesized paths use <...>.
        for match in re.finditer(r'!?\[[^\]]*\]\((<[^>]*>|[^\s)]+)(?:\s+"[^"]*")?\)', content):
            target = match.group(1).strip('<>')
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            dest = (page.parent / unquote(parsed.path)).resolve()
            if not dest.is_relative_to(root):
                errors.append(f'Link outside repository: {page.relative_to(root)} -> {target}')
            elif not dest.exists():
                errors.append(f'Missing link: {page.relative_to(root)} -> {target}')
            count += 1
    return errors, len(notes), count


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    errors, notes, links = check(root)
    print(f'Experiment notes: {notes}; local links checked: {links}')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        raise SystemExit(1)
    print('PASS: Markdown/link checks only; binary images not read as text; no 3D or external URL validation.')
