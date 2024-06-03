from dataclasses import dataclass

@dataclass
class WordPressPage:
    id: int
    title: str
    content: str
    slug: str
    excerpt: str = ''
    status: str = 'publish'

    def __post_init__(self):
        # Automatically generate slug if not provided
        if not self.slug:
            self.slug = self.title.lower().replace(" ", "-")
