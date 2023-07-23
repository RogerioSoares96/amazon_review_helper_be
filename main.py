from fastapi import FastAPI
from pydantic import BaseModel
from review_summarizer import review_summarizer

app = FastAPI()

class ProductReviews(BaseModel):
    html: str

@app.post('/reviewer')
def reviewer(product: ProductReviews):
    reviews = review_summarizer(product.html)
    return {'data': reviews}