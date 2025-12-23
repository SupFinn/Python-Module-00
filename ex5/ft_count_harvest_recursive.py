def ft_count_harvest_recursive(days: int) -> None:
    days = int(input("Days until harvest: "))
    if days == 0:
        print("Harvest time!")
        return
    ft_count_harvest_recursive()
    print(f"Day {days}")

ft_count_harvest_recursive(5)