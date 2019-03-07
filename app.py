# map blog name to blog object
blogs = dict()


def menu():
    # Show the user the available blog's
    # Let user make a choice
    # Do something with that choice
    # Exit
    print_blogs()


def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))


menu()
