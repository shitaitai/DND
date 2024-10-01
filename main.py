import random  # 导入随机模块

from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类

# 注册插件
@register(name="RandomRoll", description="Roll a 100-sided die", version="0.1", author="RockChinQ")
class MyPlugin(BasePlugin):
    # 插件加载时触发
    def __init__(self, host: APIHost):
        pass
    
    # 异步初始化
    async def initialize(self):
        pass
    
    # 当收到个人消息时触发
    @handler(PersonNormalMessageReceived)
    async def person_normal_message_received(self, ctx: EventContext):
        msg = ctx.event.text_message  # 获取发送的消息内容
        if msg == "1d100":  # 如果消息为"1d100"
            result = random.randint(1, 100)  # 生成1到100之间的随机数
            self.ap.logger.debug("Rolled a dice for {}, result: {}".format(ctx.event.sender_id, result))  # 输出调试信息
            ctx.add_return("reply", ["You rolled a {}!".format(result)])  # 回复结果
            ctx.prevent_default()  # 阻止该事件默认行为（向接口获取回复）

    # 当收到群消息时触发
    @handler(GroupNormalMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        msg = ctx.event.text_message  # 获取群消息内容
        if msg == "1d100":  # 如果消息为"1d100"
            result = random.randint(1, 100)  # 生成1到100之间的随机数
            self.ap.logger.debug("Rolled a dice in group for {}, result: {}".format(ctx.event.sender_id, result))  # 输出调试信息
            ctx.add_return("reply", ["Group rolled a {}!".format(result)])  # 回复结果
            ctx.prevent_default()  # 阻止该事件默认行为（向接口获取回复）

    # 插件卸载时触发
    def __del__(self):
        pass
