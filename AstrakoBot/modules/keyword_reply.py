# AstrakoBot/modules/keyword_reply.py

import html
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, MessageHandler, Filters

from AstrakoBot import dispatcher
from AstrakoBot.modules.disable import DisableAbleCommandHandler

def keyword_handler(update: Update, context: CallbackContext):
    # 检查消息是否存在
    if not update.message or not update.message.text:
        return
        
    text = update.message.text.strip().lower()
    chat = update.effective_chat
    
    # 只在群组中响应，避免私聊冲突
    if chat.type == "private":
        return
    
    # 添加调试日志
    print(f"[KEYWORD] 收到消息: {text}")
    
    if "官网" in text or "导航" in text:
        update.message.reply_text(
            "🔗 我们的官网是：https://bite321.com",
            parse_mode=ParseMode.HTML
        )
        return
    elif "学院" in text or "入门" in text:
        update.message.reply_text(
            "📗 bite321学院：https://learn.bite321.com/",
            parse_mode=ParseMode.HTML
        )
        return
    elif "怎么买币" in text or "买币" in text:
        update.message.reply_text(
            "🪙 新手买币教程：https://learn.bite321.com/how-to-register-okx/",
            parse_mode=ParseMode.HTML
        )
        return
    elif "比特币" in text:
        update.message.reply_text(
            "✨ 比特币（BTC）：数字时代的‘黄金’：https://learn.bite321.com/what-is-bitcoin/",
            parse_mode=ParseMode.HTML
        )
        return
    elif "推荐" in text:
        update.message.reply_text(
            "✨ 精选推荐：https://learn.bite321.com/tag/recommendations/",
            parse_mode=ParseMode.HTML
        )
        return

__help__ = """
智能关键词回复功能：

- 输入 "官网" 或 "导航"：获取官网地址
- 输入 "学院" 或 "入门"：获取学习资源  
- 输入 "买币"：获取买币教程
- 输入 "比特币"：获取比特币介绍
- 输入 "推荐"：获取精选内容

*注意：仅在群组中生效*
"""

# 创建处理器
KEYWORD_HANDLER = MessageHandler(
    Filters.text & ~Filters.command & Filters.chat_type.groups,
    keyword_handler
)

# 注册到dispatcher
dispatcher.add_handler(KEYWORD_HANDLER)

__mod_name__ = "关键词助手"
__handlers__ = [KEYWORD_HANDLER]