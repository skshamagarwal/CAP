from django.shortcuts import render
from home import randomForest as rf
from django.contrib import messages

# Create your views here.
def index(request):
    object={"color": "black"}
    return render(request, 'index.html', object)

def target(request):
    data_patient = {}
    data_patient['age'] = float(request.POST['age'])
    data_patient['sex'] = float(request.POST['sex'])
    data_patient['cp'] = float(request.POST['cp'])
    data_patient['trestbps'] = float(request.POST['trestbps'])
    data_patient['chol'] = float(request.POST['chol'])
    data_patient['fbs'] = float(request.POST['fbs'])
    data_patient['restecg'] = float(request.POST['restecg'])
    data_patient['thalach'] = float(request.POST['thalach'])
    data_patient['oldpeak'] = float(request.POST['oldpeak'])
    data_patient['slope'] = float(request.POST['slope'])
    data_patient['ca'] = float(request.POST['ca'])
    data_patient['thal'] = float(request.POST['thal'])
    data_patient['exang'] = float(request.POST['exang'])
    
    result = rf.tree(data_patient, 0, 0)
    if result == 1:
        color = 'green'
        messages.info(request,'Patient has very low chances of suffering from any Cardiovascular Disease at the moment :D')
    else:
        color = 'red'
        messages.info(request,'Patient has high chances of suffering from Cardiovascuar Disease. Please consult an doctor ASAP!!')
    
    object = {"color": color}
    return render(request, 'index.html', object)