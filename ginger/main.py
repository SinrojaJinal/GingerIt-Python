from fastapi import FastAPI
from gingerit.gingerit import GingerIt
import uvicorn

app = FastAPI()

@app.get('/get_text')
async def get_text(text: str):
    output = GingerIt().parse(text)
    return { 'Result' : output['result']}

if __name__=="__main__":
    uvicorn.run(app, host='0.0.0.0', port=8001)