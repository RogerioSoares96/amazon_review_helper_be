import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ.get('API_KEY')

def reviews_summary(reviews_list):
    reviews_str = ", \n".join(reviews_list)
    summary = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role':'system', 
            'content':'You are a helpful assistant which summarizes the pros and cons of a products based of user reviews'},
            {'role':'user', 'content':f'Provide a thorough summary of the product and its pros and cons through an extensive and descriptive text format based on the following user reviews: {reviews_str}'}
                ]
    )
    return summary.choices[0].message.content