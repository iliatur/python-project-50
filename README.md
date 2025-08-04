### Hexlet tests and linter status:
[![Actions Status](https://github.com/iliatur/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/iliatur/python-project-50/actions)[![Python CI](https://github.com/iliatur/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/iliatur/python-project-50/actions/workflows/pyci.yml)[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=iliatur_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=iliatur_python-project-50)[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=iliatur_python-project-50&metric=bugs)](https://sonarcloud.io/summary/new_code?id=iliatur_python-project-50)[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=iliatur_python-project-50&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=iliatur_python-project-50)[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=iliatur_python-project-50&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=iliatur_python-project-50)[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=iliatur_python-project-50&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=iliatur_python-project-50)[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=iliatur_python-project-50&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=iliatur_python-project-50)[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=iliatur_python-project-50&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=iliatur_python-project-50)[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=iliatur_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=iliatur_python-project-50)[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=iliatur_python-project-50&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=iliatur_python-project-50)

# 🧠 gendiff (генератор различий)
Инструмент командной строки для сравнения JSON и YAML файлов.
Позволяет выявить различия, включая вложенные структуры.

## 📚 Оглавление

- [🚀 Установка и запуск](#-установка и запуск)
- [🔍 Примеры использования](#-примеры-использования)
- [💡 Поддержка форматов](#-поддержка-форматов)
- [🧪 Тестирование](#-тестирование)


## ⚙️ Установка
1. Склонируйте репозиторий:
```bash
git clone git@github.com:iliatur/python-project-50.git
cd python-project-50
```
2. Установите зависимости с помощью UV:
```bash
uv install
```
3. Установите проект:
```bash
make install
```

## 🔍 Примеры использования
1. Запуск сравнения с форматом stylish (по умолчанию)
[![asciicast](https://asciinema.org/a/0JBvTT2KOm8MMs0P1EpADeuVZ.svg)](https://asciinema.org/a/0JBvTT2KOm8MMs0P1EpADeuVZ)

2. Запуск сравнения с форматом plain
[![asciicast](https://asciinema.org/a/EngHvisHtPUPQEw6KPN7jDuAe.svg)](https://asciinema.org/a/EngHvisHtPUPQEw6KPN7jDuAe)

3. Запуск сравнения с форматом json
[![asciicast](https://asciinema.org/a/b9KAa5CnK3eb0zbhGYegiQzG4.svg)](https://asciinema.org/a/b9KAa5CnK3eb0zbhGYegiQzG4)


## 💡 Поддержка форматов
| Формат входа | Формат вывода     | Поддержка |
|--------------|-------------------|-----------|
| `.json`      | `stylish` (default) |   ✅     |
| `.yaml`      | `plain`            |    ✅     |
| комбинированно | `json`            |   ✅     |

---

## 🧪 Тестирование
```bash
make test
make lint
```
