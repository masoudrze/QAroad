from pathlib import Path

ROOT = Path(__file__).resolve().parent

EXCLUDED_DIRS = {
    ".git",
    ".QAvenv",
    "venv",
    ".venv",
    "__pycache__",
}

TEXT_EXTENSIONS = {
    ".py",
    ".json",
    ".txt",
    ".csv",
    ".xml",
    ".html",
    ".htm",
    ".css",
    ".js",
    ".ts",
    ".yaml",
    ".yml",
    ".ini",
    ".cfg",
    ".md",
    ".rst",
    ".sql",
    ".env",
}

# Encodingهایی که به ترتیب برای تشخیص امتحان می‌شوند
ENCODINGS_TO_TRY = [
    "utf-8",
    "utf-8-sig",
    "cp1256",
    "cp1252",
]


def is_utf8(path):
    """Check whether file can be decoded as UTF-8."""
    try:
        path.read_text(encoding="utf-8")
        return True
    except UnicodeDecodeError:
        return False


def detect_encoding(path):
    """Try to detect a suitable encoding."""
    data = path.read_bytes()

    for encoding in ENCODINGS_TO_TRY:
        try:
            data.decode(encoding)
            return encoding
        except UnicodeDecodeError:
            continue

    return None


def convert_to_utf8(path, source_encoding):
    """Convert file from source encoding to UTF-8."""
    data = path.read_bytes()
    text = data.decode(source_encoding)

    backup = path.with_suffix(path.suffix + ".bak")

    if not backup.exists():
        backup.write_bytes(data)

    path.write_text(
        text,
        encoding="utf-8",
        newline=""
    )


def main():
    checked = 0
    utf8_files = 0
    converted = 0
    failed = 0

    print(f"Scanning project:\n{ROOT}\n")
    print("=" * 70)

    for path in ROOT.rglob("*"):

        if not path.is_file():
            continue

        # Skip excluded directories
        if any(part in EXCLUDED_DIRS for part in path.parts):
            continue

        # Only inspect known text file types
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue

        checked += 1

        if is_utf8(path):
            utf8_files += 1
            continue

        print(f"\nNOT UTF-8:")
        print(f"  {path}")

        source_encoding = detect_encoding(path)

        if source_encoding is None:
            print("  ERROR: Could not detect encoding.")
            failed += 1
            continue

        print(f"  Detected encoding: {source_encoding}")

        try:
            convert_to_utf8(path, source_encoding)

            print("  Converted to UTF-8")
            print(f"  Backup: {path.with_suffix(path.suffix + '.bak')}")

            converted += 1

        except Exception as e:
            print(f"  ERROR: {e}")
            failed += 1

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    print(f"Files checked      : {checked}")
    print(f"Already UTF-8      : {utf8_files}")
    print(f"Converted to UTF-8 : {converted}")
    print(f"Failed             : {failed}")


if __name__ == "__main__":
    main()