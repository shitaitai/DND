import random  # 导入随机模块

from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类

# 注册插件
@register(name="DND骰子", description="能够为你DND跑团进行一次任意骰面的掷骰", version="0.1", author="师太太")
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
        
        # 匹配 dN 格式的骰子指令，例如 "1d100" 或 "2d12"
        match = re.match(r'(\d+)d(\d+)', msg)
        if match:
            num_dice = int(match.group(1))  # 骰子的数量
            sides = int(match.group(2))      # 骰子的面数
            
            results = [random.randint(1, sides) for _ in range(num_dice)]  # 生成随机结果
            total = sum(results)  # 计算总和
            
            self.ap.logger.debug("Rolled {}d{} for {}, results: {}, total: {}".format(num_dice, sides, ctx.event.sender_id, results, total))
            ctx.add_return("reply", ["You rolled: {} (total: {})".format(results, total)])  # 回复结果
            ctx.prevent_default()  # 阻止该事件默认行为（向接口获取回复）

    # 当收到群消息时触发
    @handler(GroupNormalMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        msg = ctx.event.text_message  # 获取群消息内容
        
        match = re.match(r'(\d+)d(\d+)', msg)
        if match:
            num_dice = int(match.group(1))
            sides = int(match.group(2))
            
            results = [random.randint(1, sides) for _ in range(num_dice)]
            total = sum(results)
            
            self.ap.logger.debug("Group rolled {}d{} for {}, results: {}, total: {}".format(num_dice, sides, ctx.event.sender_id, results, total))
            ctx.add_return("reply", ["Group rolled: {} (total: {})".format(results, total)])
            ctx.prevent_default()

    # 插件卸载时触发
    def __del__(self):
        pass
