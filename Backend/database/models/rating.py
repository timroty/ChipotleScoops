import datetime

class Rating:
  def __init__(self, id: int, created_at: datetime, score: int = 0, store_number: int = 0):
        self.id = id
        self.created_at = created_at
        self.score = score
        self.store_number = store_number
        