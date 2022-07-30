<div align="center">
    <img src="https://i.imgur.com/1FOB2JF.png"/>
    <p>
      <a href="https://github.com/iclapcheeks/Atshop/pulse">
        <img alt="Last commit" src="https://img.shields.io/github/last-commit/iclapcheeks/Stelix"/>
      </a>
      <a href="https://github.com/iclapcheeks/Atshop/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/iclapcheeks/Atshop?style=flat-square&logo=GNU&label=License" alt="License">
      </a>
    </p>
</div>

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Atshop.

```bash
pip install atshop
```

## Usage
```python
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
```

## Documentation

Everything you need is listed in the [Atshop Documentation](https://docs.atshop.io/).
