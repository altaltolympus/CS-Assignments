# for f1 in range(1, 13):
#     for f2 in range(1, 13):
#         frg = f1 * f2
#         print(f"{f1} * {f2} = {frg}")
#         print()

[[print(f"{f1} * {f2} = {f1*f2}") for f2 in range(1, 13)] for f1 in range(1, 13)]