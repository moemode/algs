from typing import Iterable
from dataclasses import dataclass


@dataclass
class Item:
    value: int
    count: int


@dataclass
class Booking:
    start: int
    end: int
    n_rooms: int


def negate_counts(numbers: list[Item]):
    for item in numbers:
        item.count = -item.count
    return numbers


def satisfying_booking(
    talk_requests: list[tuple[int, int]]
) -> tuple[tuple[int, int, int], ...]:
    """
    Input:  R | Tuple of |R| talk request tuples (s, t)
    Output: B | Tuple of room booking triples (k, s, t)
              | that is the booking schedule that satisfies R
    """
    if not talk_requests:
        return ()
    start_times = map(lambda t: t[0], talk_requests)
    end_times = map(lambda t: t[1], talk_requests)
    start_time_counts = get_counts(sorted(start_times))
    end_time_counts = negate_counts(get_counts(sorted(end_times)))
    largest_end_time = end_time_counts[-1].value
    schedule = [Booking(start_time_counts[0].value, -1, start_time_counts[0].count)]
    # index of next start time to be processed
    s = 1
    # index of next end time to be processed
    e = 0
    while s < len(start_time_counts) or e < len(end_time_counts):
        current_booking = schedule[-1]
        next_start = (
            start_time_counts[s]
            if s < len(start_time_counts)
            else Item(largest_end_time + 1, 0)
        )
        next_end = end_time_counts[e]
        if next_start.value == next_end.value:
            d = next_start.count + next_end.count
            s += 1
            e += 1
        elif next_start.value < next_end.value:
            d = next_start.count
            s += 1
        else:
            d = next_end.count
            e += 1
        if d != 0:
            next_change = min(next_start.value, next_end.value)
            n_rooms = current_booking.n_rooms + d
            current_booking.end = next_change
            if next_change != largest_end_time:
                schedule.append(Booking(next_change, -1, n_rooms))
    return tuple(
        map(lambda booking: (booking.n_rooms, booking.start, booking.end), schedule)
    )


def get_counts(sorted_numbers: Iterable[int]) -> list[Item]:
    if not sorted_numbers:
        return []
    sorted_numbers = sorted_numbers.__iter__()
    counts = [Item(next(sorted_numbers), 1)]
    for n in sorted_numbers:
        prev = counts[-1]
        if n != prev.value:
            counts.append(Item(n, 1))
        else:
            prev.count += 1
    return counts


if __name__ == "__main__":
    # l = [7, 39, 2, 138, 7, 9, 7, 2, 34]
    # print(get_counts(sorted(l)))
    r = [(0, 2), (3, 4), (1, 15), (0, 3), (0, 10), (0, 14)]
    s = satisfying_booking(r)
    print(s)
