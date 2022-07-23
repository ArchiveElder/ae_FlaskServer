import json
from keras.models import load_model
from keras import utils
import numpy as np
import os

my_model = load_model('./trainedModel/model_trained.h5')
food_list = []
class FoodClassDao:

    def __init__(self, database):
        self.db = database


    def predictFood(self, filename):
        fl = self.db.execute("SELECT * FROM food101")
        print(">>food list (from RDS) is :")
        while (True):
            row = self.db.fetchone()
            if row == None:
                break
            food_list.append(row[1])

        print(food_list)

        print('>>uploaded filename (from USER) is : ' + filename)

        img = utils.load_img('./static/'+filename, grayscale=False, color_mode='rgb', target_size=(299,299))
        img = utils.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img /= 255.

        pred = my_model.predict(img)
        index = np.argmax(pred)

        food_list.sort()
        pred_value = food_list[index]
        print('>>classification result is  : ' +pred_value)

        if os.path.exists('./static/'+filename):
            os.remove('./static/'+filename)
            print('>>파일이 로컬에서 제거되었습니다.<<<')
        return pred_value

    def foodNutrient(self,food_type):
        nutrientDto={}
        sql = "SELECT * FROM nutrient101 WHERE food_type = %s"
        self.db.execute(sql,food_type)
        while (True):
            row = self.db.fetchone()
            if row == None:
                break
            #print(row)
            # name = row[2]
            # capacity = row[3]
            # calory = row[4]
            # carb = row[5]
            # pro = row[6]
            # fat = row[7]
            nutrientDto['name']=row[2]
            nutrientDto['capacity'] = row[3]
            nutrientDto['calory'] = row[4]
            nutrientDto['carb'] = row[5]
            nutrientDto['pro'] = row[6]
            nutrientDto['fat'] = row[7]
        return json.dumps(nutrientDto, ensure_ascii=False, indent=4)
