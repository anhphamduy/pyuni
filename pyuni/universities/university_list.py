from .university_detail import UniversityDetail




class UniversityOfMelbourne(UniversityDetail):
    name = "The University of Melbourne"
    login_url = 'https://mytimetable.students.unimelb.edu.au/even/student'


class AustralianNationalUniversity(UniversityDetail):
    name = "The Australian National University"
    login_url = ""
