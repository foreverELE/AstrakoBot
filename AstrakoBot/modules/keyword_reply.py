from telegram import Update
from telegram.ext import CallbackContext, MessageHandler, filters

def keyword_handler(update: Update, context: CallbackContext):
    # 仅私聊触发
    if update.effective_chat.type != "private":
        return

    text = update.message.text.strip().lower()
    print(f"[DEBUG] 用户输入：{text}")  # 如果 systemd 没有重定向，可能看不到

    if "官网" in text or "导航" in text:
        update.message.reply_text("🔗 我们的官网是：https://bite321.com")
    elif "学院" in text or "入门" in text:
        update.message.reply_text("📗 bite321学院：https://learn.bite321.com/")
    elif "怎么买币" in text or "买币" in text:
        update.message.reply_text("🪙 新手买币教程：https://learn.bite321.com/how-to-register-okx/")
    elif "比特币" in text:
        update.message.reply_text("✨ 比特币（BTC）：数字时代的“黄金”：https://learn.bite321.com/what-is-bitcoin/")
    elif "推荐" in text:
        update.message.reply_text("✨ 精选推荐：https://learn.bite321.com/tag/recommendations/")
    else:
        update.message.reply_text("🤖 暂时不理解你的问题，可以输入关键词如：官网 / 白皮书 / 买币 / 推荐")

# 注册为 handler
KEYWORD_HANDLER = MessageHandler(filters.TEXT & (~filters.COMMAND), keyword_handler)

__mod_name__ = "KeywordReply"
__handlers__ = [KEYWORD_HANDLER]
