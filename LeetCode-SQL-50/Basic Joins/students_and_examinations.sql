select stu.student_id,max(student_name) as  student_name,sub.subject_name,count(e.subject_name) as attended_exams from Students as stu cross join Subjects as sub
left join Examinations as e on
stu.student_id = e.student_id and
sub.subject_name = e.subject_name
group by stu.student_id, sub.subject_name
order by stu.student_id, sub.subject_name