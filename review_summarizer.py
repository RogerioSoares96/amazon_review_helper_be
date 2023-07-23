from scrapped_reviews import scrapped_reviews
from gpt_api import reviews_summary

def review_summarizer(html):
    # soup = BeautifulSoup(html, 'html.parser')
    # all_reviews = soup.find(string='See more reviews')
    # reviews_site_url = all_reviews.parent.get('href')

    reviews = scrapped_reviews(html)
    return reviews_summary(reviews)