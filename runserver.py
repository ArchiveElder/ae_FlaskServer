import pymysql
from flask import Flask


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
    cur.execute("select * from record")
    while(True):
        row = cur.fetchone() #row에 커서(테이블 셀렉트)를 한줄 입력하고 다음줄로 넘어감
        if row == None:
            break
        print(row)

    ## Persistenace Layer

    ## Business Layer


    ## 엔드포인트들을 생성
    #create_endpoints(app, services)

    return app
