from datetime import datetime
import dataclasses
import json


@dataclasses.dataclass # <<-- add this decorator 
class Foo():
    """An example dataclass."""

    bar: str = "hello"
    baz: str = "world"
    modified: datetime = Column(DateTime(timezone=True), default=datetime.utcnow)


class CustomJSONEncoder(json.JSONEncoder): # <<-- Add this custom encoder 
    """Custom JSON encoder for the DB class."""

    def default(self, o):
        if dataclasses.is_dataclass(o): # this serializes anything dataclass can handle  
            return dataclasses.asdict(o)
        if isinstance(o, datetime): # this adds support for datetime
            return o.isoformat()
        return super().default(o)
