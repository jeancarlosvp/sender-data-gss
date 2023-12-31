from fastapi import APIRouter, status
from app.datapayments.schemas import DataPayments
from app.config import worksheet, SEND_GS
from datetime import datetime

router = APIRouter(prefix="/datapayments", tags=["datapayments"])

@router.post("/", status_code=status.HTTP_201_CREATED)
async def datapayments(data_payment: DataPayments):
    try:
        if SEND_GS == "True":
            print(SEND_GS)
            data_payment.date_payment = datetime.now().strftime("%d/%m/%Y")
            row_to_add = len(worksheet.get('B1:B')) + 1
            worksheet.batch_update([
                {
                    'range': f'B{row_to_add}:C{row_to_add}',
                    'values': [[data_payment.date_payment, data_payment.dni]]
                },
                {
                    'range': f'F{row_to_add}:G{row_to_add}',
                    'values': [[data_payment.total, data_payment.bank]]
                },
                {
                    'range': f'P{row_to_add}:R{row_to_add}',
                    'values': [[data_payment.mode_payment, data_payment.operation_code, data_payment.card_number]]
                }
            ], value_input_option='USER_ENTERED')
            return {"message": "Datos completados correctamente"}
        return {"message": "Flag SENDGS desactivado"}
    except Exception as e:
        return {"message": "Error al recibir los datos"}