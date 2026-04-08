def calc_avg(scores: list[int]) -> float:
    return sum(scores) / len(scores) if scores else 0.0

def run_demo() -> None:
    scores = [90, 99, 85, 77, 100, 88]
    names = ["Alice", "Bob", "Chris"]

    print("Avg:", calc_avg(scores))

if __name__== '__main__':
    run_demo()
