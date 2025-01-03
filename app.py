# from flask import Flask,request,render_template
# import pickle
# import numpy as np

# app = Flask(__name__)
# model = pickle.load(open('model.pkl','rb'))
# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict',methods=['GET','POST'])
# def predict():
#     if request.method == 'POST':
#         gender=request.form['gender']
#         married=request.form['married']
#         dependents=request.form['dependents']
#         education=request.form['education']
#         employed=request.form['employed']
#         credit=request.form['credit']
#         area=request.form['area']
#         loan=request.form['loan']
#         ApplicantIncom=request.form['ApplicantIncom']
#         CoapplicantIncom=request.form['CoapplicantIncom']
#         LoanAmount=request.form['LoanAmount']
#         LoanAmount_Term=request.form['LoanAmount_Term']
#         # gender
#         if(gender=='Male'):
#             male=1
#         else:
#             male=0
#         # Married
#         if(married=='Yes'):
#             married_yes=1
#         else:
#             married_yes=0
#         #dependent
#         if(dependents=='1'):
#             dependents_1=1
#             dependents_2=0
#             dependents_3=0
#         elif(dependents=='2'):
#             dependents_1=0
#             dependents_2=1
#             dependents_3=0
#         elif(dependents=='3+'):
#             dependents_1=0
#             dependents_2=0
#             dependents_3=1
#         else:
#             dependents_1=0
#             dependents_2=1
#             dependents_3=0
#         # education
#         if(education=='Not Graduate'):
#             not_graduate=1
#         else:
#             not_graduate=0
#         # Employed
#         if(employed=='Yes'):
#             employed_yes=1
#         else:
#             employed_yes=0
#         # property area
#         if(area=='Semiurban'):
#             semiurban=1
#             urban=0
#         elif(area=='Urban'):
#             semiurban=0
#             urban=1
#         else:
#             semiurban=0
#             urban=0
#         # Loan status
#         if(loan=='Y'):
#             loan_y=1
#         else:
#             loan_y=0
#         ApplicantIncomelog = np.log(ApplicantIncom)
#         totalincomelog = np.log(ApplicantIncom+CoapplicantIncom)
#         LoanAmountlog = np.log(LoanAmount)
#         Loan_Amount_Termlog = np.log(LoanAmount_Term)

#         prediction = model.predict([[credit,ApplicantIncomelog,LoanAmountlog,Loan_Amount_Termlog,totalincomelog,male,married_yes,dependents_1,dependents_2,dependents_3,not_graduate,employed_yes,semiurban,urban]])

#         #print prediction
#         if(prediction=='N'):
#             prediction='No'
#         else:
#             prediction='Yes'

#     else:
#         return render_template('predict.html',prediction_text='Loan Status is {}'.format(predict))

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, request, render_template
# import pickle
# import numpy as np

# app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['GET', 'POST'])
# def predict():
#     prediction_text = "Please fill out the form to get a prediction."  # Default message for GET requests or errors
    
#     if request.method == 'POST':
#         try:
#             # Fetch form data and handle conversions
#             gender = request.form.get('gender', '')
#             married = request.form.get('married', '')
#             dependents = request.form.get('dependents', '')
#             education = request.form.get('education', '')
#             employed = request.form.get('employed', '')
#             credit = float(request.form.get('credit', 0))
#             area = request.form.get('area', '')
#             ApplicantIncom = float(request.form.get('ApplicantIncom', 0))
#             CoapplicantIncom = float(request.form.get('CoapplicantIncom', 0))
#             LoanAmount = float(request.form.get('LoanAmount', 0))
#             LoanAmount_Term = float(request.form.get('LoanAmount_Term', 0))

#             # Gender
#             male = 1 if gender == 'Male' else 0

#             # Married
#             married_yes = 1 if married == 'Yes' else 0

#             # Dependents
#             dependents_1 = dependents_2 = dependents_3 = 0
#             if dependents == '1':
#                 dependents_1 = 1
#             elif dependents == '2':
#                 dependents_2 = 1
#             elif dependents == '3+':
#                 dependents_3 = 1

#             # Education
#             not_graduate = 1 if education == 'Not Graduate' else 0

#             # Employed
#             employed_yes = 1 if employed == 'Yes' else 0

#             # Property area
#             semiurban = 1 if area == 'Semiurban' else 0
#             urban = 1 if area == 'Urban' else 0

#             # Log transformations
#             ApplicantIncomelog = np.log(ApplicantIncom + 1)  # Add 1 to avoid log(0)
#             totalincomelog = np.log(ApplicantIncom + CoapplicantIncom + 1)
#             LoanAmountlog = np.log(LoanAmount + 1)
#             Loan_Amount_Termlog = np.log(LoanAmount_Term + 1)

#             # Prediction
#             prediction = model.predict([[credit, ApplicantIncomelog, LoanAmountlog, Loan_Amount_Termlog,
#                                           totalincomelog, male, married_yes, dependents_1, dependents_2, dependents_3,
#                                           not_graduate, employed_yes, semiurban, urban]])
            
#             # Map prediction result
#             prediction_text = "Loan Status is Yes" if prediction[0] == 1 else "Loan Status is No"

#         except Exception as e:
#             prediction_text = f"Error: {str(e)}"  # Display error for debugging

#     return render_template('predict.html', prediction_text=prediction_text)

# if __name__ == "__main__":
#     app.run(debug=True)



from flask import Flask,request,render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction_text = "Please fill out the form to get a prediction."
    if request.method == 'POST':
        try:
            # Fetch form data
            gender = request.form.get('gender', '')
            married = request.form.get('married', '')
            dependents = request.form.get('dependents', '')
            education = request.form.get('education', '')
            employed = request.form.get('employed', '')
            credit = float(request.form.get('credit', 0))
            ApplicantIncom = float(request.form.get('ApplicantIncom', 0))
            CoapplicantIncom = float(request.form.get('CoapplicantIncom', 0))
            LoanAmount = float(request.form.get('LoanAmount', 0))
            LoanAmount_Term = float(request.form.get('LoanAmount_Term', 0))
            
            # Feature Engineering
            male = 1 if gender == 'Male' else 0
            married_yes = 1 if married == 'Yes' else 0
            dependents_1 = dependents_2 = dependents_3 = 0
            if dependents == '1': dependents_1 = 1
            elif dependents == '2': dependents_2 = 1
            elif dependents == '3+': dependents_3 = 1
            not_graduate = 1 if education == 'Not Graduate' else 0
            employed_yes = 1 if employed == 'Yes' else 0
            ApplicantIncomelog = np.log(ApplicantIncom + 1)
            totalincomelog = np.log(ApplicantIncom + CoapplicantIncom + 1)
            LoanAmountlog = np.log(LoanAmount + 1)
            Loan_Amount_Termlog = np.log(LoanAmount_Term + 1)
            
            # Input features for prediction
            input_features = [credit, ApplicantIncomelog, LoanAmountlog, Loan_Amount_Termlog,
                              totalincomelog, male, married_yes, dependents_1, dependents_2, 
                              dependents_3, not_graduate]

            # Prediction
            prediction = model.predict([input_features])
            prediction_text = "Loan Status is Yes" if prediction[0] == 1 else "Loan Status is No"

        except Exception as e:
            prediction_text = f"Error: {str(e)}"

    return render_template('predict.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
