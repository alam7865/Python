def NGR(arr):
    st = []
    st.append(-1)

    for x in range(len(arr) - 1, -1, -1):
        pres = arr[x]

        while st and arr[x] >= st[-1]:
            # print("Stack", st)
            st.pop()

        if not st:
            arr[x] = -1
        else:
            arr[x] = st[-1]

        st.append(pres)

    print(arr)


NGR([6, 8, 0, 1, 3])
