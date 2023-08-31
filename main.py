import random

def get_movie_names():
    movie_names = []
    while True:
        movie_name = input("Enter a movie name (or 'stop' to end): ")
        if movie_name.lower() == "stop":
            break
        movie_names.append(movie_name)
    return movie_names

def choose_random_movie(movie_names):
    if movie_names:
        return random.choice(movie_names)
    return None

if __name__ == "__main__":
    print("Enter movie names (type 'stop' to end):")
    movie_list = get_movie_names()
    chosen_movie = choose_random_movie(movie_list)
    if chosen_movie:
        print("Randomly chosen movie:", chosen_movie)
    else:
        print("No movie names entered.")
