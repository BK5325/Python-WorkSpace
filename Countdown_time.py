import time

def countdown(t):
    """
    Countdown timer.

    Args:
        t (int): Time in seconds.

    Returns:
        None
    """
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Time Up!!')

def main():
    t = input("Enter the time in seconds: ")
    try:
        t = int(t)
        if t < 0:
            print("Time cannot be negative.")
        else:
            countdown(t)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()