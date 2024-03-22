def main():
    total = 0
    while True:
        num = input("Masukkan angka (-1 untuk berhenti): ")
        if num == "-1":
            break
        total += float(num)
    print("Total:", "{:.2f}".format(total))

if __name__ == "__main__":
    main()
