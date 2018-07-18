from datetime import datetime


class Response(object):
    def __init__(self,
                 status_code,
                 status_message,
                 transaction_id,
                 order_id,
                 payment_type,
                 transaction_time,
                 transaction_status,
                 fraud_status,
                 gross_amount,

                 masked_card=None,
                 permata_va_number=None,
                 signature_key=None,
                 token_id=None,
                 saved_token_id=None,
                 saved_token_id_expired_at=None,
                 secure_token=None,
                 bank=None,
                 biller_code=None,
                 bill_key=None,
                 xl_tunai_order_id=None,
                 bii_va_number=None,
                 redirect_url=None,
                 eci=None,
                 validation_messages=None,
                 page=None,
                 total_page=None,
                 total_record=None,
                 payment_amounts=None,
                 va_numbers=None,
                 currency=None):

        '''
        Bellow are the fields that always present in any kind of response
        '''
        self.status_code = int(status_code)
        self.status_message = status_message
        self.transaction_id = transaction_id
        self.order_id = order_id
        self.payment_type = payment_type
        self.transaction_time = datetime.strptime(transaction_time, "%Y-%m-%d %H:%M:%S")
        self.transaction_status = transaction_status
        self.fraud_status = fraud_status
        self.gross_amount = int(gross_amount.split(".")[0])

        '''
        Additional fields exist on specific payment type
        '''
        self.masked_card = masked_card
        self.permata_va_number = permata_va_number
        self.sign_key = signature_key
        self.card_token = token_id
        self.saved_card_token = saved_token_id
        self.saved_token_exp_at = saved_token_id_expired_at
        self.secure_token = secure_token
        self.bank = bank
        self.biller_code = biller_code
        self.bill_key = bill_key
        self.xl_tunai_order_id = xl_tunai_order_id
        self.bii_va_number = bii_va_number
        self.re_url = redirect_url
        self.eci = eci
        self.val_messages = validation_messages
        self.page = page
        self.total_page = total_page
        self.total_record = total_record
        self.payment_amounts = payment_amounts
        self.va_numbers = va_numbers
        self.currency = currency