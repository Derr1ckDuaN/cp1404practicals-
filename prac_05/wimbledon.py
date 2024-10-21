def main():

    filename = 'wimbledon.csv'  # 确保文件在同一目录下
    champions, countries = read_data(filename)

    champion_count = count_champions(champions)

    print("Wimbledon Champions:")
    for champion, count in sorted(champion_count.items()):
        print(f"{champion} {count}")

    sorted_countries = unique_countries(countries)
    countries_string = ', '.join(sorted_countries)

    print(f"\nThese {len(sorted_countries)} countries have won Wimbledon:")
    print(countries_string)


def read_data(filename):

    champions = []
    countries = []

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            if len(parts) >= 2:
                champions.append(parts[0].strip())
                countries.append(parts[1].strip())

    return champions, countries


def count_champions(champions):

    champion_count = {}

    for champion in champions:
        if champion in champion_count:
            champion_count[champion] += 1
        else:
            champion_count[champion] = 1

    return champion_count


def unique_countries(countries):

    unique_countries_set = set(countries)
    return sorted(unique_countries_set)

main()
