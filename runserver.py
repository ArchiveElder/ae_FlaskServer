import pymysql
from flask import Flask

from model.FoodDao import FoodDao
from model.FoodClassDao import FoodClassDao
from service.FoodService import FoodService
from service.FoodClassService import FoodClassService
from view import create_endpoints


class Services:
    pass

################################
# Create App
################################
def create_app(test_config=None):
    app = Flask(__name__)

#    CORS(app)

    if test_config is None:
        app.config.from_pyfile("config.py")
    else:
        app.config.update(test_config)

    database = pymysql.connect(host=app.config['HOST'],user=app.config['USER'], password=app.config['PASSWORD'],
                             db=app.config['DATABASE'], charset='utf8', port=app.config['PORT'])

    cur = database.cursor()

    # Persistence Layer
    foodDao = FoodDao(cur)
    foodclassDao = FoodClassDao(cur)

    # Businsess Layer
    services = Services
    services.foodService = FoodService(foodDao)
    services.foodClassService = FoodClassService(foodclassDao)

    #cur.execute("select * from record")
    #while(True):
    #    row = cur.fetchone() #row에 커서(테이블 셀렉트)를 한줄 입력하고 다음줄로 넘어감
    #    if row == None:
    #        break
    #    print(row)

    ## Persistenace Layer

    ## Business Layer


    ## 엔드포인트들을 생성
    create_endpoints(app, services)
    database.close()
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=8080)