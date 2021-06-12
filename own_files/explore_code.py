def update(n=[0], symb="x"):
    print(n)
    if n[0] < 10:
        print(n[0])
    else:
        print("p1.stop()")
        return
    # Clock.future(4, update, [n + 1], notes_to_play[i])
    n[0] += 1
    print(n[0])
    update(n)

if __name__ == "__main__":
    update()