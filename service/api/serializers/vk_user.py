from marshmallow import Schema, fields


class VKUserSchema(Schema):
    id = fields.Int(allow_none=True)
    first_name = fields.String(allow_none=True)
    last_name = fields.String(allow_none=True)
    is_closed = fields.Boolean(allow_none=True)
    can_access_closed = fields.Boolean(allow_none=True)


class VKUsersSchema(Schema):
    response = fields.List(fields.Nested(VKUserSchema), required=True)
