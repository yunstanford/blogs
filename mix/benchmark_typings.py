import time

N = 10000
print("Iterations: {N}".format(N=N))

# typesystem
import typesystem

class Artist(typesystem.Schema):
    name = typesystem.String(max_length=100)

class Album(typesystem.Schema):
    title = typesystem.String(max_length=100)
    release_date = typesystem.Date()
    artist = typesystem.Reference(Artist)

def validate_album():
    album = Album.validate({
        "title": "Double Negative",
        "release_date": "2018-09-14",
        "artist": {"name": "Low"}
    })

def bm_typesystem():
    print("=== benchmark typesystem ===")
    start = time.time()
    for _ in range(N):
        validate_album()
    end = time.time()
    print(end - start)


bm_typesystem()

# attrs/cattrs
import attr
import cattr
from cattr import Converter
from datetime import datetime
from schematics.types import DateTimeType

datetime_type = DateTimeType()

def _structure_datetime(data, cls):
    if not data:
        raise ValueError("datetime is empty")
    return datetime_type.to_native(data)

def _unstructure_datetime(data):
    return data.isoformat()

converter = Converter()
converter.register_structure_hook(datetime, _structure_datetime)
converter.register_unstructure_hook(datetime, _unstructure_datetime)

def validate_len(instance, attribute, value):
    if len(value) > 100:
        raise ValueError("val should <= 100")

@attr.s
class Artist2:
    name = attr.ib(type=str, validator=validate_len)

@attr.s
class Album2:
    title = attr.ib(type=str, validator=validate_len)
    release_date = attr.ib(type=datetime)
    artist = attr.ib(type=Artist2)


def validate_album_2():
    utcnow = datetime.utcnow()
    album = converter.structure({
            "title": "Double Negative",
            "release_date": utcnow,
            "artist": {"name": "Low"},
        }, Album2)

def bm_attrs():
    print("=== benchmark attrs/cattrs ===")
    start = time.time()
    for _ in range(N):
        validate_album_2()
    end = time.time()
    print(end - start)

bm_attrs()


# pydantic
from datetime import datetime
from pydantic import BaseModel, validator

class Artist3(BaseModel):
    name: str

    @validator('name')
    def name_must_less_than_100(cls, v):
        if len(v) > 100:
            raise ValueError("len(name) should <= 100")
        return v

class Album3(BaseModel):
    title: str
    release_date: datetime
    artist: Artist3

    @validator('title')
    def title_must_less_than_100(cls, v):
        if len(v) > 100:
            raise ValueError("len(title) should <= 100")
        return v

def validate_album_3():
    utcnow = datetime.utcnow()
    album = Album3(**{
            "title": "Double Negative",
            "release_date": utcnow,
            "artist": {"name": "Low"},
        })

def bm_pydantic():
    print("=== benchmark pydantic ===")
    start = time.time()
    for _ in range(N):
        validate_album_3()
    end = time.time()
    print(end - start)

bm_pydantic()


# schematics
from schematics.models import Model
from schematics.types import StringType, IntType, BooleanType, FloatType, BaseType, DateTimeType
from schematics.types.compound import ModelType, ListType, DictType

class ArtistSchematics(Model):
    name = StringType(required=True)

class AlbumSchematics(Model):
    title = StringType(required=True)
    release_date = DateTimeType(required=True)
    artist = ModelType(ArtistSchematics)

def validate_album_schematics():
    utcnow = datetime.utcnow()
    album = AlbumSchematics({
            "title": "Double Negative",
            "release_date": utcnow,
            "artist": {"name": "Low"},
        })
    album.validate()

def bm_schematics():
    print("=== benchmark schematics ===")
    start = time.time()
    for _ in range(N):
        validate_album_schematics()
    end = time.time()
    print(end - start)

bm_schematics()
