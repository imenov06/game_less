from pydantic import BaseModel, ConfigDict


class STopic(BaseModel):
    id: int
    title: str
    text: str | None
    image_url: str | None
    time_learn: int
    cost: int
    course_id: int


class SCourseShort(BaseModel):
    id: int
    title: str
    is_active: bool
    is_life: bool


class SFullCourse(BaseModel):
    id: int
    title: str
    is_active: bool
    is_life: bool
    topics: list[STopic]
