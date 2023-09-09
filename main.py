import uvicorn
from fastapi import FastAPI
from peewee import DoesNotExist
from starlette.requests import Request
from starlette.responses import Response

import image_lib
from db_session import ECG, db

app = FastAPI()


@app.get('/')
async def test():
    return {'message': 'AMOGUS'}


@app.post('/new-ecg')
async def new_ecg(request: Request):
    data = await request.json()

    try:
        ecg = ECG.get(
            ECG.patient_name == data['patient_name'],
            ECG.graph_x == data['graph_x'],
            ECG.graph_y == data['graph_y'],
            ECG.pulse == data['pulse']
        )
    except DoesNotExist:
        ecg = ECG.create(
            patient_name=data['patient_name'],
            graph_x=data['graph_x'],
            graph_y=data['graph_y'],
            pulse=data['pulse']
        )
        ecg.save()

    img = await image_lib.get_ecg_image(
        data['graph_x'], data['graph_y']
    )

    return Response(
        status_code=200,
        content=img,
        media_type='image/png'
    )


@app.get('/get-ecg/{patient_id}')
async def get_ecg(patient_id: int):
    ecg = ECG.get(ECG.id == patient_id)
    data = {
        'patient_name': ecg.patient_name,
        'pulse': ecg.pulse,
        'image': await image_lib.get_ecg_image(
            ecg.graph_x,
            ecg.graph_y
        )
    }

    return Response(
        content=data,
        status_code=200
    )


with db:
    db.create_tables([ECG])

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
