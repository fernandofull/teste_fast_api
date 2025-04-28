from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Dict
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Simulando uma base de dados
items_db = {
    1: {"nome": "Notebook", "preço": 3500},
    2: {"nome": "Mouse", "preço": 120},
    3: {"nome": "Teclado", "preço": 200}
}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        "items.html",
        {"request": request, "items": items_db}
    )

@app.get("/items/{item_id}")
def read_item(item_id: int) -> Dict:
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return items_db[item_id]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
