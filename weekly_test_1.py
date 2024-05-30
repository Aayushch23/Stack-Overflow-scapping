# -*- coding: utf-8 -*-
"""weekly_test_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gJUCXjguMPMI1goGanEtZrsqC-o_moSs
"""

import requests
from bs4 import BeautifulSoup

def scrape_stackoverflow(url, question_title):
    try:
        # Fetching HTML content of the webpage
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Finding the question with the specified title
        question = soup.find('a', {'class': 'question-hyperlink', 'title': question_title})

        if question:
            print("Question:")
            print(question.text.strip())

            # Extracting answers for the question
            answers = question.find_next('div', {'class': 'answercell'}).find_all('div', {'class': 'post-text'})
            print("\nAnswers:")
            for index, answer in enumerate(answers, start=1):
                print(f"Answer {index}:")
                print(answer.text.strip())
        else:
            print("Question not found.")

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
    except Exception as ex:
        print("Error:", ex)

if __name__ == "__main__":
    url = "https://stackoverflow.com/questions/415511/how-do-i-get-the-current-time-in-python"
    question_title = "How do I get the current time in Python?"
    scrape_stackoverflow(url, question_title)