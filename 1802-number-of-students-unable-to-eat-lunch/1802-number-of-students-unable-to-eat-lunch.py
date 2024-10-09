class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        rotation=0
        while students and sandwiches:
            if students[0] != sandwiches[0]:
                students.append(students.pop(0))
                rotation+=1
            else:
                students.pop(0)
                sandwiches.pop(0)
                rotation=0
            if rotation == len(students):
                break

        return len(students)