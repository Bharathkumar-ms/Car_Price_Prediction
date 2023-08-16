from flask import Flask,request,render_template
from car.pipeline.prediction import CustomData,PredictPipeline

application=Flask(__name__)

app=application


## Route for a home page

@app.route('/')
def index():
    return '<h1>Welcome to the home page</h1>'

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('index.html')
    else:
        data=CustomData(
            Present_Price=float(request.form.get('Present_Price')),
            Kms_Driven=float(request.form.get('Kms_Driven')),
            Owner=float(request.form.get('Owner')),
            age=float(request.form.get('age')),
            Fuel_Type=request.form.get('Fuel_Type'),
            Seller_Type=request.form.get('Seller_Type'),
            Transmission=request.form.get('Transmission')

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('index.html',results=results[0])
    

if __name__=="__main__":
    app.run(debug=True)        





