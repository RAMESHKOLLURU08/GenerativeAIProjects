# Create a question answering bot to interact with using natural language.
# Link: https://learn.microsoft.com/en-us/training/modules/create-question-answer-solution-ai-language/1-introduction
##############################################################
'''Pre-requisites:
1) Create a Language Resource
Go to Portal.Azure.com
Create a Language Resource.
2) Create a question answering project
Go to https://language.cognitive.azure.com/ 
Create Azure Search Service if not exists.
Create a Project and select for 'Custom question answering'
3) Go to Manage Resource and add knowledge base
Add source url: https://docs.microsoft.com/en-us/learn/support/faq
Add another source: Chitchat
4) Edit Knowledge base
Add a new question
Add an alternate question
Add follow up prompts
5) Train and Test Knowledge base
6) Deploy the knowledge base
7) Prepare app in visual studio code.
Get Keys and End points from Azure Language Service and update envirnonment file for the below:
'AI_SERVICE_ENDPOINT'
and 'AI_SERVICE_KEY'
'''


from dotenv import load_dotenv
import os

# import namespaces
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient


def main():
    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')
        ai_project_name = os.getenv('QA_PROJECT_NAME')
        ai_deployment_name = os.getenv('QA_DEPLOYMENT_NAME')

        # Create client using endpoint and key
        credential = AzureKeyCredential(ai_key)
        ai_client = QuestionAnsweringClient(endpoint=ai_endpoint, credential=credential)


        # Submit a question and display the answer
        user_question = ''
        while user_question.lower() != 'quit':
            user_question = input('\nQuestion:\n')
            response = ai_client.get_answers(question=user_question,
                                            project_name=ai_project_name,
                                            deployment_name=ai_deployment_name)
            for candidate in response.answers:
                print(candidate.answer)
                print("Confidence: {}".format(candidate.confidence))
                print("Source: {}".format(candidate.source))



    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()



