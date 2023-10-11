from database.supabase import Supabase
from database.models.rating import Rating as Rating_DB
from services.rating.models.rating import Rating
from typing import List
from scipy.signal import savgol_filter

class Rating_Service:
    def __init__(self):
        self.supabase = Supabase()
    
    def create(self, score: int, store_number: int):
        if score < 0 or score is None or store_number < 0 or store_number is None:
            raise ValueError('Invalid score or store_number')
        
        data, count = self.supabase.client.table('Rating').upsert({'score': score, 'store_number': store_number}).execute()
        if count == 0:
            raise ValueError('Failed to create rating')

        return data[1][0]['id']
    
    def get_for_store(self, store_number: int, count: int, smooth: bool = False):
        if count is None:
            count = 10

        db_result: List[Rating_DB] = (self.supabase.client.from_('Rating').select('*').eq('store_number', store_number).limit(count).order('created_at', desc=True).execute()).data
        ratings = [Rating(rating['created_at'], rating['score']) for rating in db_result]

        if smooth:
            windowsize = round(len(ratings) / 2) if round(len(ratings) / 2) % 2 != 0 else round(len(ratings) / 2) - 1
            polynomial_order = 2 if len(ratings) <= 10 else 3 if len(ratings) <= 50 else 4

            scores = [rating.score for rating in ratings]
            scores_hat = savgol_filter(scores, windowsize, polynomial_order)

            for i, rating in enumerate(ratings):
                rating.score = scores_hat[i]

        return [rating.jsonify() for rating in ratings]
       