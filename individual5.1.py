def main() -> None:
    # scores in descending order for 20 teams
    scores = list(map(int, input("Enter 20 scores in descending order: ").split()))
    points = int(input("Enter team points: "))

    place = scores.index(points) + 1  # no if needed
    print("Place:", place)


if __name__ == "__main__":
    main()
