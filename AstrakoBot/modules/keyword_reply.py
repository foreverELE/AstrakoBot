# AstrakoBot/modules/keyword_reply.py

import html
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, MessageHandler, Filters

from AstrakoBot import dispatcher

def keyword_handler(update: Update, context: CallbackContext):
    # 检查消息是否存在
    if not update.message or not update.message.text:
        return
        
    text = update.message.text.strip().lower()
    chat = update.effective_chat
    
    # 添加调试日志
    print(f"[KEYWORD] 聊天类型: {chat.type}, 收到消息: {text}")
    
    if "官网" in text or "导航" in text:
        update.message.reply_text(
            "🚀 bite321，你的 Web3 从这里开始\n🔗 https://bite321.com",
            parse_mode=ParseMode.HTML
        )
        return

    elif "学院" in text or "入门" in text:
        update.message.reply_text(
            "📗 bite321 学院首页\n👉 https://learn.bite321.com/\n\n"
            "🗺️ BITE321 指南 - 从零开始学习 Web3\n👉 https://learn.bite321.com/reading-guide/",
            parse_mode=ParseMode.HTML
        )
        return

    elif "买币" in text:
        update.message.reply_text(
            "🪙 拥有你的第「1」枚比特币（BTC）\n👉 https://learn.bite321.com/buy-your-first-bitcoin/\n\n"
            "💡 通过 bite321 快速注册你的欧易 OKX 账户\n👉 https://learn.bite321.com/how-to-register-okx/",
            parse_mode=ParseMode.HTML
        )
        return

    elif "比特币" in text:
        update.message.reply_text(
            "📖 一文读懂加密货币：从比特币到数字资产\n👉 https://learn.bite321.com/cryptocurrency-the-future-of-digital-finance/\n\n"
            "📘 比特币（BTC）：数字时代的“黄金”\n👉 https://learn.bite321.com/what-is-bitcoin/",
            parse_mode=ParseMode.HTML
        )
        return

    elif "推荐" in text:
        update.message.reply_text(
            "📌 精选推荐合集：\n👉 https://learn.bite321.com/tag/recommendations/",
            parse_mode=ParseMode.HTML
        )
        return

    else:
        update.message.reply_text(
            "🤖 暂时不理解你的问题，可以发送关键词如：导航 / 学院 / 买币 / 比特币 / 推荐",
            parse_mode=ParseMode.HTML
        )

__help__ = """
智能关键词回复功能：

- 输入 "官网" 或 "导航"：获取官网地址
- 输入 "学院" 或 "入门"：获取学习资源  
- 输入 "买币"：获取买币教程
- 输入 "比特币"：获取比特币介绍
- 输入 "推荐"：获取精选内容

*支持群聊和私聊*
"""

# 修改过滤器：移除群组限制，支持私聊和群聊
KEYWORD_HANDLER = MessageHandler(
    Filters.text & ~Filters.command,  # 移除了 Filters.chat_type.groups
    keyword_handler
)

# 注册到dispatcher
dispatcher.add_handler(KEYWORD_HANDLER)

__mod_name__ = "关键词助手"
__handlers__ = [KEYWORD_HANDLER]