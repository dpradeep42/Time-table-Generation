import csv
import random
import copy

# Define classes for entities
class Course:
    def __init__(self, courseCode, courseName, number):
        self.courseCode = courseCode
        self.courseName = courseName
        self.number = number

class Registration:
    def __init__(self, studentName, registeredCourses):
        self.studentName = studentName
        self.registeredCourses = registeredCourses

class Exam:
    def __init__(self, startTime, roomNo, day, invigilator):
        self.startTime = startTime
        self.roomNo = roomNo
        self.day = day
        self.invigilator = invigilator

class Individual:
    def __init__(self, chromosome, value):
        self.chromosome = chromosome
        self.value = value

# Helper functions for loading data
def load_data():
    courses, registrations, instructors = [], [], []
    
    # Load courses
    with open('courses.csv') as file:
        reader = csv.reader(file)
        for count, row in enumerate(reader):
            if row:
                courses.append(Course(row[0], row[1], count))

    # Load instructors
    with open('teachers.csv') as file:
        reader = csv.reader(file)
        for count, row in enumerate(reader):
            if row:
                instructors.append((row[0], count))

    # Load student registrations
    with open('studentNames.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                registrations.append(Registration(row[0], []))

    with open('studentCourse.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0]:
                for reg in registrations:
                    if reg.studentName == row[1]:
                        reg.registeredCourses.append(row[2])

    return courses, registrations, instructors

# Fitness and Genetic Algorithm methods
def calculate_fitness(population):
    for individual in population:
        individual.value = random.randint(0, 400)  # Simplified fitness calculation
    return population

def generate_population(size, courses):
    population = []
    for _ in range(size):
        chromosome = [random.choice(courses) for _ in range(len(courses))]
        population.append(Individual(chromosome, value=-1))
    return calculate_fitness(population)

# Main algorithm

def run_algorithm(courses, registrations, instructors):
    population_size = 100
    population = generate_population(population_size, courses)
    best_solution = max(population, key=lambda ind: ind.value)

    return best_solution

# Generate a timetable
def generate_timetable():
    courses, registrations, instructors = load_data()
    best_solution = run_algorithm(courses, registrations, instructors)
    return best_solution

if __name__ == "__main__":
    best_timetable = generate_timetable()
    print("Best Timetable:", best_timetable)
