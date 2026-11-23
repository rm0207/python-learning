# 時間を止めるための機能を読み込む
import time

# 作業時間と休憩時間を「分」で設定する
WORK_MINUTES = 25
BREAK_MINUTES = 5


# タイマーを動かす関数
# minutes: 時間（分）
# label: 「作業」「休憩」など、画面に表示する名前
def countdown(minutes, label):
    # 分を秒に変換する（例：25分なら1500秒）
    seconds_left = minutes * 60

    # タイマー開始を表示する
    print(f"\n{label}を始めます（{minutes}分）")

    # 残り時間が0秒になるまで繰り返す
    while seconds_left > 0:
        # divmodで秒を「分」と「秒」に分ける
        minutes_left, seconds = divmod(seconds_left, 60)

        # \rで同じ行の先頭に戻り、残り時間を更新する
        # flush=Trueで表示をすぐに画面へ反映する
        print(
            f"\r残り {minutes_left:02d}:{seconds:02d}",
            end="",
            flush=True
        )

        # 1秒待つ
        time.sleep(1)

        # 残り秒数を1つ減らす
        seconds_left -= 1

    # タイマー終了を表示する
    print(f"\n{label}終了！")


# プログラム全体を動かす関数
def main():
    print("ポモドーロタイマー")
    print("Ctrl+C で終了できます。")

    try:
        # 作業と休憩を繰り返す
        while True:
            countdown(WORK_MINUTES, "作業")
            countdown(BREAK_MINUTES, "休憩")

    # Ctrl+Cが押されたら、エラーを出さずに終了する
    except KeyboardInterrupt:
        print("\nタイマーを終了しました。")


# このファイルを直接実行したときだけmain()を呼び出す
if __name__ == "__main__":
    main()
