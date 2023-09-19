"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    """Determine grade from user and random input."""
    score = float(input("Enter score: "))
    grade_score(score)
    final_score = grade_score(score)
    print(final_score)

    score = random.randint(1, 100)
    grade_score(score)
    print(f"Random Score: {score}")
    final_score = grade_score(score)
    print(final_score)


def grade_score(score):
    """Determine grade from score."""
    if score > 100:
        return "Invalid Score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    elif score < 50:
        return "Bad"
    else:
        return "Invalid score"


main()
