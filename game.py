import random


def main():
    answer = random.randint(1, 100)
    attempts = 0

    print("猜數字遊戲開始！我已經選好 1 到 100 的整數。")

    while True:
        user_input = input("請輸入你的猜測：").strip()

        try:
            guess = int(user_input)
        except ValueError:
            print("輸入無效，請輸入 1 到 100 的整數。")
            continue

        if guess < 1 or guess > 100:
            print("超出範圍，請輸入 1 到 100 的整數。")
            continue

        attempts += 1

        if guess < answer:
            print("太小了")
        elif guess > answer:
            print("太大了")
        else:
            print(f"答對了！你總共猜了 {attempts} 次。")
            break


if __name__ == "__main__":
    main()
