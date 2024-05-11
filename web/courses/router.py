from fastapi import APIRouter

from courses.repo import CourseRepo, TopicRepo
from courses.schemas import SCourseShort, SFullCourse, STopic

router = APIRouter(
    prefix="/courses",
    tags=["Главы. Темы"]
)


@router.get("/full")
async def get_all_full_courses() -> list[SFullCourse]:
    full_courses: list[SFullCourse] = await CourseRepo.find_all_courses()
    return full_courses


@router.get("/full/{course_id}")
async def get_full_course(course_id: int) -> SFullCourse | None:
    full_course: SFullCourse | None = await CourseRepo.find_by_id_course(course_id)
    return full_course


@router.get("/short")
async def get_all_short_courses() -> list[SCourseShort]:
    short_courses: list[SCourseShort] = await CourseRepo.find_all_courses()
    return short_courses


@router.get("/short/{course_id}")
async def get_short_course(course_id: int) -> SCourseShort | None:
    short_course: SCourseShort | None = await CourseRepo.find_by_id_course(course_id)

    return short_course


@router.get("/topic/{topic_id}")
async def get_topic_by_id(topic_id: int) -> STopic| None:
    topic: STopic|None = await TopicRepo.find_by_id(topic_id)
    return topic
