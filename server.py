from flask import Flask
import json
from mock_data import catalog


app = Flask("server")

@app.get("/")
def home():
    return "hello from flask"

@app.get("/test")
def test():
    return "this is another endpoint"

@app.get("/about")
def about():
    return "Jim Barnett"

################################################################
################################Catalog API#####################
################################################################

@app.get("/api/version")
def version():
    version = {
        "V":"V.1.1",
        "name":"Candy_Firewall",
        "yourzip":"your"
    }
    return json.dumps(version)

@app.get("/api/catalog")
def get_catalog():
    return json.dumps(catalog)

#get product by category
@app.get("/api/catalog/<category>")
def get_by_category(category):
    result = []
    for prod in catalog:
        if prod ["category"].lower() ==category.lower():
            result.append(prod)
    return json.dumps(result)

#get product by title search
@app.get("/api/catalog/search/<title>")
def search_by_title(title):
    #return all products whose title CONTAINS the title variable
    result = []
    for prod in catalog:
        if title.lower() in prod["title"].lower():
            result.append(prod)
            

    return json.dumps(result)

#return product with price less than 10 or 23

@app.get("/api/catalog/search/<price>")
def search_by_price(price):
    result = []
    for prod in catalog:
        if prod["price"] < float(price):
            result.append(prod)

    return json.dumps(result)

    #create a get endpoint that returns the number of products in the catalog
@app.get("/api/product/count")
def count_products():
    count = len(catalog)
    return json.dumps(count)
    #or json.dumps(len(catalog))

#return the cheapest product
@app.get("/api/catalog/cheapest")
def cheapest_product():
    answer = catalog[0]
    for prod in catalog:
        if prod["price"] < answer["price"]:
            answer = prod

    return json.dumps(answer)


@app.get('/test/numbers')
def get_numbers():

    result = []
    for n in range(1, 21):
        if n != 12 and n != 18:
            result.append(n)

    return json.dumps(result)

app.run(debug=True)