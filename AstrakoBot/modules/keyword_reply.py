# AstrakoBot/modules/keyword_reply.py

from telegram import Update
from telegram.ext import CallbackContext, MessageHandler, Filters

def keyword_handler(update: Update, context: CallbackContext):
    text = update.message.text.strip().lower()
    print(f"[DEBUG] 用户输入：{text}")  # 日志调试用，可删

    if any(kw in text for kw in ["官网", "导航"]):
        update.message.reply_text("🔗 我们的官网是：https://bite321.com")
    elif any(kw in text for kw in ["学院", "入门"]):
        update.message.reply_text("📗 bite321学院：https://learn.bite321.com/")
    elif any(kw in text for kw in ["怎么买币", "买币"]):
        update.message.reply_text("🪙 新手买币教程：https://learn.bite321.com/how-to-register-okx/")
    elif "比特币" in text:
        update.message.reply_text("✨ 比特币（BTC）：https://learn.bite321.com/what-is-bitcoin/")
    elif "推荐" in text:
        update.message.reply_text("✨ 精选推荐：https://learn.bite321.com/tag/recommendations/")
    else:
        update.message.reply_text("🤖 暂时不理解你的问题，可以输入关键词如：官网 / 学院 / 买币 / 推荐")


__mod_name__ = "Keyword助手"

__help__ = """
你可以输入关键词，我会自动回答常见问题：

- 输入 “官网”：获取官网地址
- 输入 “白皮书”：获取项目文档
- 输入 “怎么买币” 或 “买币”：获取买币教程
- 输入 “推荐”：获取精选推荐内容
"""

def __handlers__():
    return [
        MessageHandler(Filters.text & ~Filters.command, keyword_handler),
    ]
