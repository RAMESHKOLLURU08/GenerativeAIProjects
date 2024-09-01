'''
Project Name: Custom text classification
Source: https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/04-text-classification.html
Note: If you hit the issue 403 error, while accessing classification project which you have created, follow the below troubleshooting steps.
https://learn.microsoft.com/en-us/answers/questions/1881274/how-do-i-fix-a-403-this-request-is-not-authorized
##########
Environment File:
AI_SERVICE_ENDPOINT='https://rkclsinstance.cognitiveservices.azure.com/'
AI_SERVICE_KEY='931063595c804d3ca8ebb3a896a215ea'
PROJECT=ClassifyLab # Text classification project name
DEPLOYMENT=articles # deployment name
###########
In classify-text.py
#############
from dotenv import load_dotenv
import os

# import namespaces
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient


def main():
    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')
        project_name = os.getenv('PROJECT')
        deployment_name = os.getenv('DEPLOYMENT')

        # Create client using endpoint and key
        credential = AzureKeyCredential(ai_key)
        ai_client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)


        # Read each text file in the articles folder
        batchedDocuments = []
        articles_folder = 'articles'
        files = os.listdir(articles_folder)
        for file_name in files:
            # Read the file contents
            text = open(os.path.join(articles_folder, file_name), encoding='utf8').read()
            batchedDocuments.append(text)

        # Get Classifications
        operation = ai_client.begin_single_label_classify(
            batchedDocuments,
            project_name=project_name,
            deployment_name=deployment_name
        )

        document_results = operation.result()

        for doc, classification_result in zip(files, document_results):
            if classification_result.kind == "CustomDocumentClassification":
                classification = classification_result.classifications[0]
                print("{} was classified as '{}' with confidence score {}.".format(
                    doc, classification.category, classification.confidence_score)
                )
            elif classification_result.is_error is True:
                print("{} has an error with code '{}' and message '{}'".format(
                    doc, classification_result.error.code, classification_result.error.message)
                )



    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
'''
