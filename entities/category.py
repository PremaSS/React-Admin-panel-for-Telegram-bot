class Category:
    def __init__(self, name, id, parent_category_id=None):
        self.name: str = name
        self.id: str = id
        self.parent_category_id: str = parent_category_id

    def __str__(self):
        return f"{self.name} {self.id} {self.parent_category_id}"
