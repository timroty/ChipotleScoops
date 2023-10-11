import datetime

class Rating:
  def __init__(self, created_at: datetime, score: int = 0):
        self.created_at = created_at
        self.score = score
  
  def jsonify(self):
    return {
      "created_at": self.created_at,
      "score": self.score
    }
