from student import Student


class Manager:
    def calc_avg_mark(self, ls):
        if not isinstance(ls, (list, tuple)):
            return 0

        avg = 0
        count = 0

        for student in ls:
            if isinstance(student, Student):
                avg += student.mark
                count += 1

        return avg / count