"""
Estimated: 4hrs
Actual: 5hrs
"""
import datetime
from prac_07.project import Project


def main():
    """Program to Load, Save, Display, Filter, Add & Update projects. """
    # filename = "projects.txt"
    projects = []
    print_menu()
    user_input = input(">>> ").lower()
    while user_input != 'q':
        if user_input == 'l':
            filename = input("Enter Filename: ")
            projects = []
            read_from_file(filename, projects)

        elif user_input == 's':
            write_to_file(projects)

        elif user_input == 'd':
            completed_projects, incomplete_projects = determine_completion(projects)
            print_projects(completed_projects, incomplete_projects)

        elif user_input == 'f':  # Incomplete
            print(filter_by_date(projects))

        elif user_input == 'a':
            print("Let's add a new project")
            add_project(projects)

        elif user_input == 'u':
            for i, project in enumerate(projects, 0):
                print(f"{i} {project}")
            update_project(projects)
        else:
            print("Error")
        print_menu()
        user_input = input(">>> ").lower()


def filter_by_date(projects):
    """Return a list of filtered sorted dates"""
    filter_date = input("Filter date (dd/mm/yyyy): ")
    filter_date = datetime.datetime.strptime(filter_date, "%d/%m/%Y")
    return sorted([project for project in projects if
                   datetime.datetime.strptime(project.start_date, "%d/%m/%Y") > filter_date])


def determine_completion(projects):
    """Determine if project is completed."""
    completed_projects = []
    incomplete_projects = []
    for project in projects:
        if project.completion_percentage < 100:
            incomplete_projects.append(project)
        else:
            completed_projects.append(project)
    return completed_projects, incomplete_projects


def update_project(projects):
    """Update a project in a list."""
    project_choice = int(input("Project Choice: "))
    print(projects[project_choice])
    new_percentage = int(input("New Percentage:"))
    projects[project_choice].completion_percentage = new_percentage


def add_project(projects):
    """Add project to list."""
    name = input("Name: ")
    date_string = input("Start date (dd/mm/yy): ")
    start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = int(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def print_projects(completed_projects, incomplete_projects):
    """Print complete & incomplete projects."""
    print("Uncompleted projects: ")
    for project in incomplete_projects:
        print(project)
    print("Completed projects: ")
    for project in completed_projects:
        print(project)


def write_to_file(projects):
    """Write to an output file."""
    with open("test.txt", 'w', encoding='utf-8') as output_file:
        output_file.write(
            "Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
    for project in projects:
        output_file.write(
            f"{project.name}\t{project.start_date}\t{project.priority}"
            f"\t{project.cost_estimate}\t{project.completion_percentage}\n")
    output_file.close()


def read_from_file(filename, projects):
    """Read data from file."""
    with open(filename, 'r', encoding='utf-8') as in_file:
        in_file.readline()
    for line in in_file:
        parts = line.strip().split('\t')
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project)
    in_file.close()


def print_menu():
    """Print menu."""
    print("(L)oad projects\n(S)ave projects\n(D)isplay projects\n"
          "(F)ilter projects by date\n(A)dd new project\n(U)pdate"
          " project\n(Q)uit")


main()
