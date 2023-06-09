"""
定义一个洗衣机类，其中包含了打开/关闭洗衣机门、设置洗衣模式、设置马达转速、开始洗衣服等方法。
在初始化时，需要传入品牌brand和容量capacity两个参数。洗衣机门的状态is_closed、洗衣模式__mode和马达转速motor_speed都有默认值。
调用wash()方法时，会根据门的状态和模式来执行相应的操作，最终完成洗衣任务。
"""


class WashMachine:
    def __init__(self, name, mm):
        """
        初始化
        :param name:品牌
        :param mm:容量
        """
        self.name = name
        self.mm = mm
        # 门是否打开
        self.__is_close = False
        self.__mode = 0
        self.speed = 0

    def __str__(self):
        return f"品牌：{self.name} 容量：{self.mm}"

    def open_door(self):
        self.__is_close = False

    def close_door(self):
        self.__is_close = True

    def set_mode(self, mode):
        """
        设置洗衣模式
        :param mode:0 无模式
                    1 轻柔模式
                    2 狂飙模式
        :return:
        """
        # 判断输入指令是否正确
        if mode not in [1, 2]:
            print(f"{mode}不是内部指令，请输入正确指令")
            print("1 轻柔模式")
            print("2 狂飙模式")
        else:
            self.__mode = mode

    def start(self):
        # 判断是否关门
        if self.__is_close == False:
            print("waring:请关门")
            return
        # 判断模式是否设置
        if self.__mode == 0:
            print("Waring:请设置模式")
            return
        print(f"清洗开始，当前模式为{self.__mode}")


machine = WashMachine("海尔", 20)
print(machine)
machine.open_door()
# machine.close_door()
machine.set_mode(1)
machine.start()
