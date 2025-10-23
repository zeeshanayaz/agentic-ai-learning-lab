from fastapi import FastAPI
from schema.item import Item

# Create instance for FastAPI
app = FastAPI()

# Health check API endpoint
@app.get('/')
def health_check():
    return {
        "success": True,
        "message": "API is working properly"
    }


@app.get('/v1/hello')
def hello():
    return {
        "Success": True,
        "Message": "Hello, World!"
    }


@app.get('/v1/hello/{name}')
def hello(name: str):
    return {
        "Success": True,
        "Message": f"Hello, {name}!"
    }



items = [
    Item(id=1, name='Mobile'),
    Item(id=2, name='Laptop'),
    Item(id=3, name='Headphone'),
];


# Get all items API endpoint
@app.get('/v1/items')
def get_items():
    return {
        "success": True,
        "message": "Items fetched successfully",
        "items": items
    }


# Get item at {item_id}
@app.get('/v1/items/{item_id}')
def get_item(item_id: int):
    return {
        "success": True,
        "message": "Item fetched successfully",
        "item": items[item_id]
    }


# Add item
@app.post("/v1/item")
def add_item(item_name: str):
    item = Item(id=len(items)+1, name=item_name)
    
    items.append(item)
    return {
        "success": True,
        "message": "Item fetched successfully",
        "item": item
    }


# Update item
@app.put('/v1/items/{item_id}')
def update_item(item_id: int, item_name: str):
    items[item_id-1] = Item(id=item_id, name=item_name)

    return {
        "success": True,
        "message": "Item Updated successfully",
        "item": items[item_id-1]
    }


# Delete item
@app.delete('/v1/items/{item_id}')
def delete_item(item_id: int):
    item = items.pop(item_id-1)

    return {
        "success": True,
        "message": "Item Updated successfully",
        "item": item
    }