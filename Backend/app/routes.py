from flask import Blueprint, request, jsonify

from services.restaurant.restaurant_service import Restaurant_Service

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