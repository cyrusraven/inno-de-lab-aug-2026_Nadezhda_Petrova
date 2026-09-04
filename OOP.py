class Trainee:
    def __init__(self, name: str, surname: str, score: int = 0, passing_grade: int = 10) -> None:
        self.name = name
        self.surname = surname
        self.__score = score
        self.passing_grade = passing_grade

    @property
    def score(self) -> int:
        return self.__score

    @score.setter
    def score(self, value) -> None:
        if not isinstance(value, int):
            raise ValueError(f"Expected value of type int, got {type(value)}")
        if value < 0:
            raise ValueError("The score shouldn't be less than 0!")
        self.__score = value

    def do_homework(self) -> None:
        """Increases score by 1"""
        self.__score += 1

    def miss_homework(self) -> None:
        """Decreases score by 1"""
        self.__score -= 1

    def visit_lecture(self) -> None:
        """Increases score by 1"""
        self.__score += 1

    def miss_lecture(self) -> None:
        """Decreases score by 1"""
        self.__score -= 1

    def is_passing(self) -> bool:
        return self.score >= self.passing_grade

class HardworkingTrainee(Trainee):
    def do_homework(self) -> None:
        """Increases score by 2"""
        self.score += 2

class AuditTrainee(Trainee):
    def is_passing(self) -> bool:
        """Always returns True"""
        return True

class Cohort:
    def __init__(self, title: str, trainees: list[Trainee] = None) -> None:
        self.title = title
        self.trainees = trainees if trainees is not None else []

    def add_trainee(self, trainee: Trainee) -> None:
        self.trainees.append(trainee)

    def conduct_lecture(self) -> None:
        for trainee in self.trainees:
            trainee.visit_lecture()

    def get_passing_students(self) -> list[Trainee]:
        return [trainee for trainee in self.trainees if trainee.is_passing()]

if __name__ == "__main__":
    trainee = Trainee("Иван", "Иванов", 9, 10)

    print("=== ПРОВЕРКА УСПЕВАЕМОСТИ СТАЖЕРА ===")

    trainee.do_homework()
    print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")

    trainee.miss_lecture()
    print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")

    try:
        trainee.score = -5
    except ValueError as e:
        print(f"Ошибка: {e}")

print()

if __name__ == "__main__":
    std_trainee = Trainee("Алексей", "Смирнов" , 8, 10)
    hard_trainee = HardworkingTrainee("Елена", "Петрова", 8,10)
    audit_trainee = AuditTrainee("Дмитрий", "Сидоров", 0, 10)

    cohort = Cohort("Python Advanced")
    
    cohort.add_trainee(std_trainee)
    cohort.add_trainee(hard_trainee)
    cohort.add_trainee(audit_trainee)
    cohort.conduct_lecture()
    hard_trainee.do_homework()
    passing_students = cohort.get_passing_students()

    print(f"=== УСПЕВАЕМОСТЬ ГРУППЫ '{cohort.title}'===")
    for student in cohort.trainees:
        print(f"{student.name} {student.surname} | Баллы: {student.score} | Проходит: {student.is_passing()}")

    print("\nУспешно зачислены на следующий модуль:")
    for student in passing_students:
        print(f"- {student.name} {student.surname}")
