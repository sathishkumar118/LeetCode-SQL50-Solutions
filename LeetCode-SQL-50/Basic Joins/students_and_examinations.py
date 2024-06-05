import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    return students.merge(
        subjects, how = 'cross'
        ).set_index(
            ['student_id','subject_name','student_name']
            ).sort_index().join(
                examinations.value_counts()
                ).fillna(0).reset_index().rename(
                    columns = {'count':'attended_exams'}
                    )[['student_id','student_name','subject_name','attended_exams']]