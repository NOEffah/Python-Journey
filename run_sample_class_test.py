from sample_class_test import AnonymousSurvey

# Define a question and make a survey
question = "What language did you learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question and store the response to the question
my_survey.show_question()
print("Enter 'q' to quit.")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results.
print("\n Thank you to everyone who participated in the survey! ")
my_survey.show_results()