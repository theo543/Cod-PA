def union(intervals : list[tuple[int, int]]):
    intervals = sorted(intervals)
    ret = [intervals[0]]
    for item in intervals[1:]:
        if item[0] <= ret[-1][1]:
            ret[-1] = (ret[-1][0], max(ret[-1][1], item[1]))
        else:
            ret.append(item)
    return ret


def main():
    with open("autostrada.in") as fin, open("autostrada.out", "w") as fout:
        intervals = fin.readlines()
        len = int(intervals[0])
        intervals = [(int(x[0]), int(x[1])) for x in [line.split() for line in intervals[1:]]]
        intervals = [item if item[0] < item[1] else (item[1], item[0]) for item in intervals]
        intervals = union(intervals)
        print(*[f"[{x[0]}, {x[1]}]" for x in intervals], sep='\n', file=fout)
        open_intervals = [(0,0)] + intervals + [(len,len)]
        open_intervals = [(left[1], right[0]) for left, right in zip(open_intervals, open_intervals[1:])]
        open_intervals = [interval for interval in open_intervals if interval[0] != interval[1]]
        print(file=fout)
        print(*[f"({x[0]}, {x[1]})" for x in open_intervals], sep='\n', file=fout)
        print(file=fout)
        damage = sum([right - left for left, right in intervals])
        print(f"{damage * 100 // len}%", file=fout)

if __name__ == "__main__":
    main()
