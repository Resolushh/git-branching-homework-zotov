def build_report(student_name, group, subjects):
    lines = [
        "Отчёт студента",
        f"ФИО: {student_name}",
        f"Группа: {group}",
        "Дисциплины:",
    ]
    lines.extend(f"  - {subject}" for subject in subjects)
    return "\n".join(lines)


def print_report():
    from profile import GROUP, STUDENT_NAME
    from subjects import SUBJECTS

    print(build_report(STUDENT_NAME, GROUP, SUBJECTS))