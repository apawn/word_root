"""Keep offline dictionary records below GitHub's per-file size limit."""
from pathlib import Path


def write_source_archive(lines, directory, max_bytes=40 * 1024 * 1024):
    """Split UTF-8 JSONL on record boundaries, preserving bytes and order."""
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    paths = []
    stream = None
    size = 0
    try:
        for line in lines:
            data = line.encode('utf-8') if isinstance(line, str) else line
            if len(data) > max_bytes:
                raise ValueError('A dictionary record exceeds the shard size limit')
            if stream is None or size + len(data) > max_bytes:
                if stream is not None:
                    stream.close()
                path = directory / f'part-{len(paths) + 1:03d}.jsonl'
                paths.append(path)
                stream = path.open('wb')
                size = 0
            stream.write(data)
            size += len(data)
    finally:
        if stream is not None:
            stream.close()
    for path in directory.glob('part-*.jsonl'):
        if path not in paths:
            path.unlink()
    return paths
