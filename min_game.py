(lambda f: f(f))(
    lambda f, prt=None, field={
        i: {
            j: "\u2588" if int(__import__("random").randint(0, 10) >= 9) else "X"
            for j in range(20)
        }
        for i in range(20)
    }: f(
        f,
        print("\n".join(["".join(row.values()) for row in field.values()])),
        {
            y: {
                x: "X"
                if [
                    "X"
                    if field.get(y + adj_y, {}).get(x + adj_x) in (None, "X")
                    else "\u2588"
                    for adj_y, adj_x in [
                        (y, x)
                        for x in range(-1, 2)
                        for y in range(-1, 2)
                        if not (x == 0 and y == 0)
                    ]
                ].count("\u2588")
                < 2
                or [
                    "X"
                    if field.get(y + adj_y, {}).get(x + adj_x) in (None, "X")
                    else "\u2588"
                    for adj_y, adj_x in [
                        (y, x)
                        for x in range(-1, 2)
                        for y in range(-1, 2)
                        if not (x == 0 and y == 0)
                    ]
                ].count("\u2588")
                > 3
                or (
                    [
                        "X"
                        if field.get(y + adj_y, {}).get(x + adj_x) in (None, "X")
                        else "\u2588"
                        for adj_y, adj_x in [
                            (y, x)
                            for x in range(-1, 2)
                            for y in range(-1, 2)
                            if not (x == 0 and y == 0)
                        ]
                    ].count("\u2588")
                    == 2
                    and field.get(y).get(x) == "X"
                )
                else "\u2588"
                for x in range(20)
            }
            for y in range(20)
        }
        if input() != "q"
        else exit(),
    )
)
