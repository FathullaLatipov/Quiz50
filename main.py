from fastapi import FastAPI

# uvicorn main:app --reload
app = FastAPI()


@app.get('/users')
async def all_users():
    return {'name': 'David', 'name2': 'John'}


@app.post('/products')
async def all_products(title: str, price: int):
    return {f'Your product name {title} and price {price}'}
