from marshmallow import Schema, fields


class ItemSchema(Schema):
    name = fields.Str(required=True)
    price = fields.Int(required=True)
    

class ItemGetSchema(Schema):
    id = fields.Str(dump_only=True)
    item = fields.Nested(ItemSchema)


class SuccessMessageSchema(Schema):
    message = fields.Str(dump_only=True)