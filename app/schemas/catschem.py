from pydantic import BaseModel, Field

# from slugify import slugify


class CatSchema(BaseModel):
    name: str = Field(..., max_length=100)
    slug: str = Field(..., max_length=100)

    # @model_validator(mode="after")
    # def generate_slug(self):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     return self


class CatResponse(BaseModel):
    name: str = Field(..., max_length=100)
    id: int

    class Config:
        from_attributes = True
