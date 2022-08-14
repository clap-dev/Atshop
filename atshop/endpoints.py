'''List of all endpoints we knows about.'''

ROOT = 'wss://atshop.io/websocket'
METHODS = {
    'order.exists': [
        'order_id'
    ],
    'order.fulfill.alternativePayment': [
        'order_id',
        'amount_paid',
        'payment_method'
    ],
    'admin.orders.replace': [
        'order_id',
        'shop_id',
        'quantitiy',
        'note'
    ],

    # Orders

    'admin.product.add': [
        'shop_id',
        'product'
    ],
    'admin.product.edit': [
        'product'
    ],
    'admin.product.remove': [
        'product_id'
    ],

    # Product

    'shop.product.groups.save': [
        'product_group'
    ],
    'shop.product.groups.remove': [
        'product_group_id'
    ],

    # Product Group

    'admin.product.stock.get.all': [
        'product_id'
    ],
    'admin.product.stock.add': [
        'product_id',
        'stock'
    ],
    'admin.product.stock.delete': [
        'stock_to_remove'
    ],
    'admin.product.stock.update': [
        'product_id',
        'to_add',
        'to_remove'
    ],

    # Stock

    'coupon.create': [
        'coupon'
    ],
    'coupon.edit': [
        'coupon'
    ],
    'coupon.remove': [
        'coupon_id'
    ]

    # Coupon Codes
}
