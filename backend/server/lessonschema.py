from app import marshmallow

# Definition of the output format with marshmallow
# marshmallow is a serialization/deserialization library
# The object provides access to the Schema class, all fields in marshmallow.fields, 
# as well as the Flask-specific fields in flask_marshmallow.fields.
# This gives the access to ma.ModelSchema and ma.TableSchema, which generate marshmallow 
# Schema classes based on the passed in model or table.

class LessonSchema(marshmallow.Schema):
    class Meta:
        fields = ('id','tutorial_id','title','description', 'link')