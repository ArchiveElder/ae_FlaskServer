
from flask import request, jsonify, current_app, Response, g
from flask.json import JSONEncoder
from functools import wraps


## Default JSON encoder는 set를 JSON으로 변환할 수 없다.
## 그럼으로 커스텀 엔코더를 작성해서 set을 list로 변환하여
## JSON으로 변환 가능하게 해주어야 한다.
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)

        return JSONEncoder.default(self, obj)


def create_endpoints(app, services):
    app.json_encoder = CustomJSONEncoder

    foodService = services.foodService

    @app.route("/ping", methods=['GET'])
    def ping():
        return "pong"

    @app.route("/api/foodrecommend", methods=['POST'])
    def recommend():
        return foodService.foodRecommend(request.get_json()['ingredients'])









