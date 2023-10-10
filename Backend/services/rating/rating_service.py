import json
from database.supabase import Supabase

class Rating_Service:
    def __init__(self):
        self.supabase = Supabase()
    
    def create(self, score: int):
        data, count = self.supabase.client.table('Rating').upsert({'score': score}).execute()
        return data
    
    def get_for_store(self, store_number: int, count: int):
        if count is None:
            count = 10

        result = self.supabase.client.from_('Rating').select('*').eq('store_number', store_number).limit(count).order('created_at', desc=True).execute()
        return result.data
       