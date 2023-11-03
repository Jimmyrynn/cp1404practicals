"""
Estimate: 20 minutes
Actual:   18 minutes
"""
from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
languages = [python, ruby, visual_basic]
# print(f"{python}\n{ruby}\n{visual_basic}")

print("The dynamically typed languages are:")
for line in languages:
    if line.is_dynamic():
        print(line.name)
    else:
        print(f"Non Dynamic: {line.name}")
