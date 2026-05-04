import os
from pathlib import Path
from typing import List, Optional


class FilePathFinder:
    """Utility class to find files in a directory tree."""

    def __init__(self, root_dir: Optional[str] = None):
        """
        Initialize the FilePathFinder.

        Args:
            root_dir: Root directory to search from. Defaults to current working directory.
        """
        self.root_dir = Path(root_dir) if root_dir else Path.cwd()

    def find_by_name(self, filename: str, recursive: bool = True) -> List[Path]:
        """
        Find files by exact name.

        Args:
            filename: Name of the file to find
            recursive: Whether to search subdirectories

        Returns:
            List of Path objects matching the filename
        """
        results = []
        pattern = "**/" + filename if recursive else filename

        for file_path in self.root_dir.glob(pattern):
            if file_path.is_file():
                results.append(file_path)

        return results

    def find_by_pattern(self, pattern: str, recursive: bool = True) -> List[Path]:
        """
        Find files by glob pattern.

        Args:
            pattern: Glob pattern (e.g., "*.fasta", "data/*.txt")
            recursive: Whether to search subdirectories

        Returns:
            List of Path objects matching the pattern
        """
        results = []
        search_pattern = "**/" + pattern if recursive else pattern

        for file_path in self.root_dir.glob(search_pattern):
            if file_path.is_file():
                results.append(file_path)

        return results

    def find_by_extension(self, extension: str, recursive: bool = True) -> List[Path]:
        """
        Find files by extension.

        Args:
            extension: File extension (e.g., ".fasta", "fasta")
            recursive: Whether to search subdirectories

        Returns:
            List of Path objects with the given extension
        """
        if not extension.startswith("."):
            extension = "." + extension

        return self.find_by_pattern("*" + extension, recursive=recursive)

    def find_first(self, filename: str, recursive: bool = True) -> Optional[Path]:
        """
        Find the first occurrence of a file.

        Args:
            filename: Name of the file to find
            recursive: Whether to search subdirectories

        Returns:
            Path object if found, None otherwise
        """
        results = self.find_by_name(filename, recursive=recursive)
        return results[0] if results else None

    def exists(self, filename: str, recursive: bool = True) -> bool:
        """Check if a file exists."""
        return self.find_first(filename, recursive=recursive) is not None


# Example usage
if __name__ == "__main__":
    finder = FilePathFinder()

    # Find specific files
    Wa_fasta = finder.find_first("Wa.fasta")
    Wuhan_fasta = finder.find_first("Wuhan.fasta")

    print(f"Wa: {Wa_fasta}")
    print(f"Wuhan: {Wuhan_fasta}")

    # Find all FASTA files
    all_fasta = finder.find_by_extension("fasta")
    print(f"All FASTA files: {all_fasta}")
