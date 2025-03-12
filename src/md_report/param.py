from pydantic import BaseModel
# import logfire

# logfire.configure()
# logfire.instrument_pydantic()

class Parameter(BaseModel):
    name: str
    required: bool
    default: str | None
    alias: str
