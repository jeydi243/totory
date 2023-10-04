from dtos.course_dto import CourseDTO
from schemas.course import Course


class CourseService:
    def add_course(self, course: CourseDTO):
        co = Course(**course.dict()).save()
        print(f"add one course {co}")
        return co

    def getCourses(self):
        try:
            val = Course.objects.values_list()
            print(val[0].to_json())
        except BaseException as e:
            print(e)

    def getById(self, id: str):
        return Course.objects.get(id=id)
