import time

def main():
    tiempo1 = time.time()
    print(tiempo1)

    time.sleep(5)

    tiempo2 = time.time()
    print(tiempo2)

    print(tiempo2 -tiempo1)

if __name__ == '__main__':
    main()

