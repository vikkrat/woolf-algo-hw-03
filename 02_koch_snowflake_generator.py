import turtle

def koch_snowflake(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(order-1, size/3)
            turtle.left(angle)

def draw_snowflake(order, size):
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-size/(2**0.5), size/(2**0.5))
    turtle.pendown()
    for _ in range(3):
        koch_snowflake(order, size)
        turtle.right(120)

def main():
    order = int(input("Enter the recursion level (0-6): "))
    size = 300  # Змініть розмір, якщо необхідно
    window = turtle.Screen()
    window.setup(width=750, height=750)
    draw_snowflake(order, size)
    turtle.done()

if __name__ == '__main__':
    main()
