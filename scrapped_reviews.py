from bs4 import BeautifulSoup

def scrapped_reviews(amazon_reviews_site):
    soup = BeautifulSoup(amazon_reviews_site, 'html.parser')
    reviews = soup.find(id='cm_cr-review_list')

    bulk_reviews = reviews.contents
    granular_reviews = list()

    for review in bulk_reviews:
        if 'data-hook' in review.attrs and review.attrs['data-hook'] == 'review':
            for descendant in list(review.descendants):
                if descendant.name == 'span' and 'data-hook' in descendant.attrs and descendant.attrs['data-hook'] == 'review-body':
                    granular_review = list(descendant.contents)[1]
                    if 0 < len(granular_review.find_all('br')):
                        for tag in review.find_all('br'):
                            tag.unwrap()            
                    granular_reviews.append(granular_review.text)
    return granular_reviews