from atshop import Client

client = Client()
client.login('token')

product = client.request(
    method='admin.product.add',

    shop_id='4AueTN7mx6xRurrfu',
    product={
        'name': 'Clap is cool <3',
        'description': '',
        'purchaseNotes': '',
        'value': 100,
        'icon': '',
        'minQuantity': 1,
        'maxQuantity': 0,
        'image_url': '',
        'style': 'box',
        'requireShipping': 'no',
        'paymentMethods': [],
        'maxDisplayedStock': 0,
        'preventDuplicates': True,
        'priority': 0,
        'category': '',
        'displayDescription': True,
        'useOrderIdAsItemName': False,
        'hidden': False,
        'notForSale': False
    }
)

print(product['result'])
