"""
OOP Progression: Enhanced Note Class

Demonstrates:
- Class structure
- Methods (behavior)
- Data encapsulation
- Utility functions
"""


class Note:
    def __init__(self, language: str, title: str, content: str):
        self.language = language
        self.title = title
        self.content = content
        self.tags: list[str] = []

    # ---------------------------
    # Display Methods
    # ---------------------------
    def display(self):
        print("\n" + "=" * 30)
        print(f"Language: {self.language}")
        print(f"Title: {self.title}")
        print("\nContent:")
        print(self.content)
        print("\nTags:", ", ".join(self.tags) if self.tags else "None")
        print("=" * 30)

    def summary(self) -> str:
        return f"{self.language} - {self.title}"

    # ---------------------------
    # Content Methods
    # ---------------------------
    def word_count(self) -> int:
        return len(self.content.split())

    def contains(self, keyword: str) -> bool:
        return keyword.lower() in self.content.lower()

    def update_content(self, new_content: str):
        self.content = new_content

    def preview(self, length: int = 50) -> str:
        return self.content[:length] + "..." if len(self.content) > length else self.content

    # ---------------------------
    # Tag Methods
    # ---------------------------
    def add_tag(self, tag: str):
        tag_clean = tag.strip().lower()
        if tag_clean and tag_clean not in self.tags:
            self.tags.append(tag_clean)

    def remove_tag(self, tag: str):
        if tag in self.tags:
            self.tags.remove(tag)

    # ---------------------------
    # Utility Methods
    # ---------------------------
    def to_dict(self) -> dict:
        return {
            "language": self.language,
            "title": self.title,
            "content": self.content,
            "tags": self.tags
        }

    def __str__(self) -> str:
        return f"{self.language} | {self.title}"


# ---------------------------
# Demo / Test
# ---------------------------
if __name__ == "__main__":
    note = Note(
        language="Python",
        title="Decorators",
        content="Decorators wrap functions and allow reusable behavior."
    )

    # Add tags
    note.add_tag("python")
    note.add_tag("functions")
    note.add_tag("decorators")

    # Display full note
    note.display()

    # Other methods
    print("\nSummary:", note.summary())
    print("Word count:", note.word_count())
    print("Contains 'wrap':", note.contains("wrap"))
    print("Preview:", note.preview(30))

    # Convert to dict
    print("\nAs dict:", note.to_dict())

    # Print object
    print("\nPrint object:", note)