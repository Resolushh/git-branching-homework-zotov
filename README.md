# Git Branching Homework

## Описание проекта

**Student Branching App** — учебный Python-проект для отработки ветвления в Git. Приложение выводит профиль студента, список дисциплин и итоговый отчёт. Каждая функция разрабатывалась в отдельной ветке и попадала в `main` через merge или Pull Request.

**Автор:** Зотов Владислав Сергеевич, группа РПО 9/1

## Использованные ветки

| Ветка | Что делал | Как попала в main |
|---|---|---|
| `feature/profile` | модуль профиля студента | merge локально |
| `feature/subjects` | список дисциплин | merge локально |
| `feature/report` | итоговый отчёт | Pull Request |
| `experiment/broken-idea` | тестовая идея | удалена без merge |

## Pull Request

Ссылка на PR: https://github.com/Resolushh/git-branching-homework-zotov/pull/1

## Коммиты

1. `docs: добавить README проекта`
2. `feat: добавить базовый запуск приложения`
3. `feat(profile): добавить модуль профиля студента`
4. `feat(profile): подключить профиль в main.py`
5. `feat(subjects): добавить модуль дисциплин`
6. `feat(subjects): подключить дисциплины в main.py`
7. `feat(report): добавить модуль отчёта`
8. `feat(report): подключить отчёт в main.py`
9. `docs: оформить отчёт по веткам в README`

## Скриншоты

- `docs/screenshots/01-branches-before-merge.png` — граф веток до merge
- `docs/screenshots/02-merge-result.png` — результат merge
- `docs/screenshots/03-pull-request-merged.png` — созданный и закрытый Pull Request
- `docs/screenshots/04-final-github-main.png` — финальная ветка main на GitHub

## Вывод

Ветки позволяют разрабатывать функции изолированно, не затрагивая рабочую версию в `main`. Локальный merge удобен для небольших изменений, а Pull Request на GitHub даёт возможность проверить код перед слиянием. Экспериментальные ветки можно безопасно удалять, если идея не сработала.

## Запуск

```bash
python main.py
```
