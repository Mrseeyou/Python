import random
from tkinter import *
import threading
import queue
import time


class Food():
    '''
    功能:
        1.前端概述.出现在画面的某一个地方
        2.常用标签.一旦被吃,则增加蛇的分数
        3.控件.
    '''

    def __init__(self, queue):
        self.queue = queue

        # 自动产生一个食物
        self.new_food()
    def new_food(self):
        # 随机产生一个食物的坐标过程
        x = random.randrange(50, 480, 10)
        y = random.randrange(50, 280, 10)

        self.position = x, y  # 存放食物的位置
        # 队列,就是一个不能够随意访问内部元素,只能从头弹出一个元素,且只能从队尾追加元素的list
        # 把一个食物产生的消息放入队列
        #
        self.queue.put({"food": self.position})


class Snake(threading.Thread):
    '''
    蛇的功能:
        1.前端概述.蛇能动,由我们的上下左右按键控制
        2.常用标签.蛇每次动,都需要重新计算蛇头的位置
        3.控件.检测是否游戏结束的功能
    '''

    def __init__(self, world, queue):
        threading.Thread.__init__(self)

        self.world = world
        self.queue = queue
        self.direction = "Left"
        self.points_earned = 0  # 游戏分数
        self.food = Food(self.queue)
        self.snake_points = [(490, 50), (480, 50), (470, 50), (460, 50)]

        self.start()

    def run(self):
        '''
        一旦启动多线程 调用此函数
        要求蛇一直都在跑
        '''
        if self.world.is_game_over:
            self._delete()
        while not self.world.is_game_over:
            self.queue.put({"move": self.snake_points})
            time.sleep(0.2)  # 控制蛇的速度
            self.move()

    def move(self):
        '''
        负责蛇的移动:
            1.前端概述.重新计算蛇头的坐标
            2.常用标签.当蛇头跟食物相遇,则加分,重新生成食物,通知word加分
            3.控件.否则,蛇需要继续动
        '''
        new_snake_point = self.cal_new_position()  # 重新计算蛇头的位置

        # 蛇头位置跟食物位置相同
        if self.food.position == new_snake_point:
            self.points_earned += 1  # 得分加1
            self.queue.put({"points_earned": self.points_earned})
            self.food.new_food()  # 食物被吃掉,产生新的食物
            self.snake_points.append(new_snake_point)
        else:
            # 需要注意蛇的信息的保存方式
            # 每次移动是删除存放蛇的最前位置,并在后面追加
            self.snake_points.pop(0)
            # 判断程序是否退出,因为新的蛇可能撞墙了
            self.check_game_over(new_snake_point)
            self.snake_points.append(new_snake_point)

    def cal_new_position(self):
        # 计算新的 蛇头的位置
        last_x, last_y = self.snake_points[-1]
        if self.direction == "Up":  # direction负责存储蛇移动的方向
            new_snake_point = last_x, last_y - 10  # 每次移动的跨度是10像素
        elif self.direction == "Down":
            new_snake_point = last_x, last_y + 10
        elif self.direction == "Left":
            new_snake_point = last_x - 10, last_y
        else: #self.direction == "Right":
            new_snake_point = last_x + 10, last_y
        return (new_snake_point)

    def key_pressed(self, event):
        # keysym是按键名称
        self.direction = event.keysym

    def check_game_over(self, snake_point):
        '''
        判断的依据是蛇头是否和墙相撞
        '''
        # 把蛇头的坐标拿出来,跟墙的坐标进行判断
        x, y = snake_point[0], snake_point[1]
        if not 0 < x < 500 or not 0 < y < 300 or snake_point in self.snake_points:
            self.queue.put({"game_over": True})


class World(Tk):
    '''
    用来模拟整个游戏面板
    '''

    def __init__(self, queue):
        Tk.__init__(self)

        self.queue = queue
        self.is_game_over = False

        # 定义画板
        self.canvas = Canvas(self, width = 500, height = 300, bg='gray')
        self.canvas.pack()

        # 画出蛇和食物
        # 线(蛇)
        self.snake = self.canvas.create_line((0, 0), (0, 0), fill="black", width=10)
        # 食物
        self.food = self.canvas.create_rectangle(0, 0, 0, 0, fill="#FFCC4C", width=10)
        # 得分
        self.points_earned = self.canvas.create_text(450, 20, fill="white", text="SCORE:0")

        self.queue_handler()

    def queue_handler(self):
        try:
            # 需要不断从消息队列拿到消息,所以使用死循环
            while True:
                task = self.queue.get(block=False)

                if task.get("game_over"):
                    self.game_over()
                if task.get("move"):
                    points = [x for point in task["move"] for x in point]
                    # 重新绘制蛇
                    self.canvas.coords(self.snake, *points)

                    # 同样道理,还需要处理食物,得分
                if task.get("food"):
                    self.canvas.coords(self.food, *task["food"], *task["food"])
                if task.get("points_earned"):
                    self.canvas.itemconfigure(self.points_earned,text="SCORE: {}".format(task["points_earned"]))

        except queue.Empty:  # 报出队列为异常
            if not self.is_game_over:
                # after的含义是,在多少毫秒后调用后面的函数
                self.canvas.after(100,self.queue_handler)

    def game_over(self):
        '''
        游戏结束,清理现场
        '''
        self.is_game_over = True
        self.canvas.create_text(250,150,fill = "red",text = "Game Over!")
        qb = Button(self,text = "Quit",command = self.destroy)
        rb = Button(self,text = "Again",command = self.__init__)


if __name__ == "__main__":
    q = queue.Queue()
    world = World(q)
    snake = Snake(world, q)

    world.bind('<Key-Left>', snake.key_pressed)
    world.bind('<Key-Right>', snake.key_pressed)
    world.bind('<Key-Up>', snake.key_pressed)
    world.bind('<Key-Down>', snake.key_pressed)

    world.mainloop()
