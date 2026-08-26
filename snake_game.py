import random
import tkinter as tk

WIDTH = 500
HEIGHT = 500
GRID = 20
SPEED = 120


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.root.configure(bg="#0f172a")
        self.root.resizable(False, False)
        self.root.bind("<KeyPress>", self.on_key)
        self.root.focus_set()

        self.canvas = tk.Canvas(
            self.root,
            width=WIDTH,
            height=HEIGHT,
            bg="#0b1020",
            highlightthickness=0,
        )
        self.canvas.pack(padx=10, pady=10)

        self.score_var = tk.StringVar(value="Score: 0")
        tk.Label(
            self.root,
            textvariable=self.score_var,
            bg="#0f172a",
            fg="#f8fafc",
            font=("Arial", 12, "bold"),
        ).pack()

        self.reset_game()
        self.run()

    def reset_game(self):
        self.snake = [(10, 10), (9, 10), (8, 10)]
        self.direction = (1, 0)
        self.next_direction = (1, 0)
        self.score = 0
        self.game_over = False
        self.food = self.spawn_food()
        self.score_var.set("Score: 0")
        self.draw()

    def spawn_food(self):
        while True:
            x = random.randint(0, (WIDTH // GRID) - 1)
            y = random.randint(0, (HEIGHT // GRID) - 1)
            if (x, y) not in self.snake:
                return (x, y)

    def on_key(self, event):
        key = event.keysym.lower()

        move_map = {
            "up": (0, -1),
            "down": (0, 1),
            "left": (-1, 0),
            "right": (1, 0),
            "w": (0, -1),
            "s": (0, 1),
            "a": (-1, 0),
            "d": (1, 0),
        }

        if key == "r":
            self.reset_game()
            self.run()
            return

        if key in move_map:
            new_dir = move_map[key]
            if new_dir != (-self.direction[0], -self.direction[1]):
                self.next_direction = new_dir

    def is_collision(self, head):
        x, y = head
        if x < 0 or y < 0 or x >= WIDTH // GRID or y >= HEIGHT // GRID:
            return True
        if head in self.snake[:-1]:
            return True
        return False

    def move(self):
        if self.game_over:
            return

        self.direction = self.next_direction
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        if self.is_collision(new_head):
            self.game_over = True
            self.draw()
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.score_var.set(f"Score: {self.score}")
            self.food = self.spawn_food()
        else:
            self.snake.pop()

        self.draw()
        self.root.after(SPEED, self.move)

    def draw(self):
        self.canvas.delete("all")

        for x in range(0, WIDTH, GRID):
            self.canvas.create_line(x, 0, x, HEIGHT, fill="#1f2937")
        for y in range(0, HEIGHT, GRID):
            self.canvas.create_line(0, y, WIDTH, y, fill="#1f2937")

        for index, (x, y) in enumerate(self.snake):
            fill = "#22c55e" if index == 0 else "#16a34a"
            self.canvas.create_rectangle(
                x * GRID + 1,
                y * GRID + 1,
                (x + 1) * GRID - 1,
                (y + 1) * GRID - 1,
                fill=fill,
                outline="#14532d",
                width=2,
            )

        fx, fy = self.food
        self.canvas.create_rectangle(
            fx * GRID + 4,
            fy * GRID + 4,
            (fx + 1) * GRID - 4,
            (fy + 1) * GRID - 4,
            fill="#ef4444",
            outline="#b91c1c",
            width=2,
        )

        if self.game_over:
            self.canvas.create_text(
                WIDTH / 2,
                HEIGHT / 2,
                text="Game Over\nPress R to restart",
                fill="#f8fafc",
                font=("Arial", 18, "bold"),
                justify="center",
            )

    def run(self):
        self.root.after(SPEED, self.move)


if __name__ == "__main__":
    root = tk.Tk()
    SnakeGame(root)
    root.mainloop()
