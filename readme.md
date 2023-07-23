# Amazon Review Helper

This is a Chrome extension that allows the user use OpenAI's GPT API's in order to summarize the reviews of a specific product, this is meant to work with the adjacent [FE project](https://github.com/RogerioSoares96/amazon_review_helper_fe). The idea of a chrome extension derived from the fact that Amazon does not allow a website scrapper to get a product's reviews data, based on their Terms of Service.

### Current Capabilities:

* Identify if the user is in an amazon website and only allow the user the activate the review helper, if the user is in an amazon website

* Display concise and legible pros and cons of a specific product given its reviews

* Only gets the compiled reviews from the product reviews page, not from the original product page itself

### WIP:

* Allow the user to get the compiled reviews straight from the product page

* Use global env variables to load the BE project endpoint


## Installation Steps

1. Clone/Download this repo
2. Create a Python virtual env to be used in this repo 
3. Run command `pip install -r requirements` from the repo
4. Run the FastAPI Server using the command `uvicorn main:app --reload   `