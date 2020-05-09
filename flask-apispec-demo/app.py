
from flask import Flask
from webargs import fields
from apispec import APISpec
from marshmallow import Schema
from flask_apispec import use_kwargs, marshal_with
from flask_apispec import FlaskApiSpec
from flask_apispec.annotations import doc
from apispec.ext.marshmallow import MarshmallowPlugin


app = Flask(__name__)
app.config.update({
            'APISPEC_SPEC': APISpec(
                title='pets',
                version='v1',
                openapi_version='2.0',
                plugins=[MarshmallowPlugin()],
            ),
            'APISPEC_SWAGGER_URL': '/swagger/',
        })
docs = FlaskApiSpec(app)


class PetSchema(Schema):
    class Meta:
        fields = ('name', 'category', 'size')



class Pet:
    asd = 1
    name = 2
    category = 3
    size = 4

@app.route('/asd', methods=["GET"])
@use_kwargs({'species': fields.Str()})  # 控制request
@marshal_with(PetSchema, code=200)  # 控制response
@doc(tags=['pet'], description='a pet store asdasd')  # swagger文档注释
def list_pets(**kwargs):
    asd = Pet()
    return asd


docs.register(list_pets)  # 注册文档

