from flask import Blueprint, request, jsonify

from services.restaurant.restaurant_service import Restaurant_Service
from services.rating.rating_service import Rating_Service

bp = Blueprint('api', __name__)

@bp.route('/', methods=['GET'])
def default():
    return jsonify({'result': True})

#Restaurant
@bp.route('/restaurant/search', methods=['post'])
async def restaurant_search():
    restaurant_service = Restaurant_Service()

    body = request.json
    latitude = body['latitude'] or 0.0
    longitude = body['longitude'] or 0.0

    search_result = await restaurant_service.search(latitude, longitude)

    return jsonify(search_result)

@bp.route('/restaurant/search/zipcode', methods=['post'])
async def restaurant_search_zipcode():
    restaurant_service = Restaurant_Service()

    body = request.json
    zipcode = body['zipcode'] or "00000"

    search_result = await restaurant_service.search_zipcode(zipcode)

    return jsonify(search_result)

#Rating
@bp.route('/rating', methods=['post'])
def create_rating():
    rating_service = Rating_Service()

    body = request.json
    result = rating_service.create(body['score'], body['store_number'])

    return jsonify(result)

@bp.route('/rating/<store_number>', methods=['get'])
def get_ratings_for_store(store_number):
    rating_service = Rating_Service()

    count = request.args.get('count')
    smooth = request.args.get('smooth')
    result = rating_service.get_for_store(store_number, count, smooth)

    return jsonify(result)