# oop_intro.py
# 👉 Defines a blueprint for a Note object
class Note:
    # 👉 Constructor (runs when object is created)
    def __init__(self, language: str, title: str, content: str):
        self.language = language # 👉 Refers to the specific instance of the object
        self.title = title
        self.content = content

    def summary(self):
        return f"{self.language} - {self.title}"

    def word_count(self):
        return len(self.content.split())

    # 👉 Function tied to the object
    def display(self):
        print("\n--- Note ---")
        print(f"Language: {self.language}")
        print(f"Title: {self.title}")
        print("Content:")
        print(self.content)

# 👉 Creating instances of the Note class
note1 = Note("Python", "My First Note", "This is the content of my first note.")
note2 = Note("JavaScript", "My Second Note", "This is the content of my second note.")

# 👉 Using methods of the Note class
print(note1.summary())
print(note1.word_count())
note1.display()

print(note2.summary())
print(note2.word_count())
note2.display()