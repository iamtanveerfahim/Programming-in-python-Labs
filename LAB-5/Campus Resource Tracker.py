resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]


# Task 1: Display all resources
def display_resources(resources):
    if len(resources) == 0:
        print("No resources available.")
        return

    print("\nAll Resources:")
    for resource in resources:
        print("ID:", resource[0])
        print("Name:", resource[1])
        print("Category:", resource[2])
        print("Available Quantity:", resource[3])
        print("--------------------")


# Task 2: Search resources by category
def search_by_category(resources, category):
    found = False

    print("\nResources in category:", category)

    for resource in resources:
        if resource[2].lower() == category.lower():
            print(resource)
            found = True

    if found == False:
        print("No resource found in this category.")


# Task 3: Find unavailable resources
def find_unavailable(resources):
    found = False

    print("\nUnavailable Resources:")

    for resource in resources:
        if resource[3] == 0:
            print(resource)
            found = True

    if found == False:
        print("All resources are available.")


# Function calls
display_resources(resources)
search_by_category(resources, "Electronics")
find_unavailable(resources)
