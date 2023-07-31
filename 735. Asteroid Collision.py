def asteroidCollision(asteroids: list[int]) -> list[int]:
    st = []
    for i in range(len(asteroids)):
        while len(st) and st[-1] > 0 and asteroids[i] < 0:
            if st[-1] + asteroids[i] == 0:
                st.pop()
                break
            elif st[-1] + asteroids[i] > 0:
                break
            elif st[-1] + asteroids[i] < 0:
                st.pop()
        else:
            st.append(asteroids[i])

    return st


print(
    asteroidCollision(asteroids = [2, -2])
)

# print(
#     asteroidCollision(asteroids = [5,-5])
# )