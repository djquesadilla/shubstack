from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI()

class SlugModel(BaseModel):
    slug: str

@app.get("/{slug}")
async def redirect_to_substack(slug: str):
    if not slug:
        raise HTTPException(status_code=400, detail="Empty slug not allowed")
    substack_url = f"https://substack.com/{slug}"
    return RedirectResponse(url=substack_url)