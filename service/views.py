# views.py
from django.http import HttpResponseNotFound
from django.shortcuts import render

from django.shortcuts import render

def my_view(request):
    # Assuming you have a list named 'backend_list' containing your data
    backend_list = [
        {'id': 1, 'title': 'Machine learning approaches for Cyber Security',
         'description': 'As we use internet more, the data produced by us is enormous. But are these data being secure? The goal of applying machine learning or intelligence is to better risk modelling and prediction and for an informed decision support. Students will be working with either supervised or unsupervised machine learning approaches to solve the problem/s in the broader areas of Cyber Security.',
         'supervisor': 'Bharanidharan Shanmugam'},
        {'id': 2, 'title': 'Informetrics applications in multidisciplinary domain',
         'description': 'Informetrics studies are concerned with the quantitative aspects of information. The applications of advanced machine learning, information retrieval, network science and bibliometric techniques on various information artefact have contributed fresh insights into the evolutionary nature of research fields. This project aims at discovering informetric properties of multidisciplinary research literature using various machine learning, network analysis, data visualisation and data wrangling tools.',
         'supervisor': 'Yakub Sebastian'},
        {'id': 3, 'title': 'Development of a Virtual Reality System to Test Binaural Hearing',
         'description': 'A virtual reality system could be used to objectively test the binaural hearing ability of humans (the ability to hear stereo and locate the direction and distance of sound). This project aims to design, implement and evaluate a VR system using standard off the shelf components (VR goggle and headphones) and standard programming techniques.',
         'supervisor': 'Sami Azam'},
        {'id': 4, 'title': 'Current trends on cryptomining and its potential impact on cryptocurrencies',
         'description': 'A virtual reality system could be used to objectively test the binaural hearing ability of humans (the ability to hear stereo and locate the direction and distance of sound). This project aims to design, implement and evaluate a VR system using standard off the shelf components (VR goggle and headphones) and standard programming techniques.',
         'supervisor': 'Sami Azam'},
        {'id': 5, 'title': 'Artificial Intelligence in Health Informatics',
         'description': 'The project aims to use multiple publicly available health datasets to formulate a different dataset that may have features from the original set along with new ones developed through feature engineering. The dataset will then be used to build predictive model based on both general and deep learning based algorithm. The findings will be analysed and compared to similar research works.',
         'supervisor': 'Asif Karim'},
        {'id': 6, 'title': 'Unsupervised Model Development from Autism Screening Data',
         'description': 'The proposed system will present a two-cluster solution from a given dataset which will group toddlers based on multiple common medical traits. In depth literature survey of similar studies, both supervised and unsupervised will be carried out before the cluster-based model is implemented. The solution will be validated using both External and Internal validation measures and statistical significance tests. ',
         'supervisor': 'Asif Karim'},
        {'id': 7, 'title': 'Applying Artificial Intelligence to solve real world problems',
         'description': 'Artificial Intelligence has been used in many applications to solve certain problems through out the academia and the industry – from electricity to writing text. AI has a multitude of applications and this project will pick up a problem and explore the applications of AI with minimal human intervention. Examples of applications include -building a bot, predicting the power usage, spam filtering and the list is endless.',
         'supervisor': 'Bharanidharan Shanmugam'},
    ]
    return render(request, 'ThesisManagement/projectList.html', {'backend_list': backend_list})

def project_details_view(request, project_id):
    # Assuming you have a list named 'backend_list' containing your data
    listt = [
        {'id': 1, 'title': 'Machine learning approaches for Cyber Security',
         'description': 'As we use internet more, the data produced by us is enormous. But are these data being secure? The goal of applying machine learning or intelligence is to better risk modelling and prediction and for an informed decision support. Students will be working with either supervised or unsupervised machine learning approaches to solve the problem/s in the broader areas of Cyber Security.',
         'supervisor': 'Bharanidharan Shanmugam'},
        {'id': 2, 'title': 'Informetrics applications in multidisciplinary domain',
         'description': 'Informetrics studies are concerned with the quantitative aspects of information. The applications of advanced machine learning, information retrieval, network science and bibliometric techniques on various information artefact have contributed fresh insights into the evolutionary nature of research fields. This project aims at discovering informetric properties of multidisciplinary research literature using various machine learning, network analysis, data visualisation and data wrangling tools.',
         'supervisor': 'Yakub Sebastian'},
        {'id': 3, 'title': 'Development of a Virtual Reality System to Test Binaural Hearing',
         'description': 'A virtual reality system could be used to objectively test the binaural hearing ability of humans (the ability to hear stereo and locate the direction and distance of sound). This project aims to design, implement and evaluate a VR system using standard off the shelf components (VR goggle and headphones) and standard programming techniques.',
         'supervisor': 'Sami Azam'},
        {'id': 4, 'title': 'Current trends on cryptomining and its potential impact on cryptocurrencies',
         'description': 'A virtual reality system could be used to objectively test the binaural hearing ability of humans (the ability to hear stereo and locate the direction and distance of sound). This project aims to design, implement and evaluate a VR system using standard off the shelf components (VR goggle and headphones) and standard programming techniques.',
         'supervisor': 'Sami Azam'},
        {'id': 5, 'title': 'Artificial Intelligence in Health Informatics',
         'description': 'The project aims to use multiple publicly available health datasets to formulate a different dataset that may have features from the original set along with new ones developed through feature engineering. The dataset will then be used to build predictive model based on both general and deep learning based algorithm. The findings will be analysed and compared to similar research works.',
         'supervisor': 'Asif Karim'},
        {'id': 6, 'title': 'Unsupervised Model Development from Autism Screening Data',
         'description': 'The proposed system will present a two-cluster solution from a given dataset which will group toddlers based on multiple common medical traits. In depth literature survey of similar studies, both supervised and unsupervised will be carried out before the cluster-based model is implemented. The solution will be validated using both External and Internal validation measures and statistical significance tests. ',
         'supervisor': 'Asif Karim'},
        {'id': 7, 'title': 'Applying Artificial Intelligence to solve real world problems',
         'description': 'Artificial Intelligence has been used in many applications to solve certain problems through out the academia and the industry – from electricity to writing text. AI has a multitude of applications and this project will pick up a problem and explore the applications of AI with minimal human intervention. Examples of applications include -building a bot, predicting the power usage, spam filtering and the list is endless.',
         'supervisor': 'Bharanidharan Shanmugam'},
    ]

    # Filter the list to find the project with the matching ID
    filtered_project = next((project for project in listt if project['id'] == project_id), None)

    # Check if a project with the given ID was found
    if filtered_project:
        return render(request, 'ThesisManagement/projectDetails.html', {'project': filtered_project})
    else:
        # Handle the case when no project with the given ID is found
        return HttpResponseNotFound("Project not found")

